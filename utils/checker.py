from aiogram.exceptions import TelegramBadRequest
from bot.config import CHANNEL_ID
from utils.database import cursor


async def is_joined(bot, user_id):
    """
    Check if user joined the main channel.
    """
    try:
        member = await bot.get_chat_member(CHANNEL_ID, user_id)

        if member.status in (
            "member",
            "administrator",
            "creator"
        ):
            return True

    except TelegramBadRequest:
        pass

    return False


def is_banned(user_id):
    """
    Returns True if user is banned.
    """

    cursor.execute(
        "SELECT banned FROM users WHERE user_id=?",
        (user_id,)
    )

    result = cursor.fetchone()

    if result:
        return result[0] == 1

    return False


def is_admin(user_id):
    """
    Check if user is bot admin.
    """

    from bot.config import ADMINS

    return user_id in ADMINS
async def check_membership(bot, chat_id, user_id):
    try:
        member = await bot.get_chat_member(chat_id, user_id)

        return member.status in (
            "member",
            "administrator",
            "creator"
        )

    except Exception:
        return False
