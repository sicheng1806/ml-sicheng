import matplotlib.pyplot as plt
from pathlib import Path
import pytest
import shutil

from ml_sicheng.plot import post_plot
from ml_sicheng import iskaggle


IMG_DIR = (
    Path("output/imgs/tests") if not iskaggle() else Path("/kaggle/working/imgs/tests")
)
IMG_DIR.mkdir(exist_ok=True, parents=True)
kwargs = dict(img_dir=IMG_DIR, save=True, show=False)


@pytest.fixture(scope="function")
def setup_environ():
    plt.rcdefaults()
    shutil.rmtree(IMG_DIR, ignore_errors=True)


def test_post_plot(setup_environ):
    plt.plot([1, 3, 4, 5])
    plt.title("test-post-plot")
    post_plot(**kwargs)
    assert (IMG_DIR / "test-post-plot.png").exists()
