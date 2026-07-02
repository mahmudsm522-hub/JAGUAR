from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

withdraw_id = create_withdraw(
    user_id=message.from_user.id,
    wallet_type=data["wallet_type"],
    wallet_address=data["wallet_address"],
    amount=amount
)
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
withdraw_type_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🟡 Binance UID",
                callback_data="wallet_binance"
            )
        ],
        [
            InlineKeyboardButton(
                text="🟢 USDT (TRC20)",
                callback_data="wallet_trc20"
            )
        ],
        [
            InlineKeyboardButton(
                text="🟠 USDT (BEP20)",
                callback_data="wallet_bep20"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔵 TON Wallet",
                callback_data="wallet_ton"
            )
        ]
    ]
)
