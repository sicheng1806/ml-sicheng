import pytest
import numpy as np
from importlib import resources
from pathlib import Path
import os


from mylib.datasets import (
    DataSet,
    load_dataset,
    load_full_dataset,
    dump_datasets,
    is_datasets_exists,
    get_datasets_dir,
    DATA_MODULE,
    _get_datasets_dir,
)

TEST_DATASETS_DIR = Path("dataset/data")


@pytest.fixture(scope="function")
def setup_environ():
    os.environ["MYLIB_DATASETS_DIR"] = str(TEST_DATASETS_DIR)
    if not is_datasets_exists():
        dump_datasets(TEST_DATASETS_DIR)

@pytest.mark.parametrize("data_dir", [None, TEST_DATASETS_DIR])
@pytest.mark.parametrize("ds", [ds for ds in DataSet])
def test_load_dataset(ds, data_dir, setup_environ):
    if data_dir is not None:
        if not is_datasets_exists(data_dir):
            pytest.skip()
        os.environ["MYLIB_DATASETS_DIR"] = str(TEST_DATASETS_DIR)
    df = load_dataset(ds)
    assert (df.columns == ["value"]).all()
    assert not df.loc[:, "value"].isna().any()
    df = ds.load_dataset()
    assert (df.columns == ["value"]).all()
    assert not df.loc[:, "value"].isna().any()


@pytest.mark.parametrize("data_dir", [None, TEST_DATASETS_DIR])
@pytest.mark.parametrize("ds", [ds for ds in DataSet])
def test_load_full_dataset(ds, data_dir, setup_environ):
    if data_dir is not None:
        if not is_datasets_exists(data_dir):
            pytest.skip()
        os.environ["MYLIB_DATASETS_DIR"] = str(TEST_DATASETS_DIR)
    df = load_full_dataset(ds)
    assert not np.isnan(df.to_numpy()).any()


def test_dump_dataset_and_exists(setup_environ):
    my_dataset = Path("dataset") / "data"
    if not (
        [f.name for f in my_dataset.glob("*.csv.gz")]
        == ["W1_velocity.csv.gz", "S1.csv.gz", "W1_power.csv.gz"]
    ):
        pytest.skip(
            "Not enough test data: W1_velocity.csv.gz, S1.csv.gz, W1_power.csv.gz"
        )
    # 删除data模块中的数据
    data_model = "mylib.datasets.data"
    data_files = Path(resources.files(data_model)).glob("*.csv.gz")
    for ds in data_files:
        ds.unlink(missing_ok=True)
    assert not is_datasets_exists()
    # 载入数据
    dump_datasets(my_dataset)
    for ds in data_files:
        assert ds.exists()
    assert is_datasets_exists()


@pytest.mark.skip
def test_dump_csv_dataset():
    my_dataset = Path("dataset") / "data"
    if not (
        [f.name for f in my_dataset.glob("*.csv")]
        == ["W1_velocity.csv", "S1.csv", "W1_power.csv"]
    ):
        pytest.skip(
            "Not enough test data: W1_velocity.csv.gz, S1.csv.gz, W1_power.csv.gz"
        )
    # 删除data模块中的数据
    data_model = "mylib.datasets.data"
    data_files = Path(resources.files(data_model)).glob("*.csv.gz")
    for ds in data_files:
        ds.unlink(missing_ok=True)
    assert not is_datasets_exists()
    # 载入数据
    dump_datasets(my_dataset)
    for ds in data_files:
        assert ds.exists()
    assert is_datasets_exists()


def test_get_datasets_dir():
    os.environ["MYLIB_DATASETS_DIR"] = ""
    assert _get_datasets_dir().samefile(resources.files(DATA_MODULE))
    assert is_datasets_exists()
    assert get_datasets_dir().samefile(resources.files(DATA_MODULE))
    if is_datasets_exists(TEST_DATASETS_DIR):
        os.environ["MYLIB_DATASETS_DIR"] = str(TEST_DATASETS_DIR.resolve())
        assert get_datasets_dir().samefile(TEST_DATASETS_DIR)

