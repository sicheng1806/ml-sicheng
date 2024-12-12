import enum
import pandas as pd

from ml_sicheng.kaggle import kaggle_datasets


class DataSet(enum.Enum):
    Solar = "S1"
    WindPower = "W1_power"
    WindVelocity = "W1_velocity"

    @classmethod
    def handle(cls):
        return "sicheng1806/new-energy-plant"

    def load_dataframe(self):
        df = self.load_full_dataframe()
        return pd.DataFrame(df.T.mean(), columns=["value"])

    def load_full_dataframe(self):
        fpath = kaggle_datasets(self.handle()) / f"{self.value}.csv"
        return pd.read_csv(fpath, index_col=0)
