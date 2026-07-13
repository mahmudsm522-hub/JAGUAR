import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from bot.config import BOT_TOKEN

# Routers
from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.user.daily import router as daily_router
from handlers.user.profile import router as profile_router
from handlers.admin.tasks import router as admin_tasks_router
from handlers.admin.withdraw import router as withdraw_router
from handlers.admin.broadcast import router as broadcast_router
from handlers.admin.statistics import router as statistics_router
from handlers.user.leaderboard import router as leaderboard_router
from handlers.user.withdraw_history import router as withdraw_history_router
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
    dp.include_router(daily_router)
    dp.include_router(profile_router)
    dp.include_router(admin_tasks_router)
    dp.include_router(withdraw_router)
    dp.include_router(broadcast_router)
    dp.include_router(statistics_router)
    dp.include_router(leaderboard_router)
    dp.include_router(withdraw_history_router)
    print("🐆 Jaguar Bot Started Successfully!")
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
