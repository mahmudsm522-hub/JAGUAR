from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🪙 Earn JGR"),
            KeyboardButton(text="🎁 Daily Reward")
        ],
        [
            KeyboardButton(text="📋 Tasks"),
            KeyboardButton(text="👥 Invite")
        ],
        [
            KeyboardButton(text="👛 Wallet"),
            KeyboardButton(text="👤 Profile")
        ]
    ],
    resize_keyboard=True
)
