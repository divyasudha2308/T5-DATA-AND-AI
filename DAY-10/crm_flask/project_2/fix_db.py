import sqlite3
import os

# Path to the database
db_path = os.path.join("instance", "app.db")

def add_column():
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if column exists
        cursor.execute("PRAGMA table_info(product)")
        columns = [info[1] for info in cursor.fetchall()]
        
        if "description" not in columns:
            print("Adding 'description' column to 'product' table...")
            cursor.execute("ALTER TABLE product ADD COLUMN description TEXT")
            conn.commit()
            print("Column added successfully.")
        else:
            print("Column 'description' already exists.")
            
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    add_column()
