"""Drawing interface"""

import matplotlib.pyplot as plt
from pathlib import Path
from mylib.kaggle import iskaggle

__all__ = ["post_plot"]


def post_plot(**kwargs):
    save = kwargs.pop("save", False)
    img_dir = kwargs.pop("img_dir", None)
    show = kwargs.pop("show", True)
    if save and img_dir is not None:
        img_dir = Path(img_dir)
        if not img_dir.exists():
            img_dir.mkdir()
        # matplotlib version diff 
        if not iskaggle():
            title = plt.gcf().get_suptitle()
        else:
            title = plt.gcf()._suptitle 
            if title is not None:
                title = title.get_text()
        if not title:
            title = plt.gca().get_title()
        if title:
            plt.savefig(img_dir / f"{title}.png")
    if show:
        plt.show()
