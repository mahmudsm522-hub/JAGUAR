from aiogram import Router, F
from aiogram.types import Message

from utils.database import get_user_withdraws

router = Router()


@router.message(F.text == "📜 Withdraw History")
async def withdraw_history(message: Message):

    withdraws = get_user_withdraws(
        message.from_user.id
    )

    if not withdraws:

        await message.answer(
            "📭 You don't have any withdrawal history."
        )
        return

    text = "📜 <b>Withdraw History</b>\n\n"

    for row in withdraws:

        status = row["status"]

        if status == "approved":
            icon = "✅"

        elif status == "pending":
            icon = "⏳"

        else:
            icon = "❌"

        text += (
            f"💰 <b>{row['amount']:,} JGR</b>\n"
            f"🏦 {row['wallet_type']}\n"
            f"📍 {row['wallet_address']}\n"
            f"{icon} {status.title()}\n"
            f"📅 {row['created_at']}\n"
            "━━━━━━━━━━━━━━\n\n"
        )

    await message.answer(text)
