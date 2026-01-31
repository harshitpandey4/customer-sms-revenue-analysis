"""
Customer SMS Revenue Analysis — One-File Runner
------------------------------------------------
What this script does (end-to-end):
1) Loads CSVs from ./data
2) Cleans and standardises fields (null IDs, message_type)
3) Builds a client-month fact table (joins revenue, sms, appointment)
4) Creates dashboard-ready outputs:
   - outputs/monthly_kpis.csv
   - outputs/message_type_mix.csv
   - outputs/churn_comparison.csv
   - outputs/client_month_fact.csv
5) Generates simple charts (saved to outputs/charts):
   - monthly_sms_sent.png
   - monthly_sms_revenue.png
   - monthly_revenue_per_sms.png
   - top_message_types.png

Requirements:
- Python 3.9+
- pandas
- matplotlib

Install:
  pip install pandas matplotlib

Run:
  python run_project.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# ----------------------------
# Config
# ----------------------------
DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")
CHART_DIR = OUTPUT_DIR / "charts"

FILES = {
    "clients": DATA_DIR / "clients.csv",
    "revenue": DATA_DIR / "revenue.csv",
    "appointment": DATA_DIR / "appointment.csv",
    "sms": DATA_DIR / "sms.csv",
}


# ----------------------------
# Helpers
# ----------------------------
def ensure_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CHART_DIR.mkdir(parents=True, exist_ok=True)


def assert_files_exist() -> None:
    missing = [str(p) for p in FILES.values() if not p.exists()]
    if missing:
        print("ERROR: Missing required data files:")
        for m in missing:
            print(f" - {m}")
        print("\nExpected files in ./data:")
        print(" - clients.csv")
        print(" - revenue.csv")
        print(" - appointment.csv")
        print(" - sms.csv")
        sys.exit(1)


def standardise_message_type(s: pd.Series) -> pd.Series:
    # Trim, uppercase, replace spaces with underscores (SQLite-like standardisation)
    return (
        s.astype(str)
        .str.strip()
        .str.upper()
        .str.replace(" ", "_", regex=False)
    )


def safe_divide(numer: pd.Series, denom: pd.Series) -> pd.Series:
    # Safe division: returns NaN when denom is 0/NaN
    denom = denom.replace(0, pd.NA)
    return numer / denom


def save_csv(df: pd.DataFrame, filename: str) -> None:
    path = OUTPUT_DIR / filename
    df.to_csv(path, index=False)
    print(f"Saved: {path}")


def save_line_chart(df: pd.DataFrame, x: str, y: str, title: str, filename: str) -> None:
    plt.figure()
    plt.plot(df[x], df[y])
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xticks(rotation=45)
    plt.tight_layout()
    out = CHART_DIR / filename
    plt.savefig(out, dpi=160)
    plt.close()
    print(f"Saved chart: {out}")


def save_bar_chart(df: pd.DataFrame, x: str, y: str, title: str, filename: str) -> None:
    plt.figure()
    plt.bar(df[x], df[y])
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    out = CHART_DIR / filename
    plt.savefig(out, dpi=160)
    plt.close()
    print(f"Saved chart: {out}")


def to_datetime_month(df: pd.DataFrame, col: str, df_name: str) -> pd.DataFrame:
    df[col] = pd.to_datetime(df[col], errors="coerce")
    bad = df[col].isna().sum()
    if bad > 0:
        print(f"WARNING: {df_name} has {bad} rows with invalid {col} -> dropped.")
        df = df.dropna(subset=[col]).copy()
    return df


def to_numeric(df: pd.DataFrame, col: str, df_name: str) -> pd.DataFrame:
    if col not in df.columns:
        print(f"ERROR: {df_name} is missing required column '{col}'")
        sys.exit(1)
    df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


# ----------------------------
# Main pipeline
# ----------------------------
def main() -> None:
    print("=== Customer SMS Revenue Analysis (One-File Runner) ===")
    ensure_dirs()
    assert_files_exist()

    # 1) Load
    clients = pd.read_csv(FILES["clients"])
    revenue = pd.read_csv(FILES["revenue"])
    appointment = pd.read_csv(FILES["appointment"])
    sms = pd.read_csv(FILES["sms"])

    print("\nLoaded datasets:")
    print("clients:", clients.shape)
    print("revenue:", revenue.shape)
    print("appointment:", appointment.shape)
    print("sms:", sms.shape)

    # 2) Drop null client_id rows
    for name, df in [("clients", clients), ("revenue", revenue), ("appointment", appointment), ("sms", sms)]:
        if "client_id" not in df.columns:
            print(f"ERROR: {name}.csv missing 'client_id' column.")
            sys.exit(1)

    before_clients = len(clients)
    clients = clients[clients["client_id"].notna()].copy()
    dropped_clients = before_clients - len(clients)

    revenue = revenue[revenue["client_id"].notna()].copy()
    appointment = appointment[appointment["client_id"].notna()].copy()
    sms = sms[sms["client_id"].notna()].copy()

    if dropped_clients > 0:
        print(f"\nCleaning: Dropped {dropped_clients} rows from clients due to null client_id")

    # 3) Validate required columns + types
    # Dates
    for df_name, df in [("revenue", revenue), ("appointment", appointment), ("sms", sms)]:
        if "year_month" not in df.columns:
            print(f"ERROR: {df_name}.csv missing 'year_month' column.")
            sys.exit(1)

    revenue = to_datetime_month(revenue, "year_month", "revenue")
    appointment = to_datetime_month(appointment, "year_month", "appointment")
    sms = to_datetime_month(sms, "year_month", "sms")

    # Numerics
    revenue = to_numeric(revenue, "sms_revenue_loc", "revenue")
    sms = to_numeric(sms, "sms_count", "sms")
    appointment = to_numeric(appointment, "total_active_appointment_count", "appointment")
    appointment = to_numeric(appointment, "staff_count", "appointment")

    # Optional numeric column
    if "sms_cost" in clients.columns:
        clients["sms_cost"] = pd.to_numeric(clients["sms_cost"], errors="coerce")

    # 4) Standardise message_type
    if "message_type" not in sms.columns:
        print("ERROR: sms.csv missing 'message_type' column.")
        sys.exit(1)
    sms["message_type"] = standardise_message_type(sms["message_type"])

    # 5) Basic validation summary
    print("\nNull summary (post-cleaning):")
    print("clients nulls:\n", clients.isnull().sum())
    print("revenue nulls:\n", revenue.isnull().sum())
    print("appointment nulls:\n", appointment.isnull().sum())
    print("sms nulls:\n", sms.isnull().sum())

    # 6) Aggregate to client-month level
    revenue_cm = (
        revenue.groupby(["client_id", "year_month"], as_index=False)
        .agg(sms_revenue=("sms_revenue_loc", "sum"))
    )

    sms_cm = (
        sms.groupby(["client_id", "year_month"], as_index=False)
        .agg(sms_sent=("sms_count", "sum"))
    )

    appt_cm = (
        appointment.groupby(["client_id", "year_month"], as_index=False)
        .agg(
            total_active_appointments=("total_active_appointment_count", "sum"),
            avg_staff_count=("staff_count", "mean"),
        )
    )

    # 7) Build client-month fact table
    fact = pd.merge(revenue_cm, sms_cm, on=["client_id", "year_month"], how="outer")
    fact = pd.merge(fact, appt_cm, on=["client_id", "year_month"], how="outer")

    # Fill missing numeric values with 0 where appropriate
    for col in ["sms_revenue", "sms_sent", "total_active_appointments", "avg_staff_count"]:
        if col in fact.columns:
            fact[col] = fact[col].fillna(0)

    # Add revenue_per_sms
    fact["revenue_per_sms"] = safe_divide(fact["sms_revenue"], fact["sms_sent"])

    # Add client attributes (if present)
    add_cols = [c for c in ["churned_flag", "region", "billing_currency", "golive_date"] if c in clients.columns]
    if add_cols:
        clients_small = clients[["client_id"] + add_cols].copy()
        fact = fact.merge(clients_small, on="client_id", how="left")

    fact = fact.sort_values(["year_month", "client_id"]).reset_index(drop=True)

    # 8) Output: Monthly KPIs
    monthly_kpis = (
        fact.groupby("year_month", as_index=False)
        .agg(
            active_clients=("client_id", "nunique"),
            sms_sent=("sms_sent", "sum"),
            sms_revenue=("sms_revenue", "sum"),
            total_active_appointments=("total_active_appointments", "sum"),
        )
    )
    monthly_kpis["revenue_per_sms"] = safe_divide(monthly_kpis["sms_revenue"], monthly_kpis["sms_sent"])
    monthly_kpis = monthly_kpis.sort_values("year_month").reset_index(drop=True)

    # 9) Output: Message type mix
    message_type_mix = (
        sms.groupby(["year_month", "message_type"], as_index=False)
        .agg(sms_sent=("sms_count", "sum"))
        .sort_values(["year_month", "message_type"])
        .reset_index(drop=True)
    )

    # 10) Output: Churn comparison
    churn_comparison = pd.DataFrame()
    if "churned_flag" in clients.columns:
        client_totals = (
            fact.groupby("client_id", as_index=False)
            .agg(
                sms_sent_total=("sms_sent", "sum"),
                sms_revenue_total=("sms_revenue", "sum"),
            )
        )
        client_totals["revenue_per_sms_total"] = safe_divide(
            client_totals["sms_revenue_total"], client_totals["sms_sent_total"]
        )
        merged = client_totals.merge(clients[["client_id", "churned_flag"]], on="client_id", how="left")

        churn_comparison = (
            merged.groupby("churned_flag", as_index=False)
            .agg(
                clients=("client_id", "nunique"),
                avg_sms_sent_total=("sms_sent_total", "mean"),
                avg_sms_revenue_total=("sms_revenue_total", "mean"),
                avg_revenue_per_sms_total=("revenue_per_sms_total", "mean"),
            )
            .sort_values("churned_flag")
            .reset_index(drop=True)
        )
    else:
        print("WARNING: clients.csv missing churned_flag. churn_comparison will not be generated.")

    # 11) Save outputs
    save_csv(fact, "client_month_fact.csv")
    save_csv(monthly_kpis, "monthly_kpis.csv")
    save_csv(message_type_mix, "message_type_mix.csv")
    if not churn_comparison.empty:
        save_csv(churn_comparison, "churn_comparison.csv")

    # 12) Save charts (simple, stakeholder-friendly)
    monthly_kpis_plot = monthly_kpis.copy()
    monthly_kpis_plot["year_month"] = monthly_kpis_plot["year_month"].dt.to_period("M").astype(str)

    save_line_chart(monthly_kpis_plot, "year_month", "sms_sent", "Monthly SMS Sent", "monthly_sms_sent.png")
    save_line_chart(monthly_kpis_plot, "year_month", "sms_revenue", "Monthly SMS Revenue", "monthly_sms_revenue.png")
    save_line_chart(monthly_kpis_plot, "year_month", "revenue_per_sms", "Monthly Revenue per SMS", "monthly_revenue_per_sms.png")

    top_types = (
        sms.groupby("message_type", as_index=False)["sms_count"].sum()
        .sort_values("sms_count", ascending=False)
        .head(10)
        .rename(columns={"sms_count": "sms_sent"})
        .reset_index(drop=True)
    )
    save_bar_chart(top_types, "message_type", "sms_sent", "Top 10 Message Types by SMS Volume", "top_message_types.png")

    # 13) Print quick summary
    print("\n=== Quick Summary ===")
    if not monthly_kpis.empty:
        print(
            "Date range (monthly_kpis):",
            monthly_kpis["year_month"].min().date(),
            "to",
            monthly_kpis["year_month"].max().date(),
        )
        print("Total SMS sent:", int(monthly_kpis["sms_sent"].sum()))
        print("Total SMS revenue:", float(monthly_kpis["sms_revenue"].sum()))
        rps = monthly_kpis["revenue_per_sms"].dropna()
        if not rps.empty:
            print("Avg revenue per SMS:", float(rps.mean()))
    print("\nOutputs saved to ./outputs")
    print("Charts saved to ./outputs/charts")
    print("\nDone ✅")


if __name__ == "__main__":
    main()
