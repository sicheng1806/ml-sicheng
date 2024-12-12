import pandas as pd

from ml_sicheng.kaggle import kaggle_datasets

handles = ["uciml/iris", "competitions/store-sales-time-series-forecasting"]


def test_kaggle_datasets():
    iris = pd.read_csv(
        kaggle_datasets(handles[0]) / "Iris.csv",
        index_col=0,
    )
    assert (
        iris.columns
        == ["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]
    ).all()
    stores = pd.read_csv(kaggle_datasets(handles[1]) / "stores.csv")
    assert (stores.columns == ["store_nbr", "city", "state", "type", "cluster"]).all()
