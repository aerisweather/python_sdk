
from typing import List

from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.AerisPlace import AerisPlace
from aerisweather.responses.AerisProfile import AerisProfileObservationsArchive
from aerisweather.responses.ObservationsArchivePeriod import ObservationsArchivePeriod
from aerisweather.responses.Response import Response


class ObservationsArchiveResponse(Response):
    """ Defines an object for the data returned in an Aeris API Observations Archive responses."""

    data = {}

    def __init__(self, json_data=None):
        """ Constructor """

        super().__init__(json_data=json_data)
        self.data = json_data

    @property
    def id(self) -> str:
        return self.data["id"]

    @property
    def loc(self) -> AerisLocation:
        return AerisLocation(self.data["loc"])

    @property
    def place(self):
        place = AerisPlace(self.data["place"])
        return place

    @property
    def periods(self) -> List[ObservationsArchivePeriod]:
        """ Returns an array of ObservationsArchivePeriod objects """

        periods = self.data["periods"]

        p_list = []  # type: [ObservationsArchivePeriod]
        for per in periods:
            osp = ObservationsArchivePeriod(per)
            p_list.append(osp)

        return p_list

    @property
    def profile(self):
        """Returns an AerisProfile object."""
        profile = AerisProfileObservationsArchive(self.data["profile"])
        return profile
