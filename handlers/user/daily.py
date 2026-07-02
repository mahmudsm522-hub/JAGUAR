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
    now = datetime.now()

    daily = get_daily(user_id)

    if daily is None:
        streak = 1

    else:
        try:
            last_claim = datetime.strptime(
                daily[0],
                "%Y-%m-%d %H:%M:%S"
            )

            streak = daily[1]

            # Already claimed today
            if last_claim.date() == now.date():
                await message.answer(
                    "⏳ You have already claimed today's reward.\n\n"
                    "Please come back tomorrow."
                )
                return

            # Continue streak
            if (now.date() - last_claim.date()).days == 1:
                streak += 1
                if streak > 7:
                    streak = 1
            else:
                streak = 1

        except Exception:
            streak = 1

    reward = REWARDS[streak]

    # Save daily reward
    save_daily(
        user_id,
        now.strftime("%Y-%m-%d %H:%M:%S"),
        streak
    )

    # Add reward
    add_balance(user_id, reward)

    # Save transaction
    add_transaction(
        user_id=user_id,
        tx_type="daily_reward",
        amount=reward,
        description=f"Daily Reward - Day {streak}",
        date=now.strftime("%Y-%m-%d %H:%M:%S")
    )

    balance = get_balance(user_id)

    await message.answer(
        f"""
🎉 <b>Daily Reward Claimed!</b>

🪙 Reward: <b>+{reward} JGR</b>

🔥 Streak: <b>Day {streak}/7</b>

💰 Balance: <b>{balance} JGR</b>

Come back tomorrow for a bigger reward!
"""
                )
