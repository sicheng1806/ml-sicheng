import logging

from .plot import post_plot, set_rcParams
from .datasets import (
    load_dataset,
    DataSet,
    dump_datasets,
    is_datasets_exists,
    DataSetNotAlreadyError,
)
from .transformer import KTransformer


__version__ = "0.1.0"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

_submodules = ["plot", "datasets", "transformer"]

__all__ = [
    "post_plot",
    "set_rcParams",
    "load_dataset",
    "DataSet",
    "KTransformer",
    "is_datasets_exists",
    "dump_datasets",
    "list_environs",
]

__all__ += _submodules


def list_environs():
    return ("MYLIB_DATASETS_DIR",)


if not is_datasets_exists():
    logger.warning(DataSetNotAlreadyError.__doc__)
