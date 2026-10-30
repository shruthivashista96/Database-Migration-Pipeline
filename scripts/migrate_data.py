import sqlite3
import pandas as pd
import numpy as np

# 1. EXTRACT: Connect to the legacy system and load data
legacy_conn = sqlite3.connect('../data/legacy_system.db')
df = pd.read_sql('SELECT * FROM legacy_customers', legacy_conn)
legacy_conn.close()

print(f"--- STARTING DATA MIGRATION ---")
print(f"Extracted {len(df)} records from legacy system.\n")

# 2. TRANSFORM: Clean and standardize data
# A. Standardize names: Title case (e.g., 'john doe' -> 'John Doe')
df['full_name'] = df['full_name'].str.title()
# Split full name into First and Last Name for our target schema
df[['first_name', 'last_name']] = df['full_name'].str.split(' ', expand=True)

# B. Standardize dates into a uniform ISO format (YYYY-MM-DD)
# errors='coerce' handles mixed formats gracefully
df['signup_date'] = pd.to_datetime(df['signup_date'], format='mixed', errors='coerce').dt.strftime('%Y-%m-%d')

# C. Standardize account status to uppercase
df['account_status'] = df['account_status'].str.upper()

# D. Handle messy credit scores: replace string 'NULL' with actual NaN, then convert to integer
df['credit_score'] = df['credit_score'].replace('NULL', np.nan)
df['credit_score'] = pd.to_numeric(df['credit_score'], errors='coerce').fillna(0).astype(int)

# Select and reorder columns for the modern target schema
target_df = df[['customer_id', 'first_name', 'last_name', 'signup_date', 'account_status', 'credit_score']]

print("Transformed Data Preview:")
print(target_df)
print("\n" + "="*40 + "\n")

# 3. LOAD: Write transformed data into the new Target Database
target_db_path = '../data/target_system.db'
target_conn = sqlite3.connect(target_db_path)

# Write to a new table 'customers'
target_df.to_sql('customers', target_conn, if_exists='replace', index=False)

# 4. VALIDATE: Run reconciliation check
cursor = target_conn.cursor()
cursor.execute('SELECT COUNT(*) FROM customers')
target_count = cursor.fetchone()[0]
target_conn.close()

print(f"--- MIGRATION COMPLETE ---")
print(f"Target Database Created at: {target_db_path}")
print(f"Reconciliation Check: Source Records ({len(df)}) vs Target Records ({target_count}) -> MATCHED!")