import os
from dotenv import load_dotenv

# ==========================
# LOAD ENV
# ==========================

load_dotenv()

# ==========================
# BOT
# ==========================

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN is missing in .env")

# ==========================
# ADMIN
# ==========================

ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# ==========================
# MAIN CHANNEL
# ==========================

MAIN_CHANNEL_ID = int(
    os.getenv("MAIN_CHANNEL_ID", "0")
)

MAIN_CHANNEL_USERNAME = os.getenv(
    "MAIN_CHANNEL_USERNAME",
    ""
)

MAIN_CHANNEL_LINK = os.getenv(
    "MAIN_CHANNEL_LINK",
    ""
)

# ==========================
# WALLET CHANNEL
# ==========================

WALLET_CHANNEL_ID = int(
    os.getenv("WALLET_CHANNEL_ID", "0")
)

WALLET_CHANNEL_USERNAME = os.getenv(
    "WALLET_CHANNEL_USERNAME",
    ""
)

WALLET_CHANNEL_LINK = os.getenv(
    "WALLET_CHANNEL_LINK",
    ""
)

# ==========================
# WITHDRAW
# ==========================

MIN_WITHDRAW = int(
    os.getenv("MIN_WITHDRAW", "10000")
)

# ==========================
# WELCOME BONUS
# ==========================

WELCOME_BONUS = int(
    os.getenv("WELCOME_BONUS", "100")
)

# ==========================
# REFERRAL BONUS
# ==========================

REFERRAL_BONUS = int(
    os.getenv("REFERRAL_BONUS", "500")
)

# ==========================
# DAILY REWARD
# ==========================

DAY1_REWARD = 250
DAY2_REWARD = 300
DAY3_REWARD = 350
DAY4_REWARD = 400
DAY5_REWARD = 450
DAY6_REWARD = 500
DAY7_REWARD = 1000

# ==========================
# PREMIUM
# ==========================

PREMIUM_DAILY_BONUS = 25      # %
PREMIUM_TASK_BONUS = 20       # %

# ==========================
# BOT INFO
# ==========================

BOT_NAME = "Jaguar Bot"
BOT_VERSION = "1.0 Stable"
BOT_CURRENCY = "JGR"
