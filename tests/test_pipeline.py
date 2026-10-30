import shutil

import yaml

from rfm_kmeans import config, pipeline


def test_pipeline_end_to_end(tmp_path, raw_df):
    cfg = config.load_config()
    raw_df.to_csv(tmp_path / "raw.csv", index=False)
    cfg["paths"].update({
        "raw_csv": str(tmp_path / "raw.csv"),
        "raw_xlsx": str(tmp_path / "none.xlsx"),
        "processed_dir": str(tmp_path / "proc"),
        "figures_dir": str(tmp_path / "fig"),
        "tables_dir": str(tmp_path / "tab"),
    })
    cfg["sampling"]["target_rows"] = 1500
    cfg["evaluation"]["stability_seeds"] = [1, 2, 3]
    cfg_file = tmp_path / "cfg.yaml"
    cfg_file.write_text(yaml.safe_dump(cfg), encoding="utf-8")

    res = pipeline.run(str(cfg_file), verbose=False)
    assert res["k"] in (3, 4, 5, 6)
    assert (tmp_path / "proc" / "rfm_clustered.csv").exists()
    assert (tmp_path / "tab" / "segment_profile.csv").exists()
    assert (tmp_path / "fig" / "clusters_pca.png").exists()
