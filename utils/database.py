import sqlite3
from pathlib import Path
from datetime import datetime

# ==========================
# DATABASE
# ==========================

Path("data").mkdir(exist_ok=True)

conn = sqlite3.connect(
    "data/jaguar.db",
    check_same_thread=False
)

conn.row_factory = sqlite3.Row

cursor = conn.cursor()


# ==========================
# INIT DATABASE
# ==========================

def init_database():

    # ----------------------
    # USERS
    # ----------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        balance INTEGER DEFAULT 100,
        referrals INTEGER DEFAULT 0,
        joined_date TEXT,
        last_daily TEXT,
        wallet_verified INTEGER DEFAULT 0,
        banned INTEGER DEFAULT 0,
        premium INTEGER DEFAULT 0,
        premium_expire TEXT,
        rank TEXT DEFAULT 'Beginner'
    )
    """)

    # ----------------------
    # DAILY REWARDS
    # ----------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_rewards(
        user_id INTEGER PRIMARY KEY,
        last_claim TEXT,
        streak INTEGER DEFAULT 1
    )
    """)

    # ----------------------
    # TASKS
    # ----------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        task_type TEXT NOT NULL,
        link TEXT NOT NULL,
        reward INTEGER NOT NULL,
        status INTEGER DEFAULT 1,
        created_at TEXT
    )
    """)

    # ----------------------
    # COMPLETED TASKS
    # ----------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS completed_tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        task_id INTEGER,
        completed_at TEXT
    )
    """)

    # ----------------------
    # REFERRALS
    # ----------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS referrals(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        referrer_id INTEGER,
        new_user_id INTEGER,
        reward INTEGER,
        date TEXT
    )
    """)
