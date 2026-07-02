from aiogram import Router, F
from aiogram.types import Message
from keyboards.user.wallet import withdraw_type_keyboard
from utils.database import get_balance

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
