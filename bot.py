import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN

# ==========================
# USER ROUTERS
# ==========================

from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.user.profile import router as profile_router
from handlers.user.daily import router as daily_router
from handlers.user.tasks import router as tasks_router
from handlers.user.wallet import router as wallet_router
from handlers.user.withdraw_history import router as withdraw_history_router
from handlers.user.leaderboard import router as leaderboard_router
from handlers.user.referral_levels import router as referral_levels_router

# ==========================
# ADMIN ROUTERS
# ==========================

from handlers.admin.tasks import router as admin_tasks_router
from handlers.admin.withdraw import router as withdraw_router
from handlers.admin.broadcast import router as broadcast_router
from handlers.admin.statistics import router as statistics_router
from handlers.admin.premium import router as premium_router


async def main():

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    # ==========================
    # USER
    # ==========================

    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(profile_router)
    dp.include_router(daily_router)
    dp.include_router(tasks_router)
    dp.include_router(wallet_router)
    dp.include_router(withdraw_history_router)
    dp.include_router(leaderboard_router)
    dp.include_router(referral_levels_router)

    # ==========================
    # ADMIN
    # ==========================

    dp.include_router(admin_tasks_router)
    dp.include_router(withdraw_router)
    dp.include_router(broadcast_router)
    dp.include_router(statistics_router)
    dp.include_router(premium_router)

    print("=" * 40)
    print("🐆 Jaguar Bot Started Successfully")
    print("=" * 40)

    try:
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
