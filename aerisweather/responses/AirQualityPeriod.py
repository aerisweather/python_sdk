
from typing import List
from aerisweather.responses.Pollutant import Pollutant


class AirQualityPeriod:
    """ Defines an object for the air quality period data. """

    period = {}

    def __init__(self, period_json):
        """
        Constructor - this takes an individual air quality period's json.
                        {
                        "timestamp": 1521543600,
                        "aqi...
        """

        self.period = period_json

    @property
    def dateTimeISO(self) -> str:
        """ ISO 8601 of the valid time of the forecast. """
        return self.period["dateTimeISO"]

    @property
    def timestamp(self) -> int:
        """ UNIX timestamp of the forecast valid time """
        return self.period["timestamp"]

    @property
    def aqi(self) -> int:
        """ The standardized Air Quality Index value from 0 - 500 """
        return self.period["aqi"]

    @property
    def category(self) -> str:
        """ The Air Quality category based on the AQI """
        return self.period["category"]

    @property
    def color(self) -> str:
        """ The 6 character hexadecimal color code for the specific category. """
        return self.period["color"]

    @property
    def method(self) -> str:
        """ The method used for the AQI calculation:
            - airnow = Used the EPA AirNow AQI specification (default)
            - china = Used the China AQI specification (filter=china)
            - india = Used the India AQI specification (filter=india) """
        return self.period["method"]

    @property
    def dominant(self) -> str:
        """ The dominant pollutant. Normally set to one of the following:
            - co (Carbon Monoxide)
            - no2 (Nitrogen Dioxide)
            - o3 (Ozone)
            - pm10 (Particle Matter <10µm)
            - pm2.5 (Particle Matter <2.5µm)
            - so2 (Sulfur Dioxide) """
        return self.period["dominant"]

    @property
    def pollutants(self) -> List[Pollutant]:
        """  Array of pollutants.
                "pollutants": [
                    {
                      "type": "o3",
                      "name": "ozone",
                      "valuePPB": 33,
                      "valueUGM3": 68,
                      "aqi": 30,
                      "category": "good",
                      "color": "00E400"
                    }
                    {
                      "type": "o3",
                      "name": "ozone",
                      ...
                    }
                ],
        """
        pollutant_list = []
        for pol in self.period["pollutants"]:
            pollutant = Pollutant(pol)
            pollutant_list.append(pollutant)
        return pollutant_list

    @property
    def profile(self):
        """Returns an AerisProfile object."""
        profile = AerisProfileObservations(self.data["profile"])
        return profile