
from typing import List

from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.AerisRelativeTo import AerisRelativeTo
from aerisweather.responses.LightningObservation import LightningObservation
from aerisweather.responses.Response import Response


class LightningResponse(Response):
    """ Defines an object for the data returned in an Aeris API Lightning responses."""

    data = {}

    def __init__(self, json_data=None):
        """ Constructor
            Takes a single response json object from an Aeris API data response.
        """

        super().__init__(json_data=json_data)
        self.data = json_data

    @property
    def id(self) -> str:
        return self.data["id"]

    @property
    def loc(self) -> AerisLocation:
        return AerisLocation(self.data["loc"])

    @property
    def ob(self) -> LightningObservation:
        return LightningObservation(self.data["ob"])

    @property
    def recTimestamp(self) -> int:
        return self.data["recTimestamp"]

    @property
    def recISO(self) ->str:
        return self.data["recISO"]

    @property
    def age(self):
        return self.data["age"]

    @property
    def relativeTo(self) -> AerisRelativeTo:
        """ Returns an AerisRelativeTo object. """
        relative_to = AerisRelativeTo(self.data["relativeTo"])
        return relative_to
