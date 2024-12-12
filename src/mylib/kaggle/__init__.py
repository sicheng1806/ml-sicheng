import kagglehub
from pathlib import Path

__all__ = [
    "iskaggle",
    "kaggle_datasets",
]


def iskaggle():
    return Path("/kaggle").exists()


def kaggle_datasets(handle):
    if iskaggle():
        return Path(f"../input/{handle.split('/')[-1]}")
    host, name = handle.split("/")
    if host == "competitions":
        return Path(kagglehub.competition_download(name))
    return Path(kagglehub.dataset_download(handle))
