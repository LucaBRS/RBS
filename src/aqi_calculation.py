import numpy as np
import pandas as pd


class AqiCalculation:

    def __init__(self, dict_df: dict):
        self.dict_df = dict_df

    def get_aqi_level_by_category(self, x_level, component):
        if component not in list(self.dict_df.keys()):
            return np.nan
        else:
            df = self.dict_df[component]
            for a in range(len(df)):
                if df['I_LOW'][a] <= x_level < df['I_HIGH'][a]:
                    return ((x_level - df['I_LOW'][a]) / (df['I_HIGH'][a] - df['I_LOW'][a])) * (
                                df['AQI_HIGH'][a] - df['AQI_LOW'][a]) + df['AQI_LOW'][a]

        return np.nan


if __name__ == '__main__':
    path = '../resources/aqi_breakpoints.xlsx'
    aqi = AqiCalculation(dict_df=pd.read_excel(path, sheet_name=['electrosmog_lf', 'wifi_level',
                                                                 'temperature', 'humidity', 'air_pressure',
                                                                 'ambient_light', 'tvoc',
                                                                 'co2', 'co2e', 'pm10', 'pm25', 'sound',
                                                                 'electrosmog_hf']))
    test = aqi.get_aqi_level_by_category(1011, 'ambient_light')
    print('lol')




