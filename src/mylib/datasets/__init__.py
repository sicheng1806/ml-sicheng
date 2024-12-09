"""Utilities to load datasets"""

import enum
from importlib import resources
import pandas as pd
from pathlib import Path
import shutil
import logging
import gzip
import os

logger = logging.getLogger(__name__)

__all__ = [
    "DataSet",
    "load_dataset",
    "load_full_dataset",
    "dump_datasets",
    "is_datasets_exists",
    "DataSetNotAlreadyError",
    "get_datasets_dir",
]

DATA_MODULE = "mylib.datasets.data"


class DataSetNotAlreadyError(Exception):
    """Datasets is not already, set environ variable MYLIB_DATASETS_DIR or use dump_datasets(your_dataset_dir) to load it"""


class DataSet(enum.Enum):
    Solar = "S1"
    WindPower = "W1_power"
    WindVelocity = "W1_velocity"

    def load_dataset(self):
        return load_dataset(self)


def _get_datasets_dir() -> Path:
    datasets_dir = os.environ.get("MYLIB_DATASETS_DIR")
    if datasets_dir:
        datasets_dir = Path(datasets_dir)
    if (not datasets_dir) or (not datasets_dir.exists()):
        datasets_dir = Path(resources.files(DATA_MODULE))
    return datasets_dir


def is_datasets_exists(data_dir=None):
    datasets_dir = _get_datasets_dir() if data_dir is None else data_dir
    for ds in DataSet:
        if not list(datasets_dir.glob(f"{ds.value}.csv*")):
            return False
    return True


def get_datasets_dir() -> Path:
    if not is_datasets_exists():
        raise DataSetNotAlreadyError
    return _get_datasets_dir()


def load_full_dataset(ds: DataSet) -> pd.DataFrame:
    if not isinstance(ds, DataSet):
        raise TypeError(f"{ds} must be DataSet member")
    datadir = get_datasets_dir()
    file_names = [f.name for f in datadir.glob(f"{ds.value}.csv*")]
    if f"{ds.value}.csv.gz" in file_names:
        return pd.read_csv(
            datadir / f"{ds.value}.csv.gz", compression="gzip", index_col=0
        )
    else:
        return pd.read_csv(list(datadir.glob(f"{ds.value}.csv*"))[0], index_col=0)


def load_dataset(ds: DataSet) -> pd.DataFrame:
    df = load_full_dataset(ds)
    _df = pd.DataFrame(df.T.mean(), columns=["value"])
    return _df


def dump_datasets(dataset_dir):
    dataset_dir = Path(dataset_dir)
    if not dataset_dir.exists():
        raise ValueError(f"{dataset_dir.absolute()} is not exists!")
    target_dir = resources.files(DATA_MODULE)
    for ds in DataSet:
        fname = dataset_dir / f"{ds.value}.csv.gz"
        is_gzip = True
        if not fname.exists():
            fname = dataset_dir / f"{ds.value}.csv"
            is_gzip = False
            if not fname.exists():
                raise FileNotFoundError(fname)
        if is_gzip:
            shutil.copyfile(fname, target_dir / fname.name)
        else:
            with open(fname, "rb") as csv_file:
                csv_data = csv_file.read()
            with gzip.open(target_dir / f"{fname.name}.gz", "wb") as gzip_file:
                gzip_file.write(csv_data)
        print(f"uploaded {fname.name}")
