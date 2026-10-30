"""Jalankan seluruh pipeline.  Contoh: python scripts/run_pipeline.py --k 4"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from rfm_kmeans import pipeline  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description="Pipeline segmentasi RFM + K-Means")
    parser.add_argument("--config", default="configs/config.yaml")
    parser.add_argument("--k", type=int, default=None, help="paksa jumlah cluster")
    args = parser.parse_args()
    pipeline.run(args.config, k=args.k)


if __name__ == "__main__":
    main()
