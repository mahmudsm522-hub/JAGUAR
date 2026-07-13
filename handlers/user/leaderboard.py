from aiogram import Router
from aiogram.types import Message
from aiogram import F

from utils.database import (
    get_top_balance,
    get_top_referrals
)

router = Router()


@router.message(F.text == "🏆 Leaderboard")
async def leaderboard(message: Message):

    balances = get_top_balance()
    referrals = get_top_referrals()

    text = "🏆 <b>JAGUAR LEADERBOARD</b>\n\n"

    text += "💰 <b>Top Balance</b>\n\n"

    medals = ["🥇", "🥈", "🥉"]

    for i, user in enumerate(balances):

        medal = medals[i] if i < 3 else f"{i+1}."

        username = user["username"] or user["first_name"] or "Unknown"

        text += (
            f"{medal} {username}\n"
            f"🪙 {user['balance']:,} JGR\n\n"
        )

    text += "━━━━━━━━━━━━━━\n\n"

    text += "👥 <b>Top Referrals</b>\n\n"

    for i, user in enumerate(referrals):

        medal = medals[i] if i < 3 else f"{i+1}."

        username = user["username"] or user["first_name"] or "Unknown"

        text += (
            f"{medal} {username}\n"
            f"👥 {user['referrals']} Referrals\n\n"
        )

    await message.answer(text)
