from aiogram import Router, F
from aiogram.types import Message

from utils.database import get_active_tasks

router = Router()


@router.message(F.text == "📋 Tasks")
async def tasks_menu(message: Message):

    tasks = get_active_tasks()

    if not tasks:
        await message.answer(
            "📭 No tasks available at the moment."
        )
        return

    text = "📋 <b>Available Tasks</b>\n\n"

    for task in tasks:
        text += (
            f"🆔 {task[0]}\n"
            f"📌 {task[1]}\n"
            f"💰 Reward: {task[4]} JGR\n\n"
        )

    text += "\n👇 Select a task below."

    await message.answer(text)
