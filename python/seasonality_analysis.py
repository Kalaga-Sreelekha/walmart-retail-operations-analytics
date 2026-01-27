import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("data/processed/sales.csv")
sales["sale_date"] = pd.to_datetime(sales["sale_date"])
sales["month"] = sales["sale_date"].dt.month

monthly = sales.groupby("month")["revenue"].sum()

plt.figure()
monthly.plot()
plt.title("Monthly Revenue Seasonality")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("outputs/charts/monthly_revenue.png")