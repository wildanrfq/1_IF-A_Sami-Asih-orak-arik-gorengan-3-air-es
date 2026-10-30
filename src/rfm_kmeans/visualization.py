"""Fungsi grafik untuk EDA dan hasil clustering."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA


def _save(fig, path):
    if path:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=150, bbox_inches="tight")
    return fig


def plot_monthly_transactions(df, path=None):
    monthly = df.groupby(df["InvoiceDate"].dt.to_period("M"))["InvoiceNo"].nunique()
    fig, ax = plt.subplots(figsize=(9, 4))
    monthly.plot(ax=ax, marker="o")
    ax.set(title="Jumlah transaksi per bulan", xlabel="Bulan", ylabel="Jumlah invoice")
    return _save(fig, path)


def plot_rfm_distribution(rfm, path=None):
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
    for ax, col in zip(axes, ["Recency", "Frequency", "Monetary"]):
        sns.histplot(rfm[col], bins=40, ax=ax)
        ax.set_title(f"Distribusi {col}")
    return _save(fig, path)


def plot_rfm_correlation(rfm, path=None):
    fig, ax = plt.subplots(figsize=(4.5, 4))
    sns.heatmap(rfm[["Recency", "Frequency", "Monetary"]].corr(), annot=True,
                cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
    ax.set_title("Korelasi fitur RFM")
    return _save(fig, path)


def plot_k_selection(scan, path=None):
    fig, axes = plt.subplots(1, 3, figsize=(14, 3.8))
    axes[0].plot(scan["k"], scan["inertia"], marker="o")
    axes[0].set(title="Elbow (inertia)", xlabel="k")
    axes[1].plot(scan["k"], scan["silhouette"], marker="o", color="green")
    axes[1].set(title="Silhouette Score", xlabel="k")
    axes[2].plot(scan["k"], scan["davies_bouldin"], marker="o", color="red")
    axes[2].set(title="Davies-Bouldin Index", xlabel="k")
    return _save(fig, path)


def plot_clusters_pca(X, labels, path=None):
    comp = PCA(n_components=2, random_state=42).fit_transform(X)
    fig, ax = plt.subplots(figsize=(6.5, 5))
    sns.scatterplot(x=comp[:, 0], y=comp[:, 1], hue=labels, palette="tab10", s=18, ax=ax)
    ax.set(title="Cluster pada ruang PCA 2D", xlabel="PC1", ylabel="PC2")
    return _save(fig, path)


def plot_segment_summary(prof, path=None):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    prof["Pelanggan_%"].plot(kind="bar", ax=axes[0], title="Proporsi pelanggan (%)")
    prof["Pendapatan_%"].plot(kind="bar", ax=axes[1], color="orange",
                              title="Kontribusi pendapatan (%)")
    return _save(fig, path)
