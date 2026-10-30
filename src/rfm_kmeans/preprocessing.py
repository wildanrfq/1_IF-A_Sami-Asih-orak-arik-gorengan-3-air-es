"""Transformasi log dan standarisasi fitur RFM sebelum K-Means."""
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

FEATURES = ["Recency", "Frequency", "Monetary"]


def transform_rfm(rfm, log_transform=True):
    """Kembalikan (X_scaled DataFrame, scaler). Index = CustomerID."""
    X = rfm[FEATURES].astype(float)
    if log_transform:
        X = np.log1p(X)
    scaler = StandardScaler()
    X_scaled = pd.DataFrame(
        scaler.fit_transform(X), columns=FEATURES, index=rfm["CustomerID"].values
    )
    return X_scaled, scaler
