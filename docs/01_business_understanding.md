# Business Understanding (ringkasan)

## Masalah
1. Promosi massal kurang efisien karena perilaku belanja beragam.
2. Pelanggan bernilai tinggi dan pelanggan berisiko berhenti belum dapat dibedakan.
3. Belum ada segmentasi berbasis data untuk menyusun strategi promosi.

**Pertanyaan riset:** seberapa baik K-Means membentuk segmen yang terpisah jelas berdasarkan R, F, M, dan seberapa jelas
tiap segmen dapat diterjemahkan menjadi rekomendasi promosi yang berbeda.

## Tujuan SMART
| Aspek | Rumusan |
|---|---|
| Specific | Kelompokkan pelanggan berdasarkan R, F, M dengan K-Means, susun profil dan rekomendasi promosi tiap segmen |
| Measurable | Silhouette >= 0,4; Davies-Bouldin < 1,0; k = 3-6; setiap cluster >= 5% pelanggan |
| Achievable | Dataset publik, K-Means ringan, Python (pandas, scikit-learn) |
| Relevant | Promosi tepat sasaran dan anggaran lebih efisien |
| Time-bound | BU dan DU selesai saat UTS; sisanya fase berikutnya |

## Metrik keberhasilan
Silhouette, Davies-Bouldin, elbow (inertia), stabilitas antar seed (Adjusted Rand Index), interpretabilitas bisnis
(profil R, F, M dan kontribusi pendapatan).

## Contoh segmen dan strategi
| Segmen | Karakteristik | Strategi |
|---|---|---|
| Champions | Recency rendah, F dan M tinggi | Program loyalitas, akses awal produk baru |
| Loyal | Sering belanja, nilai sedang | Upselling, cross-selling, bundling |
| Potential / New | Baru belanja, masih jarang | Voucher selamat datang, edukasi produk |
| At Risk | Dulu aktif, lama tidak belanja | Win-back dengan diskon personal |
| Lost | Recency tinggi, F dan M rendah | Reaktivasi berbiaya rendah (email) |

Nama dan jumlah segmen final ditentukan dari hasil clustering.

## Asumsi
1. Satu CustomerID = satu pelanggan. 2. Sampel acak cukup mewakili. 3. Perilaku lampau mencerminkan masa depan.
4. Monetary = Quantity x UnitPrice. 5. Pembatalan (InvoiceNo berawalan C) dan nilai tidak valid dikeluarkan.

## Batasan
Satu retailer UK (banyak pembeli grosir), periode sekitar 1 tahun, transaksi tanpa CustomerID tidak terpakai,
tidak ada data demografi/biaya/respons promosi, K-Means sensitif outlier dan skala, tidak mencakup churn,
rekomendasi produk, deployment, dan A/B test.
