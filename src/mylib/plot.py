'''绘图接口'''

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from pathlib import Path
import os

IMG_DIR = os.environ.get("IMG_DIR",Path("./output/imgs"))

def pre_plot(**kwargs):
    '''创建fig和ax'''
    kw_list = ['nrows','ncols','sharex','sharey','squeeze','width_ratios','height_ratios','subplot_kw','gridspec_kw','figsize','num','dpi']
    default_kwargs = dict(zip(kw_list,[1,1]+[None]*(len(kw_list)-2)))
    keys = set(kwargs.keys()).intersection(kw_list)
    for k in keys:
        default_kwargs[k] = kwargs.pop(k)
    fig,ax = plt.subplots(**default_kwargs)
    kwargs['fig'] = fig
    kwargs['ax'] = ax
    return kwargs
    

def post_plot(**kwargs):
    title = kwargs.pop("title",None)
    save = kwargs.pop("save",False)
    img_dir = kwargs.pop("img_dir",IMG_DIR)
    ax = kwargs.pop('ax')
    legend = kwargs.pop("legend",False)
    show = kwargs.pop("show",True)
    if legend: plt.legend()
    if title is not None:
        if not isinstance(ax,Axes):
            ax.flat[0].set_title(title)
        else:
            plt.title(title)
        if save:
            if not img_dir.exists(): img_dir.mkdir()
            plt.savefig(img_dir / f"{title}.png")
            return 
    if show:
        plt.show()

