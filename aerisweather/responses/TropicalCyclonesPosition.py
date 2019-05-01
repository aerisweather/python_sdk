from typing import List

from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.TropicalCyclonesDetails import TropicalCyclonesDetails
from aerisweather.responses.TropicalCyclonesLocation import TropicalCyclonesLocation
from aerisweather.responses.TropicalCyclonesProfileLifespan import TropicalCyclonesProfileLifespan
from aerisweather.responses.TropicalCyclonesProfilePressure import TropicalCyclonesProfilePressure
from aerisweather.responses.TropicalCyclonesProfileWindSpeed import TropicalCyclonesProfileWindSpeed


class TropicalCyclonesPosition:
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        self.data = json_data

    @property
    def location(self) -> TropicalCyclonesLocation:
        return TropicalCyclonesLocation(self.data["location"])

    @property
    def details(self) -> TropicalCyclonesDetails:
        return TropicalCyclonesDetails(self.data["details"])

    @property
    def timestamp(self) -> int:
        return self.data["timestamp"]

    @property
    def dateTimeISO(self) -> str:
        return self.data["dateTimeISO"]

    @property
    def loc(self) -> AerisLocation:
        return AerisLocation(self.data["loc"])

    @property
    def isActive(self) -> bool:
        return self.data["isActive"]

    @property
    def lifespan(self) -> TropicalCyclonesProfileLifespan:
        return TropicalCyclonesProfileLifespan(self.data["lifespan"])

    @property
    def maxStormType(self) -> str:
        return self.data["maxStormType"]

    @property
    def maxStormCat(self) -> str:
        return self.data["maxStormCat"]

    @property
    def windSpeed(self) -> TropicalCyclonesProfileWindSpeed:
        return TropicalCyclonesProfileWindSpeed(self.data["windSpeed"])

    @property
    def pressure(self) -> TropicalCyclonesProfilePressure:
        return TropicalCyclonesProfilePressure(self.data["pressure"])

    @property
    def boundingBox(self) -> List[float]:
        return self.data["boundingBox"]

    @property
    def tz(self) -> str:
        return self.data["tz"]
