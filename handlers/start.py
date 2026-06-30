from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards.join import join_keyboard
from utils.checker import is_joined
from utils.database import create_user
from keyboards.menu import main_menu

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):

    user = message.from_user

    joined = await is_joined(
        message.bot,
        user.id
    )

    if not joined:

        await message.answer(
            "🐆 Welcome to Jaguar!\n\n"
            "📢 Please join our official channel first.",
            reply_markup=join_keyboard
        )

        return

    new_user = create_user(
        user.id,
        user.username,
        user.first_name
    )

    if new_user:

        await message.answer(
            "🎉 Registration Successful!\n\n"
            "🎁 Welcome Bonus\n"
            "+500 JGR"
        )

    await message.answer(
        "🏠 Welcome to Jaguar!",
        reply_markup=main_menu
    )


@router.callback_query(F.data == "verify_join")
async def verify_join(callback: CallbackQuery):

    joined = await is_joined(
        callback.bot,
        callback.from_user.id
    )

    if not joined:

        await callback.answer(
            "❌ Please join the channel first.",
            show_alert=True
        )

        return

    create_user(
        callback.from_user.id,
        callback.from_user.username,
        callback.from_user.first_name
    )

    await callback.message.edit_text(
        "✅ Verification Successful!\n\n"
        "Welcome to Jaguar."
    )

    await callback.message.answer(
        "🏠 Main Menu",
        reply_markup=main_menu
        )
