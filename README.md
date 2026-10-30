# Segmentasi Pelanggan E-Commerce dengan RFM dan K-Means

Proyek UTS **Data Science** - Program Studi Informatika, UPN "Veteran" Yogyakarta (2026).
Dosen pengampu: Dhimas Arief Dharmawan.

**Tim**
1. Wildan Rifqi Prambudi (123240060)
2. Muhammad Fariel Zaky Faheza (123240077)
3. Shafiq Shidqi Azizi (123240085)
4. Davi Ergana Kembaren (123240086)

## Ringkasan
Pelanggan toko online dikelompokkan berdasarkan **Recency, Frequency, Monetary (RFM)** memakai **K-Means**,
lalu tiap segmen diberi rekomendasi strategi promosi. Dataset: *Online Retail* (UCI, CC BY 4.0),
transaksi 1 Des 2010 - 9 Des 2011, 541.909 baris.

Target (SMART): Silhouette >= 0,4, Davies-Bouldin < 1,0, k = 3-6, setiap cluster >= 5% pelanggan.

## Fase CRISP-DM
| Fase | Lokasi | Status |
|---|---|---|
| Business Understanding | `docs/01_business_understanding.md` | UTS |
| Data Understanding | `notebooks/01_data_understanding.ipynb` | UTS |
| Data Preparation | `notebooks/02_data_preparation.ipynb`, `src/rfm_kmeans/` | Fase berikutnya |
| Modeling | `notebooks/03_modeling.ipynb` | Fase berikutnya |
| Evaluation | `notebooks/04_evaluation.ipynb` | Fase berikutnya |

## Struktur Repositori
```
rfm-kmeans/
├── configs/config.yaml        seed, path, parameter
├── data/
│   ├── raw/                   berkas asli UCI (tidak di-commit)
│   ├── processed/             data bersih, RFM, hasil cluster
│   └── external/              data pendukung (bila ada)
├── docs/                      business understanding, data dictionary, etika, panduan
├── models/                    model tersimpan
├── notebooks/                 01 sampai 04 (CRISP-DM)
├── reports/
│   ├── figures/               grafik EDA dan hasil
│   └── tables/                tabel hasil (profil segmen, metrik)
├── scripts/                   download data, jalankan pipeline, data sintetis
├── src/rfm_kmeans/            kode pipeline (modul per tahap)
├── tests/                     unit test (pytest)
├── requirements.txt
└── Makefile
```

## Cara Menjalankan
```bash
# 1. Siapkan environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 2. Unduh data (dari UCI)
python scripts/download_data.py

# 3. Eksplorasi data
jupyter notebook notebooks/01_data_understanding.ipynb

# 4. Jalankan seluruh pipeline
python scripts/run_pipeline.py          # atau: --k 4 untuk memaksa jumlah cluster

# 5. Tes
pytest -q
```
Uji cepat tanpa unduh data: `python scripts/make_synthetic_data.py` (data sintetis, bukan data asli).

## Reprodusibilitas
- Seed tetap **42** pada sampling dan inisialisasi K-Means (`configs/config.yaml`).
- Versi pustaka dicatat di `requirements.txt`.
- Semua grafik EDA dihasilkan dari `notebooks/01_data_understanding.ipynb`.

## Lisensi
Kode: MIT (`LICENSE`). Data: CC BY 4.0 (`DATA_LICENSE.md`).
