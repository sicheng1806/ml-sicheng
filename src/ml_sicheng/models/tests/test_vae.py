import os

os.environ["KERAS_BACKEND"] = "jax"

import keras

from ml_sicheng.models.vae import VariationalAutoEncoder


def test_vae():
    (x_train, _), _ = keras.datasets.mnist.load_data()
    x_train = x_train[:600].reshape(600, 784).astype("float32") / 255

    original_dim = 784
    vae = VariationalAutoEncoder(original_dim, 64, 32)

    optimizer = keras.optimizers.Adam(learning_rate=1e-1)
    vae.compile(optimizer, loss=keras.losses.MeanSquaredError())

    vae.fit(x_train, x_train, epochs=2, batch_size=64)
