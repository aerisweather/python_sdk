
from aerisweather.responses.ObservationsData import ObservationsData
from aerisweather.responses.AerisPlace import AerisPlace
from aerisweather.responses.AerisProfile import AerisProfileObservations
from aerisweather.responses.AerisRelativeTo import AerisRelativeTo
from aerisweather.responses.Response import Response


class ObservationsResponse(Response):
    """ Defines an object for the Observation data returned in an Aeris API observation responses."""

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
    def id(self)->str:
        """Returns the id value of the observation station."""
        return self.data["id"]

    @property
    def place(self):
        """Returns an AerisPlace object."""
        place = AerisPlace(self.data["place"])
        return place

    @property
    def profile(self):
        """Returns an AerisProfile object."""
        profile = AerisProfileObservations(self.data["profile"])
        return profile

    @property
    def relativeTo(self) -> AerisRelativeTo:
        """ Returns an AerisRelativeTo object. """
        relative_to = AerisRelativeTo(self.data["relativeTo"])
        return relative_to

    @property
    def raw(self):
        """Returns a json object containing the raw response data."""
        return self.data["raw"]

    @property
    def ob(self) -> ObservationsData:
        """Returns an observation json object. """
        return ObservationsData(self.data["ob"])

    @property
    def obTimestamp(self) -> int:
        """ Returns an int (int handles long ints in Python v3) containing the timestamp of the observation. """
        return self.data["obTimestamp"]

    @property
    def obDateTime(self):
        """ Returns a formatted string containing the timestamp of the observation. """
        return self.data["obDateTime"]
