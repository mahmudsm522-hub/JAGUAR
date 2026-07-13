from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.user.menu import main_menu
from utils.database import create_user

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    create_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.first_name
    )

    await message.answer(
        f"""
👋 Welcome <b>{message.from_user.first_name}</b>

🐆 Welcome to Jaguar Bot

🎁 Earn JGR by:
• Completing Tasks
• Daily Rewards
• Inviting Friends

💸 Minimum Withdraw: <b>10,000 JGR</b>

Choose an option below.
""",
        reply_markup=main_menu
    )
