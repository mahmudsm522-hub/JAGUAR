from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import ADMIN_ID

from utils.database import (
    get_total_users,
    get_total_tasks,
    get_withdraw_count,
    get_total_withdraw_amount,
    get_premium_users,
    get_total_referrals,
    get_today_users,
    get_total_balance
)

router = Router()


@router.message(Command("stats"))
async def statistics(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    users = get_total_users()
    tasks = get_total_tasks()

    pending = get_withdraw_count("pending")
    approved = get_withdraw_count("approved")
    rejected = get_withdraw_count("rejected")

    withdrawn = get_total_withdraw_amount()

    premium = get_premium_users()

    referrals = get_total_referrals()

    today = get_today_users()

    balance = get_total_balance()

    await message.answer(

f"""
📊 <b>JAGUAR STATISTICS</b>

━━━━━━━━━━━━━━

👥 Users
<b>{users}</b>

📅 New Today
<b>{today}</b>

📝 Active Tasks
<b>{tasks}</b>

━━━━━━━━━━━━━━

💰 Total User Balance

<b>{balance:,} JGR</b>

━━━━━━━━━━━━━━

👥 Referrals

<b>{referrals}</b>

━━━━━━━━━━━━━━

💸 Pending Withdraw

<b>{pending}</b>

✅ Approved Withdraw

<b>{approved}</b>

❌ Rejected Withdraw

<b>{rejected}</b>

━━━━━━━━━━━━━━

🏦 Total Withdraw

<b>{withdrawn:,} JGR</b>

━━━━━━━━━━━━━━

👑 Premium Users

<b>{premium}</b>

━━━━━━━━━━━━━━

🐆 Jaguar v1.0
"""

)
