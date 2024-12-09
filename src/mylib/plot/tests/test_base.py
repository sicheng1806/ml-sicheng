import matplotlib.pyplot as plt
from pathlib import Path
import pytest
import shutil

from mylib.plot import set_rcParams, post_plot


IMG_DIR = Path("output/imgs/tests")
kwargs = dict(img_dir=IMG_DIR, save=True, show=False)


@pytest.fixture(scope="function")
def setup_environ():
    plt.rcdefaults()
    shutil.rmtree(IMG_DIR, ignore_errors=True)


def test_set_rcParams(setup_environ):
    set_rcParams(figsize=(30, 8))
    assert plt.rcParams["figure.figsize"] == [30, 8]


def test_post_plot(setup_environ):
    plt.plot([1, 3, 4, 5])
    plt.title("test-post-plot")
    post_plot(**kwargs)
    assert (IMG_DIR / "test-post-plot.png").exists()
