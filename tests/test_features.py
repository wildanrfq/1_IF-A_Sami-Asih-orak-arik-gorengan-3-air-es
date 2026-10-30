import pandas as pd

from rfm_kmeans.features import build_rfm


def test_rfm_values(small_tx):
    rfm = build_rfm(small_tx, reference_offset_days=1).set_index("CustomerID")
    # tanggal acuan = 2011-01-11
    assert rfm.loc[1, "Recency"] == 1
    assert rfm.loc[2, "Recency"] == 6
    assert rfm.loc[1, "Frequency"] == 2
    assert rfm.loc[2, "Frequency"] == 1       # satu InvoiceNo unik
    assert rfm.loc[1, "Monetary"] == 2 * 10 + 1 * 5
    assert rfm.loc[2, "Monetary"] == 3 * 2 + 1 * 4


def test_rfm_one_row_per_customer(small_tx):
    assert build_rfm(small_tx)["CustomerID"].is_unique
