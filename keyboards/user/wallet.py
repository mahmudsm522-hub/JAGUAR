from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

wallet_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="💸 Withdraw",
                callback_data="withdraw"
            )
        ],
        [
            InlineKeyboardButton(
                text="📜 Withdraw History",
                callback_data="withdraw_history"
            )
        ]
    ]
)
