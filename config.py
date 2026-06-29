import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Admin
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# Required Channel
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "0"))
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
CHANNEL_LINK = os.getenv("CHANNEL_LINK")
