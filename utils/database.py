returnqlite3
from pathlib import Path

# Create data folder if it doesn't exist
Path("data").mkdir(exist_ok=True)

# Connect database
conn = sqlite3.connect("data/jaguar.db", check_same_thread=False)
cursor = conn.cursor()


def init_database():
    # Users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        balance INTEGER DEFAULT 500,
        referrals INTEGER DEFAULT 0,
        joined_date TEXT,
        last_daily TEXT,
        wallet_verified INTEGER DEFAULT 0,
        banned INTEGER DEFAULT 0,
        rank TEXT DEFAULT 'Beginner'
    )
    """)

    # Tasks
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        type TEXT,
        link TEXT,
        reward INTEGER,
        status INTEGER DEFAULT 1
    )
    """)

    # Completed Tasks
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS completed_tasks(
        user_id INTEGER,
        task_id INTEGER,
        completed_at TEXT
    )
    """)

    # Referrals
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS referrals(
        referrer_id INTEGER,
        new_user_id INTEGER,
        reward INTEGER,
        date TEXT
    )
    """)

    # Withdraws
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS withdraws(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        wallet TEXT,
        amount INTEGER,
        status TEXT,
        date TEXT
    )
    """)

    # Settings
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS settings(
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)

    # Transactions
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

    conn.commit()
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
from datetime import datetime


# ==========================
# CREATE USER
# ==========================
def create_user(user_id, username, first_name):

    cursor.execute(
        "SELECT user_id FROM users WHERE user_id = ?",
        (user_id,)
    )

    user = cursor.fetchone()

    if user:
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
        VALUES(?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        username,
        first_name,
        100,   # Welcome Bonus
        0,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    db.commit()

    return True


# ==========================
# GET USER
# ==========================
def get_user(user_id):

    cursor.execute(
        "SELECT * FROM users WHERE user_id=?",
        (user_id,)
    )

    return cursor.fetchone()


# ==========================
# GET BALANCE
# ==========================
def get_balance(user_id):

    cursor.execute(
        "SELECT balance FROM users WHERE user_id=?",
        (user_id,)
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return 0
init_database()
from datetime import datetime


def get_daily(user_id):
    cursor.execute(
        "SELECT last_claim, streak FROM daily_rewards WHERE user_id=?",
        (user_id,)
    )
    return cursor.fetchone()


def save_daily(user_id, last_claim, streak):

    cursor.execute(
        "SELECT user_id FROM daily_rewards WHERE user_id=?",
        (user_id,)
    )

    if cursor.fetchone():

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
def add_balance(user_id, amount):

    cursor.execute("""
    UPDATE users
    SET balance = balance + ?
    WHERE user_id = ?
    """, (
        amount,
        user_id
    ))

    conn.commit()


def get_balance(user_id):

    cursor.execute("""
    SELECT balance
    FROM users
    WHERE user_id=?
    """, (
        user_id,
    ))

    result = cursor.fetchone()

    if result:
        return result[0]

    return 0
def add_transaction(
    user_id,
    tx_type,
    amount,
    description,
    date
):

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

    conn.commit()0
