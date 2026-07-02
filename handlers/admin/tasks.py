from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from bot.config import ADMIN_ID
from handlers.admin.states import AddTask
from utils.database import add_task

router = Router()


@router.message(Command("addtask"))
async def add_task_start(message: Message, state: FSMContext):

    if message.from_user.id != ADMIN_ID:
        return

    await state.set_state(AddTask.waiting_for_title)

    await message.answer("📝 Send Task Title")
    

@router.message(AddTask.waiting_for_title)
async def task_title(message: Message, state: FSMContext):

    await state.update_data(title=message.text)

    await state.set_state(AddTask.waiting_for_type)

    await message.answer(
        "Task Type?\n\n"
        "Example:\n"
        "channel\n"
        "group\n"
        "bot"
    )


@router.message(AddTask.waiting_for_type)
async def task_type(message: Message, state: FSMContext):

    await state.update_data(task_type=message.text.lower())

    await state.set_state(AddTask.waiting_for_link)

    await message.answer("🔗 Send Task Link")


@router.message(AddTask.waiting_for_link)
async def task_link(message: Message, state: FSMContext):

    await state.update_data(link=message.text)

    await state.set_state(AddTask.waiting_for_reward)

    await message.answer("💰 Send Reward (JGR)")


@router.message(AddTask.waiting_for_reward)
async def task_reward(message: Message, state: FSMContext):

    if not message.text.isdigit():

        await message.answer("❌ Reward must be a number.")

        return

    data = await state.get_data()

    add_task(
        title=data["title"],
        task_type=data["task_type"],
        link=data["link"],
        reward=int(message.text)
    )

    await state.clear()

    await message.answer(
        "✅ Task Added Successfully!"
)
