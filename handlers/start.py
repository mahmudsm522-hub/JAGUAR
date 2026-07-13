from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from utils.database import create_user
from keyboards.user.main import main_keyboard

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

🎁 Complete tasks
👥 Invite friends
💰 Earn JGR
🏦 Withdraw rewards

Choose an option below.
""",
        reply_markup=main_keyboard
  )
