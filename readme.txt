# 🏏 Cricsheet Match Data Analysis Project

This project is focused on analyzing cricket match data (ODIs, T20s, and Tests) from **Cricsheet**. 
It involves **data collection, processing, database management, exploratory data analysis (EDA), and SQL queries** to extract insights.

---

## 📂 Project Structure

```
data/
├── processed/              # Processed CSV files
│   ├── odis_matches.csv
│   ├── t20s_matches.csv
│   ├── tests_matches.csv
├── raw/                    # Raw JSON data files
│   ├── odis_json/
│   ├── t20s_json/
│   ├── tests_json/

scripts/
├── 1_download_data.py      # Script to download raw JSON data
├── 2_process_data.py       # Script to process JSON → CSV
├── 3_load_to_sql.py        # Load processed CSVs into SQLite DB
├── 4_eda.py                # Perform Exploratory Data Analysis (EDA)
├── drop_matches_table.py   # Utility script to drop/reset tables
├── queries.sql             # Contains 20 SQL queries for analysis
├── run_queries.py          # Executes queries & exports results to Excel
├── cricsheet.db            # SQLite database storing matches data

all_queries_results.xlsx     # Excel file with query results
requirements.txt             # Required Python dependencies
readme.txt                   # Documentation
```

---

## 🚀 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-link>
   cd <repo-folder>
   ```

2. **Create and activate virtual environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚡ Workflow

1. **Download Data**
   ```bash
   python scripts/1_download_data.py
   ```

2. **Process Data (JSON → CSV)**
   ```bash
   python scripts/2_process_data.py
   ```

3. **Load Data into SQLite**
   ```bash
   python scripts/3_load_to_sql.py
   ```

4. **Perform EDA**
   ```bash
   python scripts/4_eda.py
   ```

5. **Run SQL Queries**
   ```bash
   python scripts/run_queries.py
   ```

---

## 📊 SQL Queries Covered

The file `queries.sql` contains **20 queries**:

The results are exported into **`all_queries_results.xlsx`** for easy viewing.

---

## 📦 Requirements

Install dependencies using:
```bash
pip install -r requirements.txt
```

Example `requirements.txt`:
```
pandas
numpy
matplotlib
seaborn
sqlite3-binary
openpyxl
requests
```

---

## 📌 Notes

- Database used: **SQLite (`cricsheet.db`)**
- Data Source: [Cricsheet](https://cricsheet.org/)
- Each script is **modular** and can be run independently.
- Running `run_queries.py` will automatically execute **all 20 queries** and save results into Excel.

---

## 👨‍💻 Author

Developed by **Sabarish Balkrishnan**  
For data analysis & cricket insights.

