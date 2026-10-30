# Risiko dan Etika

| Risiko | Mitigasi |
|---|---|
| Bias data (satu retailer, banyak grosir) | Dokumentasikan keterbatasan, jangan generalisasi ke seluruh e-commerce |
| Bias sampling | Sampling per CustomerID, seed tetap, bandingkan distribusi |
| Outlier F dan M | Transformasi log, StandardScaler |
| Data kotor | Aturan pembersihan di Data Preparation |
| Privasi dan legal | CustomerID anonim, lisensi CC BY 4.0 dicantumkan, mengikuti prinsip UU PDP (UU No. 27 Tahun 2022) |
| Perlakuan tidak adil antar segmen | Segmentasi hanya untuk strategi promosi, bukan pembedaan harga atau layanan |
| Salah interpretasi cluster | Validasi dengan metrik dan profiling R, F, M |
