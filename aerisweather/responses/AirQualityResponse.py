from typing import List

from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.AirQualityPeriod import AirQualityPeriod
from aerisweather.responses.AerisPlace import AerisPlace
from aerisweather.responses.AerisProfile import AerisProfileAirQuality
from aerisweather.responses.Response import Response


class AirQualityResponse(Response):
    """ Defines an object for the Air Quality data returned in an Aeris API airquality response. """

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
        return self.data["id"]

    @property
    def loc(self) -> AerisLocation:
        return AerisLocation(self.data["loc"])

    @property
    def place(self):
        """Returns an AerisPlace object."""
        place = AerisPlace(self.data["place"])
        return place

    @property
    def periods(self) -> List[AirQualityPeriod]:
        """ Returns an array of ForecastPeriod objects """

        periods = self.data["periods"]

        p_list = []  # type: [AirQualityPeriod]
        for per in periods:
            ap = AirQualityPeriod(per)
            p_list.append(ap)

        return p_list

    @property
    def profile(self):
        """Returns an AerisProfile object."""
        profile = AerisProfileAirQuality(self.data["profile"])
        return profile
