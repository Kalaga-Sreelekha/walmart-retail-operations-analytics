import pandas as pd
import numpy as np

np.random.seed(42)

stores = range(1, 21)
products = range(100, 150)
dates = pd.date_range("2024-01-01", "2024-12-31")

records = []
for d in dates:
    for s in stores:
        for p in np.random.choice(products, 5):
            units = np.random.poisson(5)
            price = np.random.uniform(5, 50)
            records.append([d, s, p, units, units * price])

sales = pd.DataFrame(records, columns=[
    "sale_date", "store_id", "product_id", "units_sold", "revenue"
])

sales.to_csv("sales.csv", index=False)