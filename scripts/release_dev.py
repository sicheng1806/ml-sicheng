import subprocess
from ml_sicheng import __version__

version = f"v{__version__}"

if __name__ == "__main__":
    subprocess.run(
        ["git", "tag", "-d", version],
    )
    subprocess.run(["git", "push", "origin", "-d", version])
    subprocess.run(["git", "tag", version])
    subprocess.run(["git", "push", "origin", version])
