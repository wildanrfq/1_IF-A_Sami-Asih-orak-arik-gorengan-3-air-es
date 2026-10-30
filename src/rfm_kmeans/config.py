"""Memuat konfigurasi dari configs/config.yaml."""
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def load_config(path="configs/config.yaml"):
    """Baca berkas YAML dan kembalikan dict konfigurasi."""
    cfg_path = Path(path)
    if not cfg_path.is_absolute():
        cfg_path = ROOT / cfg_path
    with open(cfg_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve(cfg, key):
    """Ubah path relatif di config menjadi path absolut dari root proyek."""
    return ROOT / cfg["paths"][key]
