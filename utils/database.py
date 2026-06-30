import sqlite3

db = sqlite3.connect("data/jaguar.db", check_same_thread=False)
cursor = db.cursor()

# ==========================
# USERS
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    balance INTEGER DEFAULT 0,
    referrals INTEGER DEFAULT 0,
    joined_date TEXT,
    last_daily TEXT,
    wallet_verified INTEGER DEFAULT 0,
    banned INTEGER DEFAULT 0
)
""")

# ==========================
# TASKS
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    task_type TEXT,
    link TEXT,
    reward INTEGER,
    status INTEGER DEFAULT 1
)
""")

# ==========================
# COMPLETED TASKS
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS completed_tasks(
    user_id INTEGER,
    task_id INTEGER,
    completed_at TEXT
)
""")

# ==========================
# WITHDRAWS
# ==========================
cursor.execute("""
CREATE TABLE IF NOT EXISTS withdraws(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    wallet_address TEXT,
    amount INTEGER,
    status TEXT
)
""")

db.commit()
