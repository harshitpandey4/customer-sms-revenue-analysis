# Customer SMS Revenue Analysis

## Overview
This project is an end-to-end **customer analytics case study** analysing SMS engagement, revenue trends, and churn behaviour using anonymised transactional data.  
The goal is to demonstrate how raw operational data can be transformed into **clear, actionable insights** for both technical and non-technical stakeholders.

The analysis combines:
- **SQL** for data cleaning, joins, and KPI development  
- **Basic Python** for data validation and exploratory analysis  
- **Dashboards** to communicate insights clearly to non-technical business users

> **Note:** This is a portfolio project. All datasets are anonymised and do not represent real customers or businesses.

---

## Business Questions
The analysis focuses on answering practical business questions such as:
- How does SMS usage and SMS-generated revenue trend over time?
- What is the revenue generated per SMS?
- Which SMS message types contribute most to overall usage?
- Do churned customers show different SMS and revenue behaviour compared to retained customers?
- How can insights be communicated clearly to non-technical stakeholders?

---

## Datasets
The project uses four anonymised datasets:

- **clients.csv**  
  Client-level attributes including region, SMS cost, go-live date, billing currency, and churn flag.

- **revenue.csv**  
  Monthly SMS revenue per client.

- **sms.csv**  
  Monthly SMS volume per client, broken down by message type.

- **appointment.csv**  
  Monthly appointment activity per client (used for contextual analysis).

---

## Data Cleaning & Preparation
Key preparation steps include:
- Removing records with missing client identifiers
- Standardising SMS message type categories
- Aligning date ranges where required for multi-table analysis
- Creating client-month level aggregates for consistent KPI calculation

---

## Analysis Approach

### SQL
SQL is used as the primary analysis tool to:
- Join multiple datasets at a client-month level
- Build core KPIs such as total SMS sent, total revenue, and revenue per SMS
- Compare behaviour between churned and non-churned customers
- Produce clean output tables ready for visualisation

### Python (Basic)
Python is used selectively for:
- Data validation and sanity checks
- Exploratory trend analysis
- Simple visualisations to support findings

Libraries used:
- `pandas`
- `matplotlib`

### Dashboards
Dashboards are created to:
- Translate analytical findings into clear visuals
- Support understanding for **non-technical stakeholders**
- Enable data-driven decision-making without requiring SQL or Python knowledge

---

## Key Insights (Example)
- SMS volume and revenue show clear monthly trends and seasonality.
- Certain message types account for a disproportionately high share of SMS usage.
- Revenue per SMS varies over time, indicating opportunities for pricing or usage optimisation.
- Churned clients display different engagement and revenue patterns compared to retained clients.

(*Detailed insights are documented in the analysis outputs and dashboards.*)

---
