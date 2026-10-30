"""Pipeline end-to-end: load -> sample -> clean -> RFM -> scale -> K-Means -> profil."""
import json
from pathlib import Path

from . import (cleaning, config, data_loader, evaluation, features, modeling,
               preprocessing, profiling, sampling, visualization)


def run(cfg_path="configs/config.yaml", k=None, verbose=True):
    cfg = config.load_config(cfg_path)
    seed = cfg["seed"]
    out = config.resolve(cfg, "processed_dir")
    fig_dir = config.resolve(cfg, "figures_dir")
    tab_dir = config.resolve(cfg, "tables_dir")
    for d in (out, fig_dir, tab_dir):
        Path(d).mkdir(parents=True, exist_ok=True)

    def say(msg):
        if verbose:
            print(msg)

    # 1. Load + sampling
    raw = data_loader.load_raw(config.resolve(cfg, "raw_csv"), config.resolve(cfg, "raw_xlsx"))
    say(f"[1] Data mentah: {len(raw):,} baris")
    if cfg["sampling"]["enabled"]:
        raw = sampling.sample_by_customer(raw, cfg["sampling"]["target_rows"], seed)
        say(f"    Sampel per CustomerID: {len(raw):,} baris")
    raw.to_csv(out / "sample_transactions.csv", index=False)

    # 2. Cleaning
    clean, log = cleaning.clean_transactions(raw, cfg["cleaning"])
    clean.to_csv(out / "clean_transactions.csv", index=False)
    (tab_dir / "cleaning_log.json").write_text(json.dumps(log, indent=2), encoding="utf-8")
    say(f"[2] Setelah cleaning: {log['akhir']:,} baris ({log['persen_tersisa']}%)")

    # 3. RFM + scaling
    rfm = features.build_rfm(clean, cfg["rfm"]["reference_offset_days"])
    X, _ = preprocessing.transform_rfm(rfm, cfg["preprocessing"]["log_transform"])
    rfm.to_csv(out / "rfm.csv", index=False)
    X.to_csv(out / "rfm_scaled.csv")
    say(f"[3] Pelanggan dianalisis: {len(rfm):,}")

    # 4. Pilih k + modeling
    m = cfg["modeling"]
    scan = modeling.scan_k(X, m["k_min"], m["k_max"], seed, m["n_init"])
    scan.to_csv(tab_dir / "k_selection.csv", index=False)
    k = k or modeling.choose_k(scan, m["k_candidates"])
    model = modeling.fit_kmeans(X, k, seed, m["n_init"], m["max_iter"])
    labels = model.labels_
    say(f"[4] k terpilih = {k}")

    # 5. Evaluasi
    checks = evaluation.check_smart_targets(X, labels, cfg["evaluation"])
    stab = evaluation.stability_ari(X, k, cfg["evaluation"]["stability_seeds"], m["n_init"])
    checks.to_csv(tab_dir / "smart_checks.csv", index=False)
    (tab_dir / "stability.json").write_text(json.dumps(stab, indent=2), encoding="utf-8")
    say(f"[5] Stabilitas ARI rata-rata: {stab['ari_mean']:.3f}")

    # 6. Profil + strategi
    prof = profiling.profile_segments(rfm, labels)
    mapping = profiling.suggest_label(prof)
    result = profiling.add_segment_names(rfm, labels, mapping)
    prof["Segmen"] = prof.index.map(mapping)
    prof.to_csv(tab_dir / "segment_profile.csv")
    result.to_csv(out / "rfm_clustered.csv", index=False)

    # 7. Grafik
    visualization.plot_rfm_distribution(rfm, fig_dir / "rfm_distribution.png")
    visualization.plot_rfm_correlation(rfm, fig_dir / "rfm_correlation.png")
    visualization.plot_k_selection(scan, fig_dir / "k_selection.png")
    visualization.plot_clusters_pca(X, labels, fig_dir / "clusters_pca.png")
    visualization.plot_segment_summary(prof, fig_dir / "segment_summary.png")
    say("[6] Selesai. Hasil di data/processed, reports/tables, reports/figures")
    return {"rfm": result, "profile": prof, "checks": checks, "stability": stab, "k": k}
