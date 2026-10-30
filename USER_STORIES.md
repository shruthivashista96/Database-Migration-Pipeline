Epic: Legacy Customer Repository (LCR) to Unified Customer Hub (UCH) Migration
Epic Description:

As the Scotiabank Enterprise Data Team, we need to migrate customer data from the Legacy Customer Repository (LCR) to the modern Unified Customer Hub (UCH) so that downstream systems receive high-quality, standardized customer records for analytics and reporting.

👤 User Story 1: Data Profiling & Hygiene Assessment
Story ID: LCR-101

Title: Source Data Profile & Exception Analysis

User Story:

As a Lead Business Systems Analyst,

I want to profile the source records in the Legacy Customer Repository (LCR),

So that I can identify data anomalies, inconsistent schemas, and formatting defects prior to execution.

Acceptance Criteria:

Audit 100% of existing customer records for null/missing values across signup_date, account_status, and credit_score.

Document all date formats present (e.g., ISO YYYY-MM-DD vs. slash formats DD/MM/YYYY).

Flag non-standard string representations (e.g., literal text 'NULL' in numeric columns).

Produce a data profiling report summary highlighting exception volume.

👤 User Story 2: Data Transformation & Standardization Engine
Story ID: LCR-102

Title: Transform & Load Customer Schema to UCH

User Story:

As an Enterprise Data Engineer,

I want to apply defined transformation rules during extraction,

So that customer data loaded into the Unified Customer Hub (UCH) adheres to target schema standards.

Acceptance Criteria:

Name Field: Convert full_name strings to Title Case and split into discrete first_name and last_name attributes.

Date Field: Parse mixed date input formats into a uniform ISO standard (YYYY-MM-DD). Invalid dates must raise an exception log rather than corrupting historical data.

Status Field: Convert all account_status values to uppercase (ACTIVE, INACTIVE, PENDING).

Credit Score Field: Convert literal string 'NULL' or empty strings to database null/numeric zero values.

👤 User Story 3: Reconciliation & Integrity Validation
Story ID: LCR-103

Title: Automated Source-to-Target Reconciliation Check

User Story:

As a Quality Assurance Lead & BSA,

I want an automated reconciliation script to validate row counts post-load,

So that we guarantee zero data loss between LCR and UCH.

Acceptance Criteria:

Extract total record count from legacy_customers prior to transformation.

Query total record count from customers in target_system.db post-load.

Perform a count check comparison: Source Count == Target Count.

Output an automated status message (MATCHED / MISMATCH) to the validation log.