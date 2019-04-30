from typing import List

from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.AerisPlace import AerisPlace
from aerisweather.responses.AerisProfile import AerisProfilePrecipSummary
from aerisweather.responses.PrecipSummaryPeriod import PrecipSummaryPeriod
from aerisweather.responses.Response import Response


class PrecipSummaryResponse(Response):
    """ Defines an object for the data returned in an Aeris API Precip Summary responses."""

    data = {}

    def __init__(self, json_data=None):
        """ Constructor """

        super().__init__(json_data=json_data)
        self.data = json_data

    @property
    def loc(self) -> AerisLocation:
        return AerisLocation(self.data["loc"])

    @property
    def place(self):
        place = AerisPlace(self.data["place"])
        return place

    @property
    def periods(self) -> List[PrecipSummaryPeriod]:
        """ Returns an array of PrecipSummaryPeriod objects """

        periods = self.data["periods"]

        p_list = []  # type: [PrecipSummaryPeriod]
        for per in periods:
            precip_per = PrecipSummaryPeriod(per)
            p_list.append(precip_per)

        return p_list

    @property
    def profile(self):
        """Returns an AerisProfile object."""
        profile = AerisProfilePrecipSummary(self.data["profile"])
        return profile
