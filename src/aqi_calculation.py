import numpy as np
import pandas as pd


class AqiCalculation:

    def __init__(self, dict_df: dict):
        self.dict_df = dict_df

    def get_aqi_level_by_category(self, x_level, category):
        if category not in list(self.dict_df.keys()):
            return -1
        else:
            df = self.dict_df[category]
            for a in range(len(df)):
                if df['I_LOW'][a] <= x_level < df['I_HIGH'][a]:
                    result = ((x_level - df['I_LOW'][a]) / (df['I_HIGH'][a] - df['I_LOW'][a])) * (
                            df['AQI_HIGH'][a] - df['AQI_LOW'][a]) + df['AQI_LOW'][a]
                    return round(result, 2)

        return -1

    def get_max_aqi(self, d: dict):
        aqi_list = []
        save_category = ''
        for category in list(self.dict_df.keys()):
            if category in list(d.keys()):
                aqi_list.append((category, self.get_aqi_level_by_category(x_level=d[category], category=category)))

        return max(aqi_list, key=lambda x: x[1])

    def calculate_aqi_on_df(self, df: pd.DataFrame):
        df_copy = df.copy()
        df_copy[['category_aqi', 'max_aqi']] = df_copy.apply(lambda row: self.get_max_aqi(row.to_dict()), axis=1,
                                                             result_type='expand')
        return df_copy


if __name__ == '__main__':
    path = '../resources/aqi_breakpoints.xlsx'
    aqi = AqiCalculation(dict_df=pd.read_excel(path, sheet_name=['electrosmog_lf', 'wifi_level',
                                                                 'temperature', 'humidity', 'air_pressure',
                                                                 'ambient_light', 'tvoc',
                                                                 'co2', 'co2e', 'pm10', 'pm25', 'sound',
                                                                 'electrosmog_hf']))
    test = aqi.get_aqi_level_by_category(1011, 'ambient_light')
    print(test)
