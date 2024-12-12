from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np


class KTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, window, *, to_nan=None):
        self.window = window
        self.to_nan = float(to_nan) if to_nan is not None else None

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        window = self.window
        to_nan = self.to_nan

        ts = pd.Series(X).copy()
        if to_nan is not None:
            ts[ts == to_nan] = np.nan
        q = ts.rolling(window).mean()
        return ts / q - 1


class EventClassifier(BaseEstimator, TransformerMixin):
    def __init__(self, t):
        self.t = t

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = np.array(X)
        return np.where(X > self.t, 1, np.where(X < -self.t, -1, 0))
