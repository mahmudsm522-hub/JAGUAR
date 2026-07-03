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
# ----------------------
    # WITHDRAWS
    # ----------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS withdraws(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        wallet_type TEXT,
        wallet_address TEXT,
        amount INTEGER,
        status TEXT DEFAULT 'pending',
        created_at TEXT,
        approved_at TEXT,
        approved_by INTEGER
    )
    """)

    # ----------------------
    # TRANSACTIONS
    # ----------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        type TEXT,
        amount INTEGER,
        description TEXT,
        date TEXT
    )
    """)

    # ----------------------
    # SETTINGS
    # ----------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS settings(
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)

    # ----------------------
    # PREMIUM LOGS
    # ----------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS premium_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        admin_id INTEGER,
        duration INTEGER,
        created_at TEXT
    )
    """)

    conn.commit()


# Initialize database
init_database()
# ==========================
# USERS
# ==========================

def user_exists(user_id):
    cursor.execute(
        "SELECT 1 FROM users WHERE user_id=?",
        (user_id,)
    )
    return cursor.fetchone() is not None


def create_user(user_id, username, first_name):

    if user_exists(user_id):
        return False

    cursor.execute("""
    INSERT INTO users(
        user_id,
        username,
        first_name,
        balance,
        referrals,
        joined_date
    )
    VALUES(?,?,?,?,?,?)
    """, (
        user_id,
        username,
        first_name,
        100,
        0,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()

    return True


def get_user(user_id):

    cursor.execute(
        "SELECT * FROM users WHERE user_id=?",
        (user_id,)
    )

    return cursor.fetchone()


def get_all_users():

    cursor.execute(
        "SELECT user_id FROM users"
    )

    return cursor.fetchall()


def get_balance(user_id):

    cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )

    result = cursor.fetchone()

    if result:
        return result["balance"]

    return 0


def add_balance(user_id, amount):

    cursor.execute("""
    UPDATE users
    SET balance = balance + ?
    WHERE user_id=?
    """, (
        amount,
        user_id
    ))

    conn.commit()


def remove_balance(user_id, amount):

    cursor.execute("""
    UPDATE users
    SET balance = balance - ?
    WHERE user_id=?
    """, (
        amount,
        user_id
    ))

    conn.commit()


def update_balance(user_id, balance):

    cursor.execute("""
    UPDATE users
    SET balance=?
    WHERE user_id=?
    """, (
        balance,
        user_id
    ))

    conn.commit()


def add_referral(user_id):

    cursor.execute("""
    UPDATE users
    SET referrals = referrals + 1
    WHERE user_id=?
    """, (
        user_id,
    ))

    conn.commit()


def get_referrals(user_id):

    cursor.execute(
        "SELECT referrals FROM users WHERE user_id=?",
        (user_id,)
    )

    result = cursor.fetchone()

    if result:
        return result["referrals"]

    return 0
