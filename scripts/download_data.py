"""Unduh dataset Online Retail dari UCI dan simpan ke data/raw/.

Jalankan dari root proyek:  python scripts/download_data.py
"""
import io
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
URL = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    xlsx = RAW / "Online Retail.xlsx"
    if not xlsx.exists():
        print("Mengunduh dataset dari UCI ...")
        with urllib.request.urlopen(URL) as resp:
            data = resp.read()
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            zf.extractall(RAW)
        print("Selesai ekstrak ke", RAW)
    else:
        print("Berkas sudah ada:", xlsx)

    # Simpan versi CSV agar pemuatan berikutnya cepat
    import pandas as pd

    csv = RAW / "online_retail.csv"
    if not csv.exists():
        df = pd.read_excel(xlsx, dtype={"InvoiceNo": str, "StockCode": str})
        df.to_csv(csv, index=False)
        print(f"CSV dibuat: {csv} ({len(df):,} baris)")


if __name__ == "__main__":
    sys.exit(main())
