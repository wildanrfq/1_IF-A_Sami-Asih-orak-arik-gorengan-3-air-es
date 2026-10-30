from rfm_kmeans.cleaning import clean_transactions


def test_cleaning_removes_dirty_rows(raw_df, cleaning_cfg):
    clean, log = clean_transactions(raw_df, cleaning_cfg)
    assert clean["CustomerID"].notna().all()
    assert (clean["Quantity"] > 0).all()
    assert (clean["UnitPrice"] > 0).all()
    assert not clean["InvoiceNo"].astype(str).str.startswith("C").any()
    assert not clean["StockCode"].isin(["POST"]).any()
    assert not clean.duplicated().any()
    assert log["akhir"] < log["awal"]
