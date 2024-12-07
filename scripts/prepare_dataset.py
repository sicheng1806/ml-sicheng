# %% [markdown]
# ## 准备数据集

# %%
import pandas as pd
from pathlib import Path

DATASET_DIR = Path("../dataset/")


# %%
with open(DATASET_DIR / "raw" / "supplement_S1.txt") as f:
    data = f.readlines()
with open(DATASET_DIR / "raw" / "S1.txt", 'w') as f:
    for line in data[3:]:
        f.write(line)
with open(DATASET_DIR / "raw" / "S1_cor.txt", 'w') as f:
    for line in data[0:3]:
        f.write(line)

# %%
dfs = []
for fname in ["S1_cor.txt","S1.txt","supplement_W1_power.txt","supplement_W1_velocity.txt"]:
    dfs.append(
        pd.read_csv(DATASET_DIR / "raw" / fname, sep=" ")
    )
CSV_DIR = DATASET_DIR / "csv"
if not CSV_DIR.exists():
    CSV_DIR.mkdir()

# %%
for n,df in zip(["S1","W1_power","W1_velocity"],dfs[1:]):
    df.set_index(df.columns[0])
    df.to_csv(CSV_DIR / f"{n}.csv",index=0)


