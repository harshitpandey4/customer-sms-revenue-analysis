# Customer SMS Revenue Analysis

## Overview
This project is an end-to-end **customer analytics case study** analysing **SMS engagement**, **revenue trends**, and **churn behaviour** using anonymised transactional data.  
The objective is to demonstrate how raw operational data can be transformed into **clear, actionable business insights** for both technical and non-technical stakeholders.

The analysis combines:
- **SQL** for data cleaning, joins, and KPI development  
- **Basic Python** for data validation and exploratory analysis  
- **Dashboards** (maintained separately) to communicate insights clearly to business users

> **Note:** This is a portfolio project. All datasets are anonymised and do not represent real customers or businesses.

---

## Business Questions
The project focuses on answering practical business questions, including:
- How do SMS usage and SMS-generated revenue trend over time?
- What is the revenue generated per SMS?
- Which SMS message types contribute most to overall usage?
- Do churned customers exhibit different SMS and revenue behaviour compared to retained customers?
- How can insights be communicated clearly to non-technical stakeholders?

---

## Datasets
The analysis is based on four anonymised datasets:

- **clients.csv**  
  Client-level attributes such as region, SMS cost, go-live date, billing currency, and churn flag.

- **revenue.csv**  
  Monthly SMS revenue per client.

- **sms.csv**  
  Monthly SMS volume per client, segmented by message type.

- **appointment.csv**  
  Monthly appointment activity per client, used as a contextual behavioural signal.

### Data Notes
- Datasets cover different date ranges. Where multi-table analysis is required, results are aligned to overlapping months.
- SMS message type values are standardised during data cleaning.

---

## Data Cleaning & Preparation
Key preparation steps include:
- Removing records with missing client identifiers
- Standardising SMS message type categories
- Aligning date ranges for joined analysis
- Creating client-month level aggregates for consistent KPI calculation

---

## Analysis Approach

### SQL (Primary)
SQL is used as the primary analysis tool to:
- Join datasets at a client-month level
- Build core KPIs such as total SMS sent, total revenue, and revenue per SMS
- Analyse engagement and revenue trends over time
- Compare churned and retained customer cohorts

### Python (Basic)
Python is used selectively to support the SQL analysis by:
- Performing data validation and sanity checks
- Conducting exploratory analysis
- Creating simple trend visualisations

Libraries used:
- `pandas`
- `matplotlib`
  
---
## Tools & Technologies
- SQL (SQLite; logic transferable to Postgres)
- Python (pandas, matplotlib)
- Dashboards (maintained separately)
- GitHub for version control and documentation

---

## Author
Created as a portfolio project to demonstrate business analysis, data analytics, and stakeholder communication skills.
