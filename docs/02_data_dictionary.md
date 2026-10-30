# Data Dictionary

## Tabel transaksi (Online Retail.xlsx) - 541.909 baris, 8 variabel
| Variabel | Tipe | Unit | Keterangan |
|---|---|---|---|
| InvoiceNo | Kategorikal | ID | Nomor faktur 6 digit; awalan C = pembatalan |
| StockCode | Kategorikal | ID | Kode produk 5 digit |
| Description | Kategorikal | teks | Nama produk |
| Quantity | Integer | unit | Jumlah produk per transaksi |
| InvoiceDate | Tanggal | tanggal dan jam | Waktu transaksi dibuat |
| UnitPrice | Kontinu | poundsterling | Harga per unit |
| CustomerID | Kategorikal | ID | Nomor pelanggan 5 digit |
| Country | Kategorikal | teks | Negara pelanggan |

## Fitur turunan RFM
| Fitur | Tipe | Unit | Pembentukan |
|---|---|---|---|
| Recency | Integer | hari | Tanggal acuan (transaksi terakhir + 1 hari) dikurangi transaksi terakhir pelanggan |
| Frequency | Integer | transaksi | Jumlah InvoiceNo unik per CustomerID |
| Monetary | Kontinu | poundsterling | Total Quantity x UnitPrice per CustomerID |

Implementasi: `src/rfm_kmeans/features.py`.
