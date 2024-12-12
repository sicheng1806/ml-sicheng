import os

os.environ["KERAS_BACKEND"] = "jax"
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

from mylib.models.lstm import SimpleLSTMRegression


def test_simple_LSTM_regression():
    N = 1000
    ts = np.random.randn(N)
    windows = (20, 1)
    data = sliding_window_view(ts, window_shape=windows[0] + windows[1])
    X, y = data[:, : windows[0]], data[:, windows[1]]
    X = X.reshape((X.shape[0], windows[0], -1))
    lstm = SimpleLSTMRegression(
        input_shape=X.shape[1:],
        units=24,
    )
    lstm.compile(optimizer="adam", loss="mean_squared_error")
    _ = lstm.fit(X, y, verbose=0, epochs=1, batch_size=64)
