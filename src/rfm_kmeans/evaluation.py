"""Evaluasi cluster: metrik, target SMART, dan stabilitas antar seed."""
import numpy as np
import pandas as pd
from sklearn.metrics import adjusted_rand_score, davies_bouldin_score, silhouette_score

from .modeling import fit_kmeans


def cluster_metrics(X, labels):
    return {
        "silhouette": float(silhouette_score(X, labels)),
        "davies_bouldin": float(davies_bouldin_score(X, labels)),
    }


def check_smart_targets(X, labels, cfg_eval, k_range=(3, 6)):
    """Cek target pada tujuan SMART. Kembalikan DataFrame ringkas."""
    m = cluster_metrics(X, labels)
    sizes = pd.Series(labels).value_counts(normalize=True) * 100
    k = len(sizes)
    checks = [
        ("Silhouette >= %.2f" % cfg_eval["min_silhouette"], m["silhouette"],
         m["silhouette"] >= cfg_eval["min_silhouette"]),
        ("Davies-Bouldin < %.2f" % cfg_eval["max_davies_bouldin"], m["davies_bouldin"],
         m["davies_bouldin"] < cfg_eval["max_davies_bouldin"]),
        ("Jumlah cluster %d-%d" % k_range, k, k_range[0] <= k <= k_range[1]),
        ("Cluster terkecil >= %.0f%%" % cfg_eval["min_cluster_pct"], round(sizes.min(), 2),
         sizes.min() >= cfg_eval["min_cluster_pct"]),
    ]
    return pd.DataFrame(checks, columns=["Target", "Nilai", "Tercapai"])


def stability_ari(X, k, seeds, n_init=10):
    """ARI rata-rata antar pasangan seed (1.0 = identik)."""
    all_labels = [fit_kmeans(X, k, seed=s, n_init=n_init).labels_ for s in seeds]
    scores = []
    for i in range(len(all_labels)):
        for j in range(i + 1, len(all_labels)):
            scores.append(adjusted_rand_score(all_labels[i], all_labels[j]))
    return {"ari_mean": float(np.mean(scores)), "ari_min": float(np.min(scores))}
