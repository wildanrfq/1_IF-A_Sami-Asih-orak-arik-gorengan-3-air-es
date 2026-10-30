"""Pembersihan data sesuai aturan pada laporan (Data Preparation)."""


def flag_non_product(df, codes):
    """Tandai baris non-produk (ongkir, biaya bank, penyesuaian, dst.)."""
    codes_upper = {c.upper() for c in codes}
    return df["StockCode"].astype(str).str.upper().isin(codes_upper)


def clean_transactions(df, cfg_cleaning):
    """Bersihkan data dan kembalikan (df_bersih, log_pembersihan)."""
    log = {"awal": len(df)}
    data = df.copy()

    if cfg_cleaning.get("drop_missing_customer", True):
        data = data.dropna(subset=["CustomerID"])
        log["setelah_hapus_CustomerID_kosong"] = len(data)

    if cfg_cleaning.get("drop_duplicates", True):
        data = data.drop_duplicates()
        log["setelah_hapus_duplikat"] = len(data)

    if cfg_cleaning.get("drop_cancellations", True):
        is_cancel = data["InvoiceNo"].astype(str).str.upper().str.startswith("C")
        data = data[~is_cancel]
        log["setelah_hapus_pembatalan"] = len(data)

    if cfg_cleaning.get("drop_invalid_values", True):
        data = data[(data["Quantity"] > 0) & (data["UnitPrice"] > 0)]
        log["setelah_hapus_nilai_tidak_valid"] = len(data)

    if cfg_cleaning.get("drop_non_product", True):
        mask = flag_non_product(data, cfg_cleaning.get("non_product_codes", []))
        data = data[~mask]
        log["setelah_hapus_non_produk"] = len(data)

    data = data.copy()
    data["CustomerID"] = data["CustomerID"].astype(int)
    log["akhir"] = len(data)
    log["persen_tersisa"] = round(100 * len(data) / max(log["awal"], 1), 2)
    return data, log
