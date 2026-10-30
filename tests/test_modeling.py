from rfm_kmeans import cleaning, evaluation, features, modeling, preprocessing


def _prepare(raw_df, cleaning_cfg):
    clean, _ = cleaning.clean_transactions(raw_df, cleaning_cfg)
    rfm = features.build_rfm(clean)
    X, _ = preprocessing.transform_rfm(rfm)
    return rfm, X


def test_scaling_mean_zero(raw_df, cleaning_cfg):
    _, X = _prepare(raw_df, cleaning_cfg)
    assert abs(X.mean().max()) < 1e-6


def test_scan_and_choose_k(raw_df, cleaning_cfg):
    _, X = _prepare(raw_df, cleaning_cfg)
    scan = modeling.scan_k(X, 2, 6)
    assert list(scan["k"]) == [2, 3, 4, 5, 6]
    assert modeling.choose_k(scan) in (3, 4, 5, 6)


def test_stability(raw_df, cleaning_cfg):
    _, X = _prepare(raw_df, cleaning_cfg)
    res = evaluation.stability_ari(X, 4, [1, 2, 3])
    assert -1 <= res["ari_mean"] <= 1
