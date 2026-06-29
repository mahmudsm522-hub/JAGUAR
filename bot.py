"""
=====================================
🐆 Jaguar Telegram Bot
Version : v0.1
=====================================
"""

import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import BOT_TOKEN


# ==========================
# Create Bot & Dispatcher
# ==========================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# ==========================
# Start Command
# ==========================

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🐆 Welcome to Jaguar!\n\n"
        "Jaguar is starting successfully."
    )


# ==========================
# Main Function
# ==========================

async def main():
    print("🐆 Jaguar Bot is Running...")
    await dp.start_polling(bot)


# ==========================
# Run Bot
# ==========================

if __name__ == "__main__":
    asyncio.run(main())
