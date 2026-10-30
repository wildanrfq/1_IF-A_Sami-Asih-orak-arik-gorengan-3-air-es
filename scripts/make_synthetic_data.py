"""Buat data sintetis kecil untuk uji cepat pipeline tanpa mengunduh UCI.

Output: data/raw/online_retail.csv (HANYA untuk demo, bukan data asli).
"""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def make(n_customers=600, seed=42):
    rng = np.random.default_rng(seed)
    rows, inv = [], 500000
    start = pd.Timestamp("2010-12-01")
    for cid in range(12000, 12000 + n_customers):
        profile = rng.choice(["champ", "loyal", "new", "lost"], p=[0.1, 0.3, 0.25, 0.35])
        n_inv = {"champ": 25, "loyal": 8, "new": 2, "lost": 2}[profile]
        n_inv = max(1, int(rng.poisson(n_inv)))
        last_day = 360 if profile in ("champ", "loyal", "new") else 120
        for _ in range(n_inv):
            inv += 1
            day = int(rng.integers(0, last_day if profile != "new" else 365))
            date = start + pd.Timedelta(days=day, hours=int(rng.integers(8, 18)))
            for _ in range(int(rng.integers(1, 6))):
                rows.append([str(inv), str(int(rng.integers(20000, 20100))), "ITEM",
                             int(rng.integers(1, 12)), date,
                             round(float(rng.uniform(0.5, 15)), 2), float(cid), "United Kingdom"])
    df = pd.DataFrame(rows, columns=["InvoiceNo", "StockCode", "Description", "Quantity",
                                     "InvoiceDate", "UnitPrice", "CustomerID", "Country"])
    # sisipkan data kotor
    dirty = df.sample(30, random_state=1).copy()
    dirty["InvoiceNo"] = "C" + dirty["InvoiceNo"]
    dirty["Quantity"] = -dirty["Quantity"]
    nocust = df.sample(40, random_state=2).copy()
    nocust["CustomerID"] = np.nan
    post = df.sample(10, random_state=3).copy()
    post["StockCode"] = "POST"
    return pd.concat([df, dirty, nocust, post, df.head(15)], ignore_index=True)


if __name__ == "__main__":
    out = ROOT / "data" / "raw" / "online_retail.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    make().to_csv(out, index=False)
    print("Data sintetis ditulis ke", out)
