"""Sampling per CustomerID agar riwayat pelanggan tidak terpotong."""
import numpy as np


def sample_by_customer(df, target_rows, seed=42):
    """Ambil pelanggan secara acak sampai jumlah baris mendekati target_rows.

    Seluruh transaksi milik pelanggan terpilih ikut diambil.
    Baris tanpa CustomerID tidak ikut (tidak dipakai untuk RFM).
    """
    data = df.dropna(subset=["CustomerID"])
    rows_per_customer = data.groupby("CustomerID").size()

    rng = np.random.default_rng(seed)
    order = rng.permutation(rows_per_customer.index.to_numpy())
    cumulative = rows_per_customer.loc[order].cumsum()

    n_selected = int((cumulative < target_rows).sum()) + 1
    selected = order[:n_selected]
    return data[data["CustomerID"].isin(selected)].copy()


def compare_distribution(full, sample, column="Country", top=5):
    """Bandingkan proporsi kategori antara data penuh dan sampel."""
    import pandas as pd

    a = full[column].value_counts(normalize=True).head(top)
    b = sample[column].value_counts(normalize=True)
    return pd.DataFrame({"penuh": a, "sampel": b.reindex(a.index)}).round(4)
