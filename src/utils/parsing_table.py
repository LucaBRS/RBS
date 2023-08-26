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
            'rom_unixtime(ts)': dt.date

        }

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
            return dt.datetime.strptime(val, '%d/%m/%Y')


    def date_converter_ext(self,val):

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
            return dt.datetime.strptime(val, '%d/%m/%Y')



    def cast(self, df: pd.DataFrame) -> pd.DataFrame:
        res = df
        for c in df.columns:
            res[c] = ParsingTable.convert(self.columns_types[c], df[c])

        return res

    def _read_file(self, path: Path) -> pd.DataFrame:

        df = pd.read_csv(str(path),
                         # parse_dates=False,
                         encoding='latin1',

                         )

        return self.cast(df)

    def parse(self, input_path: Path) -> pd.DataFrame:

        res = self._read_file(input_path)

        return res


if __name__ == '__main__':
    path = '../../resources/clean_file/CAP153_1.csv'
    # print(ParsingTable().columns_types['device_id'])
    raw_df = pd.read_csv(path)
    df = ParsingTable().parse(path)
    print('end')
