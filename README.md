# Database-to-Database Migration & Cleansing Pipeline

## 📌 Project Overview
This project simulates an enterprise database upgrade and data migration lifecycle. It extracts legacy customer data containing common data quality issues (mixed case naming, inconsistent date formats, string-based null values), transforms the schema and data types to meet modern standards, and loads it into a target relational database with automated validation reporting.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, NumPy, SQLite3
- **Database:** SQLite (Relational)

## 🔄 Data Migration Lifecycle (ETL)
1. **Discovery & Profiling:** Analyzed legacy records to identify missing values, schema gaps, and formatting inconsistencies (`profile_data.py`).
2. **Mapping & Transformation:** 
   - Standardized full names to Title Case and split them into distinct `first_name` and `last_name` fields.
   - Handled mixed date formats (`YYYY-MM-DD`, `DD/MM/YYYY`, `YYYY/MM/DD`) using flexible parsing.
   - Cleaned up corrupted string values (`'NULL'`) and converted them to database-safe nulls/integers.
3. **Load & Reconciliation:** Loaded cleansed data into a target schema and executed an automated record count reconciliation to guarantee zero data loss.

## 📂 Project Structure
```text
DataMigrationProject/
│
├── data/
│   ├── legacy_system.db      # Source database with raw, messy data
│   └── target_system.db      # Cleaned, modernized target database
│
├── scripts/
│   ├── setup_legacy_db.py    # Generates mock legacy data
│   ├── profile_data.py       # Data discovery and profiling report script
│   └── migrate_data.py       # Core ETL and validation script
│
└── README.md                 # Project documentation