"""
Data bundle
"""

from typing import Optional
from enum import Enum

class DataFormat(Enum):
    PANDAS = 1
    JSON = 2

class Data:
    def __init__(self):
        pass

    def set(self, format_: DataFormat, data):
        pass

    def get(self, format_: DataFormat):
        pass

class DataPandas(Data):
    def __init__(self, df):
        super().__init__()
        self.df = df

    def set(self, data, format_: DataFormat = DataFormat.PANDAS ):
        self.df = data

    def get(self, format_: DataFormat = DataFormat.PANDAS):
        if format_ == DataFormat.PANDAS:
            return self.df

class DataJson(Data):
    def __init__(self, json):
        super().__init__()
        self.json = json

    def set(self, data, format_: DataFormat = DataFormat.JSON) \
        -> None:
        self.json = data

    def get(self, format_: DataFormat = DataFormat.JSON) \
        -> Optional[object]:
        if format_ == DataFormat.JSON:
            return self.json
        return None
