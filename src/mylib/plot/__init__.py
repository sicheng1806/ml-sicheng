"""Drawing interface"""

import matplotlib.pyplot as plt
from pathlib import Path

__all__ = ["set_rcParams", "post_plot"]

rc_keys = [k.split(".")[-1] for k in plt.rcParams.keys()]


def set_rcParams(rc_params={}, **kwargs):
    kwargs |= rc_params
    for k, v in kwargs.items():
        if "." in k:
            plt.rcParams[k] = v
        k = list(plt.rcParams.keys())[rc_keys.index(k)]
        plt.rcParams[k] = v


def post_plot(**kwargs):
    save = kwargs.pop("save", False)
    img_dir = kwargs.pop("img_dir", None)
    show = kwargs.pop("show", True)
    if save and img_dir is not None:
        img_dir = Path(img_dir)
        if not img_dir.exists():
            img_dir.mkdir()
        title = plt.gcf().get_suptitle()
        if not title:
            title = plt.gca().get_title()
        if title:
            plt.savefig(img_dir / f"{title}.png")
    if show:
        plt.show()
