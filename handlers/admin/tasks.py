from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.config import ADMIN_ID
from utils.database import add_task

router = Router()


@router.message(Command("addtask"))
async def add_task_command(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    text = (
        "📌 Send task in this format:\n\n"
        "Title | Type | Link | Reward\n\n"
        "Example:\n"
        "Join Jaguar Channel|channel|https://t.me/Jaguar|500"
    )

    await message.answer(text)
