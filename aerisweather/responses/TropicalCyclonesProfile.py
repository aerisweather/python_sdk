from typing import List

from aerisweather.responses.TropicalCyclonesProfileLifespan import TropicalCyclonesProfileLifespan
from aerisweather.responses.TropicalCyclonesProfilePressure import TropicalCyclonesProfilePressure
from aerisweather.responses.TropicalCyclonesProfileWindSpeed import TropicalCyclonesProfileWindSpeed


class TropicalCyclonesProfile:
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        super().__init__(json_data=json_data)
        self.data = json_data

    @property
    def basinOrigin(self) -> str:
        return self.data["basinOrigin"]

    @property
    def basinCurrent(self) -> str:
        return self.data["basinCurrent"]

    @property
    def basins(self) -> List:

        basins = self.data["basins"]

        b_list = []  # type: List
        for bsn in basins:
            b_list.append(bsn)

        return b_list

    @property
    def name(self) -> str:
        return self.data["name"]

    @property
    def year(self) -> int:
        return self.data["year"]

    @property
    def event(self) -> int:
        return self.data["event"]

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
