from aiogram import Router, F
from aiogram.types import Message

from utils.database import (
    get_user,
    get_balance,
    get_daily
)

router = Router()


@router.message(F.text == "👤 Profile")
async def profile(message: Message):

    user_id = message.from_user.id

    user = get_user(user_id)

    if not user:
        await message.answer(
            "❌ User not found.\nPlease use /start first."
        )
        return

    balance = get_balance(user_id)

    daily = get_daily(user_id)

    streak = 0

    if daily:
        streak = daily[1]

    username = message.from_user.username

    if username:
        username = "@" + username
    else:
        username = "No Username"

    await message.answer(
        f"""
👤 <b>YOUR PROFILE</b>

━━━━━━━━━━━━━━

🆔 ID: <code>{user_id}</code>

👤 Username: {username}

🪙 Balance: <b>{balance} JGR</b>

🔥 Daily Streak: <b>{streak}/7</b>

🏅 Rank: Beginner

👥 Referrals: 0

━━━━━━━━━━━━━━

🐆 Jaguar v0.2 Alpha
"""
  )
