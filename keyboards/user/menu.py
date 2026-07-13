from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="👤 Profile"),
            KeyboardButton(text="🎁 Daily Reward")
        ],
        [
            KeyboardButton(text="📋 Tasks"),
            KeyboardButton(text="💼 Wallet")
        ],
        [
            KeyboardButton(text="🏆 Leaderboard"),
            KeyboardButton(text="📈 Referral Levels")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Choose an option..."
)
