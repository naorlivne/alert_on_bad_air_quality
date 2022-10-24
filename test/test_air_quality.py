from unittest import TestCase
from alert_on_bad_air.functions.air_quality.aqi import *
from parse_it import ParseIt


parser = ParseIt(recurse=False, config_type_priority=["envvars"])
aqicn_api_key = parser.read_configuration_variable("aqicn_api_key", required=True)


class BaseTests(TestCase):

    def test_weather_forecast_init(self):
        current_aqi = air_quality_index(aqicn_api_key, "tel-aviv")
        self.assertTrue(0 <= current_aqi <= 1000)

