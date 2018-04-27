
from typing import List

from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.AerisPlace import AerisPlace
from aerisweather.responses.AerisProfile import AerisProfileObservationsSummary
from aerisweather.responses.ObservationsSummaryPeriod import ObservationsSummaryPeriod
from aerisweather.responses.Response import Response


class ObservationsSummaryResponse(Response):
    """ Defines an object for the data returned in an Aeris API ObservationsSummary responses."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor
        Takes a single response json object from an Aeris API data response.

        Examples would be:
            either of the responses in the following response array:
              "response": [
                {
                ...
                },
                {
                ...
                }
        or
            the contents of a single response:
              "response": {
                "loc": {
                  "lat": 43.80136,
        """

        super().__init__(json_data=json_data)
        self.data = json_data

    @property
    def id(self) -> str:
        """Returns the id value of the observation station."""
        return self.data["id"]

    @property
    def loc(self) -> AerisLocation:
        """Returns an AerisLocation object."""
        return AerisLocation(self.data["loc"])

    @property
    def place(self):
        """Returns an AerisPlace object."""
        place = AerisPlace(self.data["place"])
        return place

    @property
    def periods(self) -> List[ObservationsSummaryPeriod]:
        """ Returns an array of ObservationsSummaryPeriod objects """

        periods = self.data["periods"]

        p_list = []  # type: [ObservationsSummaryPeriod]
        for per in periods:
            osp = ObservationsSummaryPeriod(per)
            p_list.append(osp)

        return p_list

    @property
    def profile(self):
        """Returns an AerisProfile object."""
        profile = AerisProfileObservationsSummary(self.data["profile"])
        return profile
