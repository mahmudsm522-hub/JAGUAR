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
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

...

for task in tasks:

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📂 Open",
                    url=task[3]
                )
            ],
            [
                InlineKeyboardButton(
                    text="✅ Verify",
                    callback_data=f"verify_{task[0]}"
                )
            ]
        ]
    )

    await message.answer(
        f"""
📌 <b>{task[1]}</b>

💰 Reward: {task[4]} JGR
""",
        reply_markup=keyboard
    )
