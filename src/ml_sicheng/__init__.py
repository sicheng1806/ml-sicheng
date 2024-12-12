import logging

from .plot import post_plot
from .kaggle import kaggle_datasets, iskaggle

__version__ =  "0.1.2"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

_submodules = ["plot", "transformer", "kaggle", "new_energy_plant"]

__all__ = ["post_plot", "kaggle_datasets", "iskaggle"]

__all__ += _submodules