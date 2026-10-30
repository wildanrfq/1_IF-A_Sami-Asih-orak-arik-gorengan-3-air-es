"""Profil segmen dan rekomendasi strategi promosi."""
import pandas as pd

PROMO_STRATEGY = {
    "Champions": "Program loyalitas, akses awal produk baru",
    "Loyal": "Upselling, cross-selling, dan bundling",
    "Potential / New": "Voucher selamat datang, edukasi produk",
    "At Risk": "Kampanye win-back dengan diskon personal",
    "Lost": "Reaktivasi berbiaya rendah, misalnya email",
}


def profile_segments(rfm, labels):
    """Ringkasan R, F, M, jumlah pelanggan, dan kontribusi pendapatan per cluster."""
    data = rfm.copy()
    data["Cluster"] = labels
    prof = data.groupby("Cluster").agg(
        Pelanggan=("CustomerID", "count"),
        Recency_mean=("Recency", "mean"),
        Frequency_mean=("Frequency", "mean"),
        Monetary_mean=("Monetary", "mean"),
        Monetary_total=("Monetary", "sum"),
    )
    prof["Pelanggan_%"] = 100 * prof["Pelanggan"] / prof["Pelanggan"].sum()
    prof["Pendapatan_%"] = 100 * prof["Monetary_total"] / prof["Monetary_total"].sum()
    return prof.round(2)


def suggest_label(prof):
    """Usulan nama segmen berbasis aturan sederhana (cek ulang secara manual).

    Aturan: bandingkan R, F, M tiap cluster dengan rata-rata keseluruhan.
    """
    r_all = (prof["Recency_mean"] * prof["Pelanggan"]).sum() / prof["Pelanggan"].sum()
    f_all = (prof["Frequency_mean"] * prof["Pelanggan"]).sum() / prof["Pelanggan"].sum()
    labels = {}
    for cl, row in prof.iterrows():
        recent = row["Recency_mean"] <= r_all
        frequent = row["Frequency_mean"] >= f_all
        if recent and frequent:
            labels[cl] = "Champions" if row["Frequency_mean"] > 2 * f_all else "Loyal"
        elif recent and not frequent:
            labels[cl] = "Potential / New"
        elif not recent and frequent:
            labels[cl] = "At Risk"
        else:
            labels[cl] = "Lost"
    return labels


def add_segment_names(rfm, labels, mapping):
    out = rfm.copy()
    out["Cluster"] = labels
    out["Segmen"] = out["Cluster"].map(mapping)
    out["Strategi"] = out["Segmen"].map(PROMO_STRATEGY)
    return out
