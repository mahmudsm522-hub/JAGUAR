from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.startswith("approve_"))
async def approve(callback: CallbackQuery):

    await callback.message.edit_text(
        callback.message.text + "\n\n✅ APPROVED"
    )

    await callback.bot.send_message(
        int(callback.data.split("_")[1]),
        "🎉 Your withdrawal has been approved."
    )

    await callback.answer()


@router.callback_query(F.data.startswith("reject_"))
async def reject(callback: CallbackQuery):

    await callback.message.edit_text(
        callback.message.text + "\n\n❌ REJECTED"
    )

    await callback.bot.send_message(
        int(callback.data.split("_")[1]),
        "❌ Your withdrawal has been rejected."
    )

    await callback.answer()
