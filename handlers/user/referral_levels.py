from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "📈 Referral Levels")
async def referral_levels(message: Message):

    await message.answer(
"""
📈 <b>Referral Levels</b>

🌱 Beginner
0 - 4 Referrals

🥉 Bronze
5 - 19 Referrals

🥈 Silver
20 - 49 Referrals

🥇 Gold
50 - 99 Referrals

💎 Diamond
100 - 249 Referrals

👑 Elite
250+ Referrals
"""
    )
