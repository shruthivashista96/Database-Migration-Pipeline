import sqlite3
import os

# Ensure data directory exists
os.makedirs('../data', exist_ok=True)
db_path = '../data/legacy_system.db'

# Connect to SQLite (creates the file automatically)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a messy legacy customer table
cursor.execute('''
CREATE TABLE IF NOT EXISTS legacy_customers (
    customer_id TEXT,
    full_name TEXT,
    signup_date TEXT,
    account_status TEXT,
    credit_score TEXT
)
''')

# Insert some messy legacy sample data
sample_data = [
    ('CUST-001', 'john doe', '2023-01-15', 'ACTIVE', '720'),
    ('CUST-002', 'JANE SMITH', '15/02/2023', 'inactive', '650'),  # Notice the messy date format and lowercase/uppercase
    ('CUST-003', 'Bob Johnson', '2023-03-10', 'ACTIVE', 'NULL'),  # Notice the string 'NULL' instead of database null
    ('CUST-004', 'Alice Brown', '2023/04/22', 'PENDING', '810')   # Another weird date format
]

cursor.executemany('INSERT INTO legacy_customers VALUES (?, ?, ?, ?, ?)', sample_data)
conn.commit()
conn.close()

print("Legacy database successfully created with messy sample data at ../data/legacy_system.db!")