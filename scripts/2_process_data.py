import sqlite3
import pandas as pd
import os

# --- Paths ---
DB_FILE = "cricsheet.db"
DATA_DIR = r"D:\Guvi Projects\cricsheet_project\New folder\data\processed"

# Match formats and corresponding CSV file names
FORMATS = {
    "odis": "odis_json",
    "t20s": "t20s_json",
    "tests": "tests_json"
}

def load_to_sql():
    # Connect to SQLite DB
    conn = sqlite3.connect(DB_FILE)

    for fmt, filename in FORMATS.items():
        csv_path = os.path.join(DATA_DIR, f"{filename}.csv")

        if not os.path.exists(csv_path):
            print(f"❌ CSV file not found: {csv_path}")
            continue

        # Load CSV
        df = pd.read_csv(csv_path)
        print(f"✅ Loaded {len(df)} rows from {filename}.csv")

        # Convert list-like/object columns to string
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].astype(str)

        # Save to SQL (table name = format)
        table_name = f"matches_{fmt}"
        df.to_sql(table_name, conn, if_exists="replace", index=False)

        # Verify row count
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cur.fetchone()[0]
        print(f"✅ Inserted {row_count} rows into table '{table_name}'")

    conn.close()
    print("🎉 All CSV files loaded successfully into DB")

if __name__ == "__main__":
    load_to_sql()
