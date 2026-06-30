from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config import CHANNEL_LINK


join_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 Join Channel",
                url=CHANNEL_LINK
            )
        ],
        [
            InlineKeyboardButton(
                text="✅ Verify",
                callback_data="verify_join"
            )
        ]
    ]
)
