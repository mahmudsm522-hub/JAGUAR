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
# ==========================
# DAILY REWARD
# ==========================

def get_daily(user_id):

    cursor.execute("""
    SELECT last_claim, streak
    FROM daily_rewards
    WHERE user_id=?
    """, (user_id,))

    return cursor.fetchone()


def save_daily(user_id, last_claim, streak):

    if get_daily(user_id):

        cursor.execute("""
        UPDATE daily_rewards
        SET last_claim=?,
            streak=?
        WHERE user_id=?
        """, (
            last_claim,
            streak,
            user_id
        ))

    else:

        cursor.execute("""
        INSERT INTO daily_rewards(
            user_id,
            last_claim,
            streak
        )
        VALUES(?,?,?)
        """, (
            user_id,
            last_claim,
            streak
        ))

    conn.commit()


# ==========================
# TRANSACTIONS
# ==========================

def add_transaction(
    user_id,
    tx_type,
    amount,
    description,
    date=None
):

    if date is None:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO transactions(
        user_id,
        type,
        amount,
        description,
        date
    )
    VALUES(?,?,?,?,?)
    """, (
        user_id,
        tx_type,
        amount,
        description,
        date
    ))

    conn.commit()


def get_transactions(user_id, limit=20):

    cursor.execute("""
    SELECT *
    FROM transactions
    WHERE user_id=?
    ORDER BY id DESC
    LIMIT ?
    """, (
        user_id,
        limit
    ))

    return cursor.fetchall()


# ==========================
# PREMIUM
# ==========================

def is_premium(user_id):

    cursor.execute("""
    SELECT premium
    FROM users
    WHERE user_id=?
    """, (user_id,))

    result = cursor.fetchone()

    if result:
        return bool(result["premium"])

    return False


def set_premium(user_id, status):

    cursor.execute("""
    UPDATE users
    SET premium=?
    WHERE user_id=?
    """, (
        int(status),
        user_id
    ))

    conn.commit()


# ==========================
# BAN / UNBAN
# ==========================

def ban_user(user_id):

    cursor.execute("""
    UPDATE users
    SET banned=1
    WHERE user_id=?
    """, (user_id,))

    conn.commit()


def unban_user(user_id):

    cursor.execute("""
    UPDATE users
    SET banned=0
    WHERE user_id=?
    """, (user_id,))

    conn.commit()


def is_banned(user_id):

    cursor.execute("""
    SELECT banned
    FROM users
    WHERE user_id=?
    """, (user_id,))

    result = cursor.fetchone()

    if result:
        return bool(result["banned"])

    return False
# ==========================
# TASKS
# ==========================

def add_task(title, task_type, link, reward):

    cursor.execute("""
    INSERT INTO tasks(
        title,
        task_type,
        link,
        reward,
        status,
        created_at
    )
    VALUES(?,?,?,?,?,?)
    """, (
        title,
        task_type,
        link,
        reward,
        1,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()

    return cursor.lastrowid


def get_active_tasks():

    cursor.execute("""
    SELECT *
    FROM tasks
    WHERE status=1
    ORDER BY id DESC
    """)

    return cursor.fetchall()


def get_task(task_id):

    cursor.execute("""
    SELECT *
    FROM tasks
    WHERE id=?
    """, (task_id,))

    return cursor.fetchone()


def delete_task(task_id):

    cursor.execute("""
    DELETE FROM tasks
    WHERE id=?
    """, (task_id,))

    conn.commit()


def disable_task(task_id):

    cursor.execute("""
    UPDATE tasks
    SET status=0
    WHERE id=?
    """, (task_id,))

    conn.commit()


def enable_task(task_id):

    cursor.execute("""
    UPDATE tasks
    SET status=1
    WHERE id=?
    """, (task_id,))

    conn.commit()


# ==========================
# COMPLETED TASKS
# ==========================

def is_task_completed(user_id, task_id):

    cursor.execute("""
    SELECT id
    FROM completed_tasks
    WHERE user_id=? AND task_id=?
    """, (
        user_id,
        task_id
    ))

    return cursor.fetchone() is not None


def complete_task(user_id, task_id):

    if is_task_completed(user_id, task_id):
        return False

    cursor.execute("""
    INSERT INTO completed_tasks(
        user_id,
        task_id,
        completed_at
    )
    VALUES(?,?,?)
    """, (
        user_id,
        task_id,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()

    return True


def get_completed_tasks(user_id):

    cursor.execute("""
    SELECT task_id
    FROM completed_tasks
    WHERE user_id=?
    """, (user_id,))

    return cursor.fetchall()
# ==========================
# WITHDRAW SYSTEM
# ==========================

def create_withdraw(
    user_id,
    wallet_type,
    wallet_address,
    amount
):

    cursor.execute("""
    INSERT INTO withdraws(
        user_id,
        wallet_type,
        wallet_address,
        amount,
        status,
        created_at
    )
    VALUES(?,?,?,?,?,?)
    """, (
        user_id,
        wallet_type,
        wallet_address,
        amount,
        "pending",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()

    return cursor.lastrowid


def get_withdraw(withdraw_id):

    cursor.execute("""
    SELECT *
    FROM withdraws
    WHERE id=?
    """, (withdraw_id,))

    return cursor.fetchone()


def get_user_withdraws(user_id):

    cursor.execute("""
    SELECT *
    FROM withdraws
    WHERE user_id=?
    ORDER BY id DESC
    """, (user_id,))

    return cursor.fetchall()


def get_pending_withdraws():

    cursor.execute("""
    SELECT *
    FROM withdraws
    WHERE status='pending'
    ORDER BY id ASC
    """)

    return cursor.fetchall()


def approve_withdraw(
    withdraw_id,
    admin_id
):

    cursor.execute("""
    UPDATE withdraws
    SET
        status='approved',
        approved_at=?,
        approved_by=?
    WHERE id=?
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        admin_id,
        withdraw_id
    ))

    conn.commit()


def reject_withdraw(
    withdraw_id,
    admin_id
):

    cursor.execute("""
    UPDATE withdraws
    SET
        status='rejected',
        approved_at=?,
        approved_by=?
    WHERE id=?
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        admin_id,
        withdraw_id
    ))

    conn.commit()


def get_withdraw_count(status):

    cursor.execute("""
    SELECT COUNT(*)
    FROM withdraws
    WHERE status=?
    """, (status,))

    return cursor.fetchone()[0]


def get_total_withdraw_amount():

    cursor.execute("""
    SELECT COALESCE(SUM(amount),0)
    FROM withdraws
    WHERE status='approved'
    """)

    return cursor.fetchone()[0]
