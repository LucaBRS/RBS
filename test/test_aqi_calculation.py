import unittest

import numpy as np
import numpy.testing
import pandas as pd

from utils.aqi_calculation import AqiCalculation


class TestAqiCalculation(unittest.TestCase):
    def setUp(self):
        path = '../resources/aqi_breakpoints.xlsx'
        self.aqi_calc = AqiCalculation(dict_df=pd.read_excel(path, sheet_name=['electrosmog_lf', 'wifi_level',
                                                                               'temperature', 'humidity',
                                                                               'air_pressure',
                                                                               'ambient_light', 'tvoc',
                                                                               'co2', 'co2e', 'pm10', 'pm25', 'sound',
                                                                               'electrosmog_hf']))

    def test_get_aqi_level_by_category(self):
        self.assertEquals(self.aqi_calc.get_aqi_level_by_category(1011, 'ambient_light'), 101.98)
        numpy.testing.assert_equal(self.aqi_calc.get_aqi_level_by_category(5449511, 'ambient_light'), np.nan)
        numpy.testing.assert_equal(self.aqi_calc.get_aqi_level_by_category(-1, 'ambient_light'), np.nan)
        numpy.testing.assert_equal(self.aqi_calc.get_aqi_level_by_category(1011, 'lol'), np.nan)

    def test_get_max_aqi(self):
        test_dict = {'electrosmog_hf': 1,
                     'sound': 1,
                     'ambient_light': 1011,
                     'wifi_level': 1
                     }
        self.assertEquals(self.aqi_calc.get_max_aqi(d=test_dict), ('ambient_light',101.98) )

        test_dict = {'electrosmog_hf': 1,
                     'sound': 1,
                     'ambient_light': 1011,
                     'wifi_level': 5555888
                     }
        self.assertEquals(self.aqi_calc.get_max_aqi(d=test_dict), ('ambient_light', 101.98))