import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from bot.config import BOT_TOKEN

# Routers
from handlers.start import router as start_router
from handlers.menu import router as menu_router


async def main():

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    # Register Routers
    dp.include_router(start_router)
    dp.include_router(menu_router)

    print("🐆 Jaguar Bot Started Successfully!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
