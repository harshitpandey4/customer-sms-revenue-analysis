# Dashboards (Non-Technical View)

These dashboards translate the analysis into **clear, decision-ready insights** for non-technical stakeholders.  
They are designed to answer three core questions:

**What’s happening? Why might it be happening? What should we do next?**

> Note: All dashboards are based on anonymised data and created solely for portfolio demonstration purposes.

---

## 1) Executive Summary — SMS Performance Overview

**Problem statement**  
Stakeholders need a high-level view of SMS activity and revenue performance to quickly understand whether the channel is growing, stagnating, or declining.

<img width="939" height="532" alt="Executive Summary" src="https://github.com/user-attachments/assets/462631f0-3594-4e84-9777-d70049433950" />

**What this dashboard shows**
- Overall SMS volumes over time
- SMS-generated revenue trends
- Revenue earned per SMS

**Key questions answered**
- Is SMS usage increasing or decreasing?
- Is SMS revenue growing faster than usage?
- Is the business becoming more or less efficient at monetising SMS?

**How to use it**
- Start here for a quick health check.
- Use this view to identify periods that require deeper investigation using the dashboards below.

---

## 2) Message Type Mix — What Drives SMS Volume?

**Problem statement**  
Not all SMS messages deliver equal value. Understanding which message types dominate usage helps identify cost drivers and engagement patterns.

<img width="788" height="652" alt="Message Type Mix" src="https://github.com/user-attachments/assets/e17e5d1b-18eb-4c0c-b5d2-7585e6e82c17" />
<img width="824" height="649" alt="Message Type Trends" src="https://github.com/user-attachments/assets/3be12a21-771b-48c3-9b5c-276b7f1559e7" />

**What this dashboard shows**
- Distribution of SMS volume by message type
- Changes in message type usage over time

**Key questions answered**
- Which message types account for the majority of SMS traffic?
- Are some message types growing faster than others?
- Is SMS usage concentrated in a small number of categories?

**How to use it**
- Identify high-volume message types that may drive cost.
- Prioritise optimisation efforts on message categories with high usage but unclear value.

---

## 3) Churn Comparison — Retained vs Churned Behaviour

**Problem statement**  
Understanding behavioural differences between retained and churned customers helps identify early warning signals and improve retention strategies.

<img width="838" height="803" alt="Churn SMS Behaviour" src="https://github.com/user-attachments/assets/10f55f33-0e63-4511-a2f3-a8d23bdfce15" />
<img width="842" height="775" alt="Churn Revenue Behaviour" src="https://github.com/user-attachments/assets/a639a556-a1a0-49fe-8ce3-bd95fdeb648b" />

**What this dashboard shows**
- Average SMS usage for churned vs retained customers
- Revenue contribution by churn group
- Revenue per SMS comparison

**Key questions answered**
- Do churned customers engage less via SMS?
- Is SMS revenue lower among churned customers?
- Are there efficiency differences in revenue per SMS?

**How to use it**
- Use these patterns as input into churn prediction or retention initiatives.
- Support proactive outreach to customers showing declining engagement.

---

## 4) Yearly SMS Revenue Trend

**Problem statement**  
Stakeholders need to understand whether SMS revenue growth is sustainable over time.

<img width="892" height="854" alt="image" src="https://github.com/user-attachments/assets/b2532e54-9ec9-40cb-8d84-4efb133de636" />

**What this dashboard shows**
- Year-over-year comparison of SMS-generated revenue

**Key questions answered**
- Is SMS revenue accelerating or slowing?
- Is growth driven by volume increases or pricing effects?

**How to use it**
- Support strategic planning and forecasting discussions.
- Validate whether SMS remains a growing revenue channel.

---

## 5) SMS Pricing & Margin Analysis

**Problem statement**  
Pricing decisions directly affect margins. This dashboard explores how different SMS price points impact revenue and profitability.

<img width="785" height="1124" alt="image" src="https://github.com/user-attachments/assets/6386ac04-3593-4cec-83f2-89e6a6d8ef05" />


**What this dashboard shows**
- SMS cost assumptions
- Revenue and margin at different price levels
- Gross margin percentage comparison

**Key questions answered**
- How sensitive revenue is to SMS pricing changes?
- Which price points maximise margin without excessive cost?
- Is current pricing sustainable?

**How to use it**
- Support pricing strategy discussions.
- Identify opportunities to improve profitability.

---

## 6) Message Types vs Appointments

**Problem statement**  
Some SMS messages are closely tied to operational outcomes, such as appointments. Understanding this relationship helps assess effectiveness.

<img width="928" height="645" alt="image" src="https://github.com/user-attachments/assets/5260c710-2a1f-4017-98ae-03fdcb49026b" />


**What this dashboard shows**
- SMS volume by message type alongside appointment activity

**Key questions answered**
- Which message types are most strongly associated with appointments?
- Are high-volume messages translating into operational impact?

**How to use it**
- Focus messaging efforts on message types with clear business impact.
- Reduce low-impact messaging where appropriate.

---

## 7) Message Type Variability

**Problem statement**  
Highly variable message volumes can create operational and cost unpredictability.

<img width="905" height="695" alt="image" src="https://github.com/user-attachments/assets/13e0c47c-584d-419a-9ef0-4adface79f44" />


**What this dashboard shows**
- Variability in monthly SMS volume by message type

**Key questions answered**
- Which message types are stable and predictable?
- Which message types show bursty or inconsistent usage?

**How to use it**
- Improve forecasting and capacity planning.
- Identify message types that may require tighter controls.

---

## Recommended Stakeholder Actions (Example)

Based on insights typically surfaced by these dashboards, stakeholders may consider:
- Reviewing high-volume message types to ensure they deliver measurable value
- Monitoring revenue per SMS to detect pricing or usage inefficiencies
- Using churn behaviour patterns as early warning signals
- Aligning SMS strategy more closely with appointment and engagement outcomes

---

## Files & Outputs

Dashboards are built using analysis outputs generated by `run_project.py`, including:
- `outputs/monthly_kpis.csv`
- `outputs/message_type_mix.csv`
- `outputs/churn_comparison.csv`
- `outputs/client_month_fact.csv`
