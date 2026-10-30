"""Memuat data mentah Online Retail."""
from pathlib import Path

import pandas as pd

EXPECTED_COLUMNS = [
    "InvoiceNo", "StockCode", "Description", "Quantity",
    "InvoiceDate", "UnitPrice", "CustomerID", "Country",
]


def load_raw(csv_path, xlsx_path=None):
    """Muat data mentah. Pakai CSV bila ada, kalau tidak baca xlsx."""
    csv_path = Path(csv_path)
    if csv_path.exists():
        df = pd.read_csv(
            csv_path,
            dtype={"InvoiceNo": str, "StockCode": str},
            parse_dates=["InvoiceDate"],
        )
    elif xlsx_path is not None and Path(xlsx_path).exists():
        df = pd.read_excel(xlsx_path, dtype={"InvoiceNo": str, "StockCode": str})
    else:
        raise FileNotFoundError(
            "Data mentah tidak ditemukan. Jalankan: python scripts/download_data.py"
        )
    validate_columns(df)
    return df


def validate_columns(df):
    """Pastikan 8 kolom yang diharapkan ada."""
    missing = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Kolom hilang: {missing}")
