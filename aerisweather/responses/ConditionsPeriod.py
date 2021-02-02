from typing import Optional


class ConditionsPeriod:
    """
    Object describing a period from the conditions endpoint.
    """
    # A conditions endpoint period takes the form:
    #
    # {
    #   "timestamp": 1612215840,
    #   "dateTimeISO": "2021-02-01T16:44:00-05:00",
    #   "tempC": 2.58,
    #   "tempF": 36.64,
    #   "feelslikeC": -1.26,
    #   "feelslikeF": 29.74,
    #   "dewpointC": -3.26,
    #   "dewpointF": 26.13,
    #   "humidity": 62,
    #   "pressureMB": 1014.5,
    #   "pressureIN": 29.96,
    #   "windDir": "NW",
    #   "windDirDEG": 320,
    #   "windSpeedKTS": 17.95,
    #   "windSpeedKPH": 33.24,
    #   "windSpeedMPH": 20.66,
    #   "windGustKTS": 26.9,
    #   "windGustKPH": 49.82,
    #   "windGustMPH": 30.96,
    #   "precipMM": 0,
    #   "precipIN": 0,
    #   "snowCM": 0,
    #   "snowIN": 0,
    #   "visibilityKM": 19.911,
    #   "visibilityMI": 12.372,
    #   "sky": 95,
    #   "cloudsCoded": "OV",
    #   "weather": "Cloudy",
    #   "weatherCoded": "::OV",
    #   "weatherPrimary": "Cloudy",
    #   "weatherPrimaryCoded": "::OV",
    #   "icon": "cloudy.png",
    #   "solradWM2": 83,
    #   "uvi": 0,
    #   "isDay": true
    # }

    def __init__(self, data) -> None:
        self.data = data

    @property
    def timestamp(self) -> int:
        return self.data["timestamp"]

    @property
    def dateTimeISO(self) -> str:
        return self.data["dateTimeISO"]

    @property
    def tempC(self) -> Optional[float]:
        return self.data["tempC"]

    @property
    def tempF(self) -> Optional[float]:
        return self.data["tempF"]

    @property
    def feelslikeC(self) -> Optional[float]:
        return self.data["feelsLikeC"]

    @property
    def feelslikeF(self) -> Optional[float]:
        return self.data["feelsLikeF"]

    @property
    def dewpointC(self) -> Optional[float]:
        return self.data["dewpointC"]

    @property
    def dewpointF(self) -> Optional[float]:
        return self.data["dewpointF"]

    @property
    def humidity(self) -> Optional[int]:
        return self.data["humidity"]

    @property
    def pressureMB(self) -> Optional[float]:
        return self.data["pressureMB"]

    @property
    def pressureIN(self) -> Optional[float]:
        return self.data["pressureIN"]

    @property
    def windDir(self) -> Optional[str]:
        return self.data["windDir"]

    @property
    def windDirDEG(self) -> Optional[int]:
        return self.data["windDirDEG"]

    @property
    def windSpeedKTS(self) -> Optional[float]:
        return self.data["windSpeedKTS"]

    @property
    def windSpeedKPH(self) -> Optional[float]:
        return self.data["windSpeedKPH"]

    @property
    def windSpeedMPH(self) -> Optional[float]:
        return self.data["windSpeedMPH"]

    @property
    def windGustKTS(self) -> Optional[float]:
        return self.data["windGustKTS"]

    @property
    def windGustKPH(self) -> Optional[float]:
        return self.data["windGustKPH"]

    @property
    def windGustMPH(self) -> Optional[float]:
        return self.data["windGustMPH"]

    @property
    def precipMM(self) -> Optional[int]:
        return self.data["precipMM"]

    @property
    def precipIN(self) -> Optional[float]:
        return self.data["precipIN"]

    @property
    def snowCM(self) -> Optional[float]:
        return self.data["snowCM"]

    @property
    def snowIN(self) -> Optional[float]:
        return self.data["snowIN"]

    @property
    def visibilityKM(self) -> Optional[float]:
        return self.data["visibilityKM"]

    @property
    def visibilityMI(self) -> Optional[float]:
        return self.data["visibilityMI"]

    @property
    def sky(self) -> Optional[float]:
        return self.data["sky"]

    @property
    def cloudsCoded(self) -> Optional[str]:
        return self.data["cloudsCoded"]

    @property
    def weather(self) -> Optional[str]:
        return self.data["weather"]

    @property
    def weatherCoded(self) -> Optional[str]:
        return self.data["weatherCoded"]

    @property
    def weatherPrimary(self) -> Optional[str]:
        return self.data["weatherPrimary"]

    @property
    def weatherPrimaryCoded(self) -> Optional[str]:
        return self.data["weatherPrimaryCoded"]

    @property
    def icon(self) -> Optional[str]:
        return self.data["icon"]

    @property
    def solradWM2(self) -> Optional[int]:
        return self.data["solradWM2"]

    @property
    def uvi(self) -> Optional[float]:
        return self.data["uvi"]

    @property
    def isDay(self) -> bool:
        return self.data["isDay"]
