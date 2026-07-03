import sqlite3

conn = sqlite3.connect("data/jaguar.db")
cursor = conn.cursor()


def add_column(table, column, column_type):

    try:

        cursor.execute(
            f"""
            ALTER TABLE {table}
            ADD COLUMN {column} {column_type}
            """
        )

        print(f"✅ Added: {table}.{column}")

    except sqlite3.OperationalError:

        print(f"✔ Already Exists: {table}.{column}")


# USERS
add_column("users", "premium", "INTEGER DEFAULT 0")
add_column("users", "premium_expire", "TEXT")
add_column("users", "rank", "TEXT DEFAULT 'Beginner'")

# WITHDRAWS
add_column("withdraws", "wallet_type", "TEXT")
add_column("withdraws", "created_at", "TEXT")
add_column("withdraws", "approved_at", "TEXT")
add_column("withdraws", "approved_by", "INTEGER")

conn.commit()

print("🎉 Migration Completed")
