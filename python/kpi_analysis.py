import pandas as pd

sales = pd.read_csv("data/processed/sales.csv")
sales["sale_date"] = pd.to_datetime(sales["sale_date"])

kpis = sales.groupby("store_id").agg(
    total_revenue_kpi=("revenue", "sum"),
    avg_order_value_kpi=("revenue", "mean"),
    total_units_sold=("units_sold", "sum")
).reset_index()

kpis.to_csv("outputs/summary_tables/store_kpis.csv", index=False)
print("KPIs generated successfully")