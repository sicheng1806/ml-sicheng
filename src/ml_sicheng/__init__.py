import logging

from .plot import post_plot
from .kaggle import kaggle_datasets, iskaggle
from .__about__ import __version__

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

_submodules = ["plot", "transformer", "kaggle", "new_energy_plant"]

__all__ = ["__version__", "post_plot", "kaggle_datasets", "iskaggle"]

__all__ += _submodules
