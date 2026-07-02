from aiogram import Router, F
from aiogram.types import Message
from keyboards.user.wallet import withdraw_type_keyboard
from utils.database import get_balance
from aiogram.types importCallbackQuery
from aiogram.fsm.context import FSMContext
from handlers.user.states import WithdrawState
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
