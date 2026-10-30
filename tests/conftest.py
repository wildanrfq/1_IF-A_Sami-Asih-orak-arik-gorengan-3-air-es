import sys
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))


@pytest.fixture
def raw_df():
    from make_synthetic_data import make
    return make(n_customers=200, seed=7)


@pytest.fixture
def cleaning_cfg():
    return {
        "drop_missing_customer": True, "drop_duplicates": True,
        "drop_cancellations": True, "drop_invalid_values": True,
        "drop_non_product": True, "non_product_codes": ["POST", "D", "M"],
    }


@pytest.fixture
def small_tx():
    return pd.DataFrame({
        "InvoiceNo": ["1", "2", "3", "3"],
        "StockCode": ["A", "A", "B", "C"],
        "Description": ["x"] * 4,
        "Quantity": [2, 1, 3, 1],
        "InvoiceDate": pd.to_datetime(["2011-01-01", "2011-01-10", "2011-01-05", "2011-01-05"]),
        "UnitPrice": [10.0, 5.0, 2.0, 4.0],
        "CustomerID": [1, 1, 2, 2],
        "Country": ["UK"] * 4,
    })
