import subprocess
from ml_sicheng import __version__
import argparse

version = f"v{__version__}"


def main():
    parser = argparse.ArgumentParser(
        description="release with tag or push kernel ml-sicheng-test to test in kaggle"
    )
    parser.add_argument("-t", "--task", type=str, default="tag", help="tag or kaggle")
    args = parser.parse_args()
    match args.task:
        case "tag":
            subprocess.run(
                ["git", "tag", "-d", version],
            )
            subprocess.run(["git", "push", "origin", "-d", version])
            subprocess.run(["git", "tag", version])
            subprocess.run(["git", "push", "origin", version])
        case "kaggle":
            subprocess.run(
                ["kaggle", "kernels", "push", "-p", "notebook/ml-sicheng-test"]
            )
        case _:
            print("error args!\n" "use --help for use")


if __name__ == "__main__":
    main()
