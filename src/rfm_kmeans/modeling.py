"""K-Means dan pencarian jumlah cluster (k)."""
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import davies_bouldin_score, silhouette_score


def fit_kmeans(X, k, seed=42, n_init=10, max_iter=300):
    """Latih K-Means dan kembalikan model."""
    model = KMeans(n_clusters=k, random_state=seed, n_init=n_init, max_iter=max_iter)
    model.fit(X)
    return model


def scan_k(X, k_min=2, k_max=10, seed=42, n_init=10):
    """Hitung inertia, silhouette, dan Davies-Bouldin untuk setiap k."""
    rows = []
    for k in range(k_min, k_max + 1):
        model = fit_kmeans(X, k, seed=seed, n_init=n_init)
        rows.append({
            "k": k,
            "inertia": model.inertia_,
            "silhouette": silhouette_score(X, model.labels_),
            "davies_bouldin": davies_bouldin_score(X, model.labels_),
        })
    return pd.DataFrame(rows)


def choose_k(scan, candidates=(3, 4, 5, 6)):
    """Pilih k dari kandidat dengan silhouette tertinggi."""
    sub = scan[scan["k"].isin(candidates)]
    return int(sub.loc[sub["silhouette"].idxmax(), "k"])
