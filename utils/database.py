import sqlite3

db = sqlite3.connect("data/jaguar.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    balance INTEGER DEFAULT 0,
    referrals INTEGER DEFAULT 0
)
""")

db.commit()
