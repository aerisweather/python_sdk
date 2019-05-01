from aerisweather.responses.Geometry import Geometry


class TropicalCyclonesBreakPointAlerts:
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        self.data = json_data

    @property
    def alertType(self) -> str:
        return self.data['alertType']

    @property
    def coords(self) -> Geometry:
        return Geometry(self.data['coords'])
