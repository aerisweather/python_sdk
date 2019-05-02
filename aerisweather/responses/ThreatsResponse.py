from typing import List

from aerisweather.responses.ThreatsPeriod import ThreatsPeriod
from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.AerisPlace import AerisPlace
from aerisweather.responses.AerisProfile import AerisProfile
from aerisweather.responses.Response import Response


class ThreatsResponse(Response):
    """ Defines an object for the data returned in an Aeris API Threats response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        super().__init__(json_data=json_data)
        self.data = json_data

    @property
    def loc(self) -> AerisLocation:
        return AerisLocation(self.data["loc"])

    @property
    def place(self):
        """Returns an AerisPlacePlaces object."""
        place = AerisPlace(self.data["place"])
        return place

    @property
    def profile(self):
        """Returns an AerisProfile object."""
        profile = AerisProfile(self.data["profile"])
        return profile

    @property
    def periods(self) -> List[ThreatsPeriod]:
        """ Returns an array of PrecipSummaryPeriod objects """

        periods = self.data["periods"]

        p_list = []  # type: [ThreatsPeriod]
        for per in periods:
            precip_per = ThreatsPeriod(per)
            p_list.append(precip_per)

        return p_list
