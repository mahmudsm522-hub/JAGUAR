import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# Main channel (required before using the bot)
MAIN_CHANNEL_ID = int(os.getenv("MAIN_CHANNEL_ID", "0"))
MAIN_CHANNEL_USERNAME = os.getenv("MAIN_CHANNEL_USERNAME")
MAIN_CHANNEL_LINK = os.getenv("MAIN_CHANNEL_LINK")

# Wallet channel (required before withdrawal)
WALLET_CHANNEL_ID = int(os.getenv("WALLET_CHANNEL_ID", "0"))
WALLET_CHANNEL_USERNAME = os.getenv("WALLET_CHANNEL_USERNAME")
WALLET_CHANNEL_LINK = os.getenv("WALLET_CHANNEL_LINK")
