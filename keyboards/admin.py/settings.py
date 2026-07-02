keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Approve",
                callback_data=f"approve_{withdraw_id}"
            ),
            InlineKeyboardButton(
                text="❌ Reject",
                callback_data=f"reject_{withdraw_id}"
            )
        ]
    ]
)
