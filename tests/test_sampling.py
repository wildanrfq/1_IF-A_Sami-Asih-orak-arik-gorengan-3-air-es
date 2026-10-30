from rfm_kmeans.sampling import sample_by_customer


def test_sampling_keeps_full_customer_history(raw_df):
    sample = sample_by_customer(raw_df, target_rows=800, seed=42)
    full = raw_df.dropna(subset=["CustomerID"])
    for cid in sample["CustomerID"].unique()[:20]:
        assert (sample["CustomerID"] == cid).sum() == (full["CustomerID"] == cid).sum()


def test_sampling_reproducible(raw_df):
    a = sample_by_customer(raw_df, 800, seed=42)
    b = sample_by_customer(raw_df, 800, seed=42)
    assert a.equals(b)
