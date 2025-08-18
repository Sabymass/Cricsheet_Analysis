import sqlite3

# Connect to your SQLite database
DB_PATH = r"D:\Guvi Projects\cricsheet_project\New folder\scripts\cricsheet.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Optional: List all tables to confirm
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("✅ Existing tables before deletion:", tables)

# Drop only the 'matches' table
cursor.execute("DROP TABLE IF EXISTS matches")
conn.commit()

# Optional: List tables after deletion
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables_after = cursor.fetchall()
print("✅ Tables after deletion:", tables_after)

conn.close()
print("✅ 'matches' table deleted successfully!")
