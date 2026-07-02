WithdrawState aiogram import Router, F
from aiogram.types import Message
from keyboards.user.wallet import withdraw_type_keyboard
from utils.database import get_balance
from aiogram.types importCallbackQuery
from aiogram.fsm.context import FSMContext
from handlers.user.states import WithdrawState
from utils.database import (
    get_balance,
    create_withdraw
)
router = Router()
from bot.config import ADMIN_ID
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@router.message(F.text == "👛 Wallet")
async def wallet_menu(message: Message):

    user_id = message.from_user.id

    balance = get_balance(user_id)

    text = f"""
👛 <b>JAGUAR WALLET</b>

━━━━━━━━━━━━━━

💰 Balance:
<b>{balance} JGR</b>

💸 Minimum Withdraw:
<b>10,000 JGR</b>

━━━━━━━━━━━━━━

Choose an option below.
"""

    await message.answer(text)

@router.callback_query(F.data == "withdraw")
async def withdraw_menu(callback: CallbackQuery):

    await callback.message.answer(
        "💸 Select Wallet Type",
        reply_markup=withdraw_type_keyboard
    )

    await callback.answer()
@router.callback_query(F.data.startswith("wallet_"))
async def wallet_type_selected(
    callback: CallbackQuery,
    state: FSMContext
):

    wallet_type = callback.data.replace("wallet_", "")

    await state.update_data(wallet_type=wallet_type)

    await state.set_state(
        WithdrawState.waiting_wallet_address
    )

    await callback.message.answer(
        "📥 Send your wallet address (or Binance UID)."
    )

    await callback.answer()
@router.message(WithdrawState.waiting_wallet_address)
async def wallet_address(
    message: Message,
    state: FSMContext
):

    await state.update_data(
        wallet_address=message.text
    )

    await state.set_state(
        WithdrawState.waiting_amount
    )

    await message.answer(
        "💰 Enter withdrawal amount (JGR)."
    )
@router.message(WithdrawState.waiting_amount)
async def withdraw_amount(
    message: Message,
    state: FSMContext
):

    if not message.text.isdigit():

        await message.answer(
            "❌ Please enter numbers only."
        )
        return

    amount = int(message.text)

    if amount < 10000:

        await message.answer(
            "❌ Minimum withdrawal is 10,000 JGR."
        )
        return

    balance = get_balance(message.from_user.id)

    if amount > balance:

        await message.answer(
            "❌ Insufficient balance."
        )
        return

    data = await state.get_data()

    create_withdraw(
        user_id=message.from_user.id,
        wallet_address=data["wallet_address"],
        amount=amount
    )
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Approve",
                callback_data=f"approve_{message.from_user.id}"
            ),
            InlineKeyboardButton(
                text="❌ Reject",
                callback_data=f"reject_{message.from_user.id}"
            )
        ]
    ]
)

await message.bot.send_message(
    ADMIN_ID,
    f"""
💸 <b>New Withdrawal Request</b>

👤 User:
@{message.from_user.username}

🆔 ID:
<code>{message.from_user.id}</code>

💳 Wallet Type:
{data['wallet_type']}

🏦 Wallet:
<code>{data['wallet_address']}</code>

💰 Amount:
<b>{amount} JGR</b>

Status:
⏳ Pending
""",
    reply_markup=keyboard
)
    await state.clear()

    await message.answer(
        f"""
✅ Withdrawal request submitted.

💰 Amount: {amount} JGR

⏳ Status: Pending Admin Approval.
"""
)
