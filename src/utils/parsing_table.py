import datetime as dt
import re
from pathlib import Path
from typing import Union, Type, Optional, Iterable
import numpy as np

import pandas as pd


class ParsingTable():

    @property
    def columns_types(self) -> dict[str, Type]:
        return {
            'device_id': str,
            'iaq': np.int64,
            'electrosmog_lf': np.int64,
            'wifi_level': np.int64,
            'wifi_n': np.int64,
            'temperature': np.int64,
            'humidity': np.int64,
            'air_pressure': np.int64,
            'ambient_light': np.int64,
            'tvoc': np.int64,
            'co2': np.int64,
            'co2e': np.int64,
            'pm10': np.int64,
            'pm25': np.int64,
            'electrosmog_hf': np.int64,
            'sound': np.int64,
            'battery': str,
            'main_power': str,
            'air': np.int64,
            'comfort': np.int64,
            'electrosmog': np.int64,
            'from_unixtime(ts)': dt.date,
            'rom_unixtime(ts)': dt.date,
            'date': dt.date

        }

    @staticmethod
    def date_converter(val):

        if not isinstance(val, str):
            return np.nan

        # date_format_1 = '%Y-%m-%d %H:%M:%S'
        regex_format_1 = re.compile('^\d{4}-\d{1,2}-\d{1,2}\s\d{2}:\d{2}:\d{2}$')
        # date_format_2 = '%d-%m-%Y %H:%M'
        regex_format_2 = re.compile('^\d{1,2}-\d{1,2}-\d{4}\s\d{2}:\d{2}$')
        # date_format_3 = '%d/%m/%Y'
        regex_format_3 = re.compile('^\d{1,2}/\d{1,2}/\d{4}')

        regex_match_1 = regex_format_1.findall(val)
        regex_match_2 = regex_format_2.findall(val)
        regex_match_3 = regex_format_3.findall(val)

        if regex_match_1:
            return dt.datetime.strptime(val, '%Y-%m-%d %H:%M:%S')
        if regex_match_2:
            return dt.datetime.strptime(val, '%d-%m-%Y %H:%M')
        if regex_match_3:
            return dt.datetime.strptime(val, '%d/%m/%Y').date()

    @staticmethod
    def convert(dtype: Type, vals: pd.Series) -> pd.Series:

        res = vals

        no_nan = res.loc[res.notna()].shape[0] == res.shape[0]

        if dtype != str:
            if dtype == dt.date:
                res.loc[res.notna()] = res.loc[res.notna()].apply(ParsingTable.date_converter)
            else:
                if no_nan:
                    res = pd.to_numeric(res, errors='coerce')
                    # res = res.astype(dtype)
                else:
                    res.loc[res.notna()] = pd.to_numeric(res.loc[res.notna()], errors='coerce').round(3)

            return res

        # res.loc[res.notna()] = res.loc[res.notna()].str.strip()

        return res

    def cast(self, df: pd.DataFrame) -> pd.DataFrame:
        res = df

        for c in df.columns:
            res[c] = ParsingTable.convert(self.columns_types[c], df[c])

        if 'from_unixtime(ts)' in res.columns.tolist():
            res.rename(columns={'from_unixtime(ts)': 'date'}, inplace=True)
        else:
            res.rename(columns={'rom_unixtime(ts)': 'date'}, inplace=True)

        if 'co2' not in res.columns.tolist():
            res['co2']=0
        column_ranges = {
            'iaq': (10, 400),
            'electrosmog_lf': (0, 600),
            'wifi_level': (-200, -2),
            'wifi_n': (0, 80),
            'temperature': (-20, 100),
            'humidity': (-10, 120),
            'air_pressure': (500, 2000),
            'ambient_light': (0, 2000),
            'tvoc': (0, 900),
            'co2': (0, 3000),
            'co2e': (0, 3000),
            'pm10': (0, 800),
            'pm25': (0, 600),
            'electrosmog_hf': (0, 90),
            'sound': (0, 200)
        }

        for column, column_range in column_ranges.items():
            res = res[res[column].between(column_range[0], column_range[1])]

        return res

    def _read_file(self, path: Path) -> pd.DataFrame:

        df = pd.read_csv(str(path),
                         # parse_dates=False,
                         encoding='latin1',

                         ).dropna()

        return self.cast(df)

    def parse(self, input_path: Path) -> pd.DataFrame:

        res = self._read_file(input_path)

        return res


if __name__ == '__main__':
    path = '../../resources/semi_clean_file/CAP153_1.csv'
    # print(ParsingTable().columns_types['device_id'])
    raw_df = pd.read_csv(path)
    df = ParsingTable().parse(path)
    print('end')
