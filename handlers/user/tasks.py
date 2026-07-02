from aiogram import Router, F
from aiogram.types import Message

from utils.database import get_active_tasks
from aiogram import F
from aiogram.types import CallbackQuery

from utils.database import (
    get_task,
    is_task_completed,
    complete_task,
    add_balance,
    add_transaction
)

from utils.checker import is_joined
router = Router()

@router.callback_query(F.data.startswith("verify_"))
async def verify_task(callback: CallbackQuery):

    task_id = int(callback.data.split("_")[1])

    task = get_task(task_id)

    if not task:

        await callback.answer(
            "Task not found.",
            show_alert=True
        )
        return

    if is_task_completed(callback.from_user.id, task_id):

        await callback.answer(
            "Already completed.",
            show_alert=True
        )
        return

    # A yanzu muna duba Main Channel kawai.
    joined = await is_joined(
        callback.bot,
        callback.from_user.id
    )

    if not joined:

        await callback.answer(
            "Join the channel first.",
            show_alert=True
        )
        return

    reward = task[4]

    add_balance(
        callback.from_user.id,
        reward
    )

    complete_task(
        callback.from_user.id,
        task_id
    )

    from datetime import datetime

    add_transaction(
        callback.from_user.id,
        "task_reward",
        reward,
        task[1],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    await callback.answer(
        "Reward Added!",
        show_alert=True
    )

    await callback.message.answer(
        f"🎉 Task completed!\n\n🪙 +{reward} JGR has been added to your balance."
    )
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
