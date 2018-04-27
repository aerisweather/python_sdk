
from typing import List
from aerisweather.responses.AerisProfile import AerisProfileForecasts
from aerisweather.responses.ForecastPeriod import ForecastPeriod
from aerisweather.responses.Response import Response


class ForecastsResponse(Response):
    """ Defines an object for the data returned in an Aeris API Forecasts responses."""

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
    def profile(self):
        """Returns an AerisProfile object."""
        profile = AerisProfileForecasts(self.data["profile"])
        return profile

    @property
    def interval(self):
        """ The interval between periods. """
        return self.data["interval"]

    @property
    def periods(self) -> List[ForecastPeriod]:
        """ Returns an array of ForecastPeriod objects """

        periods = self.data["periods"]

        p_list = []  # type: [ForecastPeriod]
        for per in periods:
            fp = ForecastPeriod(per)
            p_list.append(fp)

        return p_list
