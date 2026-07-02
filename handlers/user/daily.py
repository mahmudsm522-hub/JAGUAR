from datetime import datetime, timedelta

from aiogram import Router, F
from aiogram.types import Message

from utils.database import (
    get_daily,
    save_daily,
    add_balance,
    get_balance,
    add_transaction
)

router = Router()

# Daily Reward Table
REWARDS = {
    1: 250,
    2: 300,
    3: 350,
    4: 400,
    5: 450,
    6: 500,
    7: 1000
}


@router.message(F.text == "🎁 Daily Reward")
async def daily_reward(message: Message):

    user_id = message.from_user.id

    today = datetime.now()

    daily = get_daily(user_id)

    # First Claim
    if daily is None:

        streak = 1
        reward = REWARDS[1]

    else:

        last_claim = datetime.strptime(
            daily[0],
            "%Y-%m-%d %H:%M:%S"
        )

        streak = daily[1]

        # Already claimed today
        if last_claim.date() == today.date():

            await message.answer(
                "⏳ You already claimed today's reward.\n\nCome back tomorrow."
            )
            return

        # Continue streak
        if today.date() == (last_claim + timedelta(days=1)).date():

            streak += 1

            if streak > 7:
                streak = 1

        else:
            streak = 1

        reward = REWARDS[streak]

    # Save Daily
    save_daily(
        user_id,
        today.strftime("%Y-%m-%d %H:%M:%S"),
        streak
    )

    # Add Balance
    add_balance(
        user_id,
        reward
    )

    # Save Transaction
    add_transaction(
        user_id,
        "daily_reward",
        reward,
        f"Day {streak} Daily Reward",
        today.strftime("%Y-%m-%d %H:%M:%S")
    )

    balance = get_balance(user_id)

    await message.answer(
        f"""
🎁 <b>Daily Reward Claimed!</b>

🪙 Reward: <b>+{reward} JGR</b>

🔥 Streak: <b>Day {streak}</b>

💰 Balance: <b>{balance} JGR</b>
"""
)
