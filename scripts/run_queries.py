import sqlite3
import pandas as pd

DB_FILE = r"D:\Guvi Projects\cricsheet_project\New folder\scripts\cricsheet.db"
SQL_FILE = r"D:\Guvi Projects\cricsheet_project\New folder\scripts\queries.sql"
OUTPUT_FILE = r"D:\Guvi Projects\cricsheet_project\New folder\all_queries_results.xlsx"

# Connect to database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Read all queries from file
with open(SQL_FILE, "r") as f:
    sql_content = f.read()

# Split queries by semicolon
queries = [q.strip() for q in sql_content.split(";") if q.strip()]

# Create a Pandas Excel writer
with pd.ExcelWriter(OUTPUT_FILE) as writer:
    for idx, query in enumerate(queries, 1):
        try:
            df = pd.read_sql_query(query, conn)
            # Save each query result in a separate sheet
            sheet_name = f"Query_{idx}"
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"✅ Query {idx} executed successfully.")
        except Exception as e:
            print(f"❌ Query {idx} failed: {e}")

conn.close()
print(f"All query results saved in {OUTPUT_FILE}")
