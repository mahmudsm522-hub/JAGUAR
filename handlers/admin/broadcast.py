from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.config import ADMIN_ID
from handlers.admin.states import BroadcastState
from utils.database import get_all_users

router = Router()


@router.message(Command("broadcast"))
async def start_broadcast(message: Message, state: FSMContext):

    if message.from_user.id != ADMIN_ID:
        return

    await state.set_state(BroadcastState.waiting_message)

    await message.answer(
        "📢 Send the message you want to broadcast."
    )


@router.message(BroadcastState.waiting_message)
async def send_broadcast(message: Message, state: FSMContext):

    users = get_all_users()

    sent = 0
    failed = 0

    for user in users:

        try:
            await message.bot.copy_message(
                chat_id=user[0],
                from_chat_id=message.chat.id,
                message_id=message.message_id
            )

            sent += 1

        except Exception:

            failed += 1

    await state.clear()

    await message.answer(
        f"""
✅ Broadcast Completed

📨 Sent: {sent}

❌ Failed: {failed}
"""
)
