from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from aiogram.types import Update

from bot import bot, dp
from config import BOT_TOKEN, RENDER_URL


WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = f"{RENDER_URL}{WEBHOOK_PATH}"


@asynccontextmanager
async def lifespan(app: FastAPI):

    await bot.set_webhook(
        WEBHOOK_URL,
        drop_pending_updates=True
    )

    print("✅ Webhook Connected")

    yield

    await bot.delete_webhook()
    await bot.session.close()

    print("🛑 Jaguar Bot Stopped")


app = FastAPI(
    title="Jaguar Bot",
    version="1.0",
    lifespan=lifespan
)


@app.get("/")
async def home():

    return {
        "status": "online",
        "bot": "Jaguar",
        "version": "1.0 Stable"
    }


@app.post(WEBHOOK_PATH)
async def webhook(request: Request):

    update = Update.model_validate(
        await request.json(),
        context={"bot": bot}
    )

    await dp.feed_update(bot, update)

    return {"ok": True}
