import sqlite3
import os

def check_db(path):
    print(f"Checking database at: {path}")
    if not os.path.exists(path):
        print("  - File does not exist.")
        return

    try:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(product)")
        columns = [info[1] for info in cursor.fetchall()]
        print(f"  - Columns in 'product' table: {columns}")
        if 'description' in columns:
            print("  - 'description' column EXISTS.")
        else:
            print("  - 'description' column MISSING.")
        conn.close()
    except Exception as e:
        print(f"  - Error reading database: {e}")

if __name__ == "__main__":
    # Check instance/app.db
    check_db(os.path.join("instance", "app.db"))
    # Check app.db in root
    check_db("app.db")
