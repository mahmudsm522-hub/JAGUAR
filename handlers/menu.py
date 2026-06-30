from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text == "🪙 Earn JGR")
async def earn_jgr(message: Message):
    await message.answer(
        "💰 Earn more JGR by completing Tasks and inviting friends."
    )


@router.message(F.text == "🎁 Daily Reward")
async def daily_reward(message: Message):
    await message.answer(
        "🎁 Daily Reward system is under development."
    )


@router.message(F.text == "📋 Tasks")
async def tasks(message: Message):
    await message.answer(
        "📋 Tasks will appear here soon."
    )


@router.message(F.text == "👥 Invite")
async def invite(message: Message):
    await message.answer(
        f"👥 Invite your friends:\n\n"
        f"https://t.me/YOUR_BOT_USERNAME?start={message.from_user.id}"
    )


@router.message(F.text == "👛 Wallet")
async def wallet(message: Message):
    await message.answer(
        "👛 Wallet system coming soon."
    )


@router.message(F.text == "👤 Profile")
async def profile(message: Message):
    await message.answer(
        "👤 Profile system coming soon."
               )
