from pathlib import Path

import pandas as pd
import numpy as np

DATASET_DIR = Path("dataset")
TARGET_DIR = Path("src/mylib/datasets/data")
if not (DATASET_DIR / "csv").exists():
    raise FileNotFoundError("请准备好数据集后再尝试运行")


def tidy_dataset(df: pd.DataFrame, name):
    """清洗数据集:索引、Nan值补全"""
    # 索引处理
    if len(df) == df.index[-1] - df.index[0] + 1:
        df.index = np.arange(df.index[0], df.index[-1] + 1)
    else:
        df = pd.DataFrame(df, index=np.arange(df.index[0], df.index[-1]))
    df[df.isna()] = 0
    tidy_dir = TARGET_DIR
    if not tidy_dir.exists():
        tidy_dir.mkdir()
    df.to_csv(tidy_dir / f"{name}.csv.gz", compression="gzip")


if __name__ == "__main__":
    for name in ["S1", "W1_power", "W1_velocity"]:
        df = pd.read_csv(DATASET_DIR / "csv" / f"{name}.csv", index_col=0)
        df.index.name = None
        df = tidy_dataset(df, name)
