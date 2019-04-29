
from aerisweather.responses.LightningSummarySummary import LightningSummarySummary
from aerisweather.responses.Response import Response


class LightningSummaryResponse(Response):
    """ Defines an object for the data returned in an Aeris API Lightning Summary responses."""

    data = {}

    def __init__(self, json_data=None):
        """ Constructor
            Takes a single response json object from an Aeris API data response.
        """

        super().__init__(json_data=json_data)
        self.data = json_data

    @property
    def summary(self) -> LightningSummarySummary:
        return LightningSummarySummary(self.data["summary"])
