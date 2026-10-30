# Rencana Kualitas Data

| Pemeriksaan | Cara | Penanganan | Kode |
|---|---|---|---|
| Missing value | Hitung nilai kosong per kolom | Hapus baris tanpa CustomerID | `cleaning.py` |
| Duplikasi | Baris identik pada semua kolom | Hapus | `cleaning.py` |
| Pembatalan | InvoiceNo berawalan C | Keluarkan dari RFM | `cleaning.py` |
| Nilai tidak valid | Quantity atau UnitPrice <= 0 | Hapus | `cleaning.py` |
| Outlier | Boxplot dan IQR | Tidak dihapus; transformasi log + standarisasi | `preprocessing.py` |
| Kode non-produk | POST, D, M, BANK CHARGES, dst. | Tandai, cek manual, lalu keluarkan | `cleaning.py` |
| Representasi sampel | Bandingkan sampel vs data penuh | Ulang sampling bila menyimpang | `sampling.py` |

Sampling dilakukan **per CustomerID** agar riwayat pelanggan tidak terpotong.
