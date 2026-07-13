from aiogram import Router, F
from aiogram.types import Message

from utils.database import (
    get_user,
    get_balance
)

router = Router()


def get_referral_level(referrals: int):

    if referrals >= 250:
        return "👑 Elite"

    elif referrals >= 100:
        return "💎 Diamond"

    elif referrals >= 50:
        return "🥇 Gold"

    elif referrals >= 20:
        return "🥈 Silver"

    elif referrals >= 5:
        return "🥉 Bronze"

    return "🌱 Beginner"


@router.message(F.text == "👤 Profile")
async def profile(message: Message):

    user = get_user(message.from_user.id)

    if not user:

        await message.answer(
            "❌ User not found."
        )
        return

    balance = get_balance(message.from_user.id)

    username = user["username"] or "No Username"
    first_name = user["first_name"]
    referrals = user["referrals"]
    joined = user["joined_date"]

    premium = "✅ Active" if user.get("premium", 0) else "❌ Not Active"

    level = get_referral_level(referrals)

    await message.answer(
        f"""
👤 <b>Your Profile</b>

━━━━━━━━━━━━━━

🆔 <b>ID:</b>
<code>{message.from_user.id}</code>

👤 <b>Name:</b>
{first_name}

📛 <b>Username:</b>
@{username}

💰 <b>Balance:</b>
{balance:,} JGR

👥 <b>Referrals:</b>
{referrals}

🏅 <b>Level:</b>
{level}

👑 <b>Premium:</b>
{premium}

📅 <b>Joined:</b>
{joined}

━━━━━━━━━━━━━━
"""
)
