
from aerisweather.responses.AerisPlace import AerisPlacePlaces
from aerisweather.responses.AerisProfile import AerisProfilePlaces
from aerisweather.responses.Response import Response


class PlacesResponse(Response):
    """ Defines an object for the data returned in an Aeris API Places response."""

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
    def place(self):
        """Returns an AerisPlacePlaces object."""
        place = AerisPlacePlaces(self.data["place"])
        return place

    @property
    def profile(self):
        """Returns an AerisProfile object."""
        profile = AerisProfilePlaces(self.data["profile"])
        return profile
