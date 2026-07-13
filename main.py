from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from aiogram.types import Update

from bot import bot, dp
from config import BOT_TOKEN


WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = f"https://YOUR-RENDER-URL.onrender.com{WEBHOOK_PATH}"


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Startup
    await bot.set_webhook(
        url=WEBHOOK_URL,
        drop_pending_updates=True
    )

    print("✅ Webhook Connected")

    yield

    # Shutdown
    await bot.delete_webhook()
    await bot.session.close()

    print("🛑 Bot Stopped")


app = FastAPI(
    title="Jaguar Bot",
    lifespan=lifespan
)


@app.get("/")
async def home():

    return {
        "status": "running",
        "bot": "Jaguar",
        "version": "1.0 Stable"
    }


@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):

    update = Update.model_validate(
        await request.json(),
        context={"bot": bot}
    )

    await dp.feed_update(
        bot,
        update
    )

    return {
        "ok": True
}
