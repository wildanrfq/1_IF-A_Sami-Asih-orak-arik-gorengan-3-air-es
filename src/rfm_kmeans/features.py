"""Pembentukan fitur RFM per pelanggan."""
import pandas as pd


def build_rfm(df, reference_offset_days=1, reference_date=None):
    """Hitung Recency, Frequency, Monetary per CustomerID.

    Recency   = selisih (hari) tanggal acuan dan transaksi terakhir
    Frequency = jumlah InvoiceNo unik
    Monetary  = total Quantity x UnitPrice
    """
    data = df.copy()
    data["TotalPrice"] = data["Quantity"] * data["UnitPrice"]

    if reference_date is None:
        reference_date = data["InvoiceDate"].max() + pd.Timedelta(days=reference_offset_days)

    rfm = data.groupby("CustomerID").agg(
        Recency=("InvoiceDate", lambda s: (reference_date - s.max()).days),
        Frequency=("InvoiceNo", "nunique"),
        Monetary=("TotalPrice", "sum"),
    )
    return rfm.reset_index()
