import nox
import argparse
import shutil
from pathlib import Path

python_version = "3.13"

nox.options.sessions = ["prepare-dataset", "clean"]


@nox.session(name="prepare-dataset", reuse_venv=True)
def prepare_dataset(session):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--only-tidy", action="store_false", help="only prepare tidy data"
    )
    args = parser.parse_args(session.posargs)

    session.install("pandas")
    if not args.only_tidy:
        session.run("python", "scripts/prepare_dataset.py")
    session.run("python", "scripts/tidy_dataset.py")


@nox.session(reuse_venv=True)
def clean(session):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--target",
        type=str,
        default="imgs",
        help="the target of clean: imgs,data,nox,uv,dataset. default value is : output",
    )

    args = parser.parse_args(session.posargs)
    clean_dir = []
    match args.target:
        case "imgs":
            clean_dir.append("output/imgs")
        case "data":
            clean_dir.append("output/.data")
        case "nox":
            clean_dir.append(".nox")
        case "uv":
            clean_dir.append(".venv")
        case "dataset":
            clean_dir.append("dataset")
        case e:
            raise ValueError(f"Unknown Target value:{e}")
    for c in clean_dir:
        shutil.rmtree(c, ignore_errors=True)
    if args.target == "imgs":
        Path("output/imgs").mkdir()


@nox.session(reuse_venv=True)
def lint(session: nox.Session):
    session.install("ruff")
    session.run(
        "ruff",
        "format",
    )
    session.run(
        "ruff",
        "check",
        "--fix",
    )


@nox.session(reuse_venv=True, name="tar-lib")
def tar_lib(session: nox.Session):
    tar_options = ["--exclude=__pycache__", "--exclude=tests", "-C", "src"]
    tar_cmd = ["tar", "-zcvf", "datasets/sicheng-ml-lib/mylib.tar.gz"] + tar_options + ["mylib"]
    session.run(*tar_cmd, external=True)
