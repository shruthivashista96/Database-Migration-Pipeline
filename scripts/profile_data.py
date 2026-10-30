import sqlite3
import pandas as pd

# Connect to the legacy database
db_path = '../data/legacy_system.db'
conn = sqlite3.connect(db_path)

# Load legacy customers into a pandas DataFrame
df = pd.read_sql('SELECT * FROM legacy_customers', conn)
conn.close()

print("--- DATA DISCOVERY & PROFILING REPORT ---")
print(f"Total Records Found: {len(df)}\n")

print("1. Raw Data Sample:")
print(df)
print("\n" + "="*40 + "\n")

print("2. Column Data Types & Non-Null Counts:")
print(df.info())
print("\n" + "="*40 + "\n")

print("3. Unique Account Statuses (Checking for inconsistencies):")
print(df['account_status'].value_counts())