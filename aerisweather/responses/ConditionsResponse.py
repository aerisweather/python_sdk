from typing import List

from aerisweather.responses.AerisProfile import AerisProfileConditions
from aerisweather.responses.ConditionsPeriod import ConditionsPeriod
from aerisweather.responses.Response import Response


class ConditionsResponse(Response):
    """
    Defines the object that stores conditions for a location.
    """

    # URL / response body for conditions follows:
    #
    # https://api.aerisapi.com/conditions?p=33.953,-84.55&client_id=$AERIS_CLIENT_ID&client_secret=$AERIS_CLIENT_SECRET
    #
    #
    # {
    #   "success": true,
    #   "error": null,
    #   "response": [
    #     {
    #       "loc": {
    #         "lat": 33.953,
    #         "long": -84.55
    #       },
    #       "place": {
    #         "name": "marietta",
    #         "state": "ga",
    #         "country": "us"
    #       },
    #       "periods": [
    #         {
    #           "timestamp": 1612215840,
    #           "dateTimeISO": "2021-02-01T16:44:00-05:00",
    #           "tempC": 2.58,
    #           "tempF": 36.64,
    #           "feelslikeC": -1.26,
    #           "feelslikeF": 29.74,
    #           "dewpointC": -3.26,
    #           "dewpointF": 26.13,
    #           "humidity": 62,
    #           "pressureMB": 1014.5,
    #           "pressureIN": 29.96,
    #           "windDir": "NW",
    #           "windDirDEG": 320,
    #           "windSpeedKTS": 17.95,
    #           "windSpeedKPH": 33.24,
    #           "windSpeedMPH": 20.66,
    #           "windGustKTS": 26.9,
    #           "windGustKPH": 49.82,
    #           "windGustMPH": 30.96,
    #           "precipMM": 0,
    #           "precipIN": 0,
    #           "snowCM": 0,
    #           "snowIN": 0,
    #           "visibilityKM": 19.911,
    #           "visibilityMI": 12.372,
    #           "sky": 95,
    #           "cloudsCoded": "OV",
    #           "weather": "Cloudy",
    #           "weatherCoded": "::OV",
    #           "weatherPrimary": "Cloudy",
    #           "weatherPrimaryCoded": "::OV",
    #           "icon": "cloudy.png",
    #           "solradWM2": 83,
    #           "uvi": 0,
    #           "isDay": true
    #         }
    #       ],
    #       "profile": {
    #         "tz": "America/New_York",
    #         "tzname": "EST",
    #         "tzoffset": -18000,
    #         "isDST": false,
    #         "elevFT": null,
    #         "elevM": null
    #       }
    #     }
    #   ]
    # }

    def __init__(self, json_data):
        super().__init__(json_data=json_data)
        profile_data = self.data.get("profile", None)
        if profile_data is not None:
            self._profile = AerisProfileConditions(profile_data)

        period_data = self.data.get("periods", None)
        if period_data is not None:
            self._periods = [ConditionsPeriod(d) for d in period_data]

    @property
    def profile(self) -> AerisProfileConditions:
        return self._profile

    @property
    def periods(self) -> List[ConditionsPeriod]:
        return self._periods.copy()
