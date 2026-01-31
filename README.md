# Customer SMS Revenue Analysis

## Overview
This project is an end-to-end **customer analytics case study** analysing **SMS engagement**, **revenue trends**, and **churn behaviour** using anonymised transactional data.  
The goal is to show how raw operational data can be transformed into **clear, actionable insights** for both technical and non-technical stakeholders.

The analysis combines:
- **SQL** for data cleaning, joins, and KPI development
- **Basic Python** for validation and exploratory analysis
- **Dashboards** to communicate insights clearly to business users

> **Note:** This is a portfolio project. All datasets are anonymised and do not represent real customers or businesses.

---

## Business Questions
- How do SMS usage and SMS-generated revenue trend over time?
- What is the revenue generated per SMS?
- Which message types contribute most to overall SMS volume?
- Do churned customers show different SMS/revenue behaviour compared to retained customers?
- How can insights be communicated clearly to non-technical stakeholders?

---

## Datasets
This project uses four anonymised datasets:

- **clients.csv**  
  Client attributes: region, SMS cost, go-live date, billing currency, churn flag.
- **revenue.csv**  
  Monthly SMS revenue per client.
- **sms.csv**  
  Monthly SMS volume per client, split by message type.
- **appointment.csv**  
  Monthly appointment activity per client (contextual signal).

### Data Notes
- Some datasets cover different date ranges. For multi-table analysis, results are aligned to the overlapping months where required.
- Message type values are standardised during cleaning (e.g., casing/spacing).

---

## Data Cleaning & Preparation
- Removed records with missing client identifiers
- Standardised message type categories
- Aligned date ranges for joined analysis
- Built client-month aggregates for consistent KPI calculation

---

## Analysis Approach

### SQL
SQL is used to:
- Join datasets at a client-month level
- Build KPIs (SMS sent, SMS revenue, revenue per SMS)
- Compare churned vs non-churned cohorts
- Produce clean output tables for visualisation

### Python (Basic)
Python is used selectively for:
- Data validation checks
- Exploratory analysis
- Simple trend visuals

Libraries:
- `pandas`
- `matplotlib`

---

## Dashboards (for non-technical stakeholders)
Dashboards were created to translate findings into clear visuals for business users.

**Suggested views:**
- **Executive Summary:** total SMS sent, total revenue, revenue per SMS, trend line by month
- **Message Type Mix:** share of SMS by message type over time
- **Churn Comparison:** churned vs retained behaviour (volume + revenue)

> Add screenshots here:
- `dashboards/executive_summary.png`
- `dashboards/message_type_mix.png`
- `dashboards/churn_comparison.png`

---

## Key Insights (Example)
- SMS volume and revenue show monthly trends and seasonality.
- Certain message types account for a disproportionately high share of usage.
- Revenue per SMS varies over time, indicating optimisation opportunities.
- Churned clients show different engagement patterns than retained clients.

---

## How to Run

### Option A: SQL (recommended)
1. Load CSVs into your database (Postgres-compatible).
2. Run scripts in order:
   - `sql/00_create_tables.sql`
   - `sql/01_cleaning.sql`
   - `sql/02_kpi_core.sql`
   - `sql/03_sms_effectiveness.sql`
   - `sql/04_churn_signals.sql`

### Option B: Python (basic exploration)
1. Install dependencies:
   - `pip install pandas matplotlib`
2. Run notebooks inside `/python` for validation + exploratory analysis.

---

## Tools & Technologies
- SQL (Postgres-compatible)
- Python (pandas, matplotlib)
- Dashboards (screenshots/exports)
- GitHub for version control and documentation

---

## Author
Created as a portfolio project to demonstrate business analysis, data analytics, and stakeholder communication skills.
