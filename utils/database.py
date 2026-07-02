returnqlite3
from pathlib import Path
from datetime import datetime
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
from datetime import datetime

def create_withdraw(user_id, wallet_type, wallet_address, amount):
    cursor.execute("""
        INSERT INTO withdraws
        (user_id, wallet_type, wallet_address, amount, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
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
def get_user(user_id):

    cursor.execute(
        "SELECT * FROM users WHERE user_id=?",
        (user_id,)
    )

    return cursor.fetchone()
def get_active_tasks():

    cursor.execute("""
    SELECT *
    FROM tasks
    WHERE status=1
    ORDER BY id ASC
    """)

    return cursor.fetchall()
def add_task(title, task_type, link, reward):

    cursor.execute(
        """
        INSERT INTO tasks
        (title, type, link, reward)
        VALUES (?, ?, ?, ?)
        """,
        (
            title,
            task_type,
            link,
            reward
        )
    )

    conn.commit()
def get_task(task_id):
    cursor.execute(
        "SELECT * FROM tasks WHERE id=? AND status=1",
        (task_id,)
    )
    return cursor.fetchone()


def is_task_completed(user_id, task_id):
    cursor.execute(
        """
        SELECT 1 FROM completed_tasks
        WHERE user_id=? AND task_id=?
        """,
        (user_id, task_id)
    )
    return cursor.fetchone() is not None


def complete_task(user_id, task_id):
    from datetime import datetime

    cursor.execute(
        """
        INSERT INTO completed_tasks(
            user_id,
            task_id,
            completed_at
        )
        VALUES(?,?,?)
        """,
        (
            user_id,
            task_id,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conn.commit()

def create_withdraw(user_id, wallet_address, amount):
    cursor.execute("""
        INSERT INTO withdraws
        (user_id, wallet_address, amount, status, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        user_id,
        wallet_address,
        amount,
        "pending",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))
    conn.commit()


def get_pending_withdraws():
    cursor.execute("""
        SELECT * FROM withdraws
        WHERE status='pending'
        ORDER BY id DESC
    """)
    return cursor.fetchall()


def update_withdraw_status(withdraw_id, status):
    cursor.execute("""
        UPDATE withdraws
        SET status=?
        WHERE id=?
    """, (status, withdraw_id))
    conn.commit()
def update_withdraw_status(withdraw_id, status):
    cursor.execute(
        """
        UPDATE withdraws
        SET status=?
        WHERE id=?
        """,
        (status, withdraw_id)
    )
    conn.commit()
def get_withdraw(withdraw_id):
    cursor.execute(
        "SELECT * FROM withdraws WHERE id=?",
        (withdraw_id,)
    )
    return cursor.fetchone()
