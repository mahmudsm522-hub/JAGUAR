from aiogram import Router
from aiogram import F
from aiogram.types import Message

from keyboards.user.menu import main_menu

router = Router()


@router.message(F.text == "🏠 Home")
async def home(message: Message):

    await message.answer(
        "🏠 <b>Main Menu</b>",
        reply_markup=main_menu
    )
