import keras
from keras import layers


def SimpleLSTMRegression(
    input_shape,
    units,
    window_post=1,
    dropout_rate=0.2,
    name="lstm-regression",
    **kwargs,
):
    return keras.Sequential(
        [
            keras.Input(shape=input_shape),
            layers.LSTM(units, return_sequences=True),
            layers.Dropout(dropout_rate),
            layers.LSTM(units),
            layers.Dense(window_post),
        ],
        name=name,
        **kwargs,
    )
