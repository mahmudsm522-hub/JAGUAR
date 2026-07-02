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
