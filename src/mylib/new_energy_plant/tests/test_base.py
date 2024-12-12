import pytest
import numpy as np
from mylib.new_energy_plant.transformer import KTransformer, EventClassifier
from mylib.new_energy_plant.dataset import DataSet


def test_dataset():
    for ds in DataSet:
        df = ds.load_dataframe()
        assert (df.columns == ["value"]).all()
        df = ds.load_full_dataframe()
        assert len(df.columns) > 2


@pytest.mark.parametrize("to_nan", [None, 0])
def test_k_transformer(to_nan):
    X = [1, 2, 0, 4, 5]

    k = KTransformer(window=2, to_nan=to_nan).transform(X)
    k[np.isnan(k)] = 0
    k_val = [0, 1 / 3, -1, 1, 1 / 9] if to_nan is None else [0, 1 / 3, 0, 0, 1 / 9]
    assert np.isclose(k, k_val).all()
    assert X == [1, 2, 0, 4, 5]


def test_event_transformer():
    k = [1, 0, 1.1, 2, 3, -1, -2]
    t = 1.1

    event = EventClassifier(t=t).transform(k)
    assert np.isclose(event, [0, 0, 0, 1, 1, 0, -1]).all()
