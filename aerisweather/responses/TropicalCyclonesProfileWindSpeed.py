

class TropicalCyclonesProfileWindSpeed:
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        self.data = json_data

    @property
    def maxKTS(self) -> int:
        return self.data["maxKTS"]

    @property
    def maxKPH(self) -> int:
        return self.data["maxKPH"]

    @property
    def maxMPH(self) -> int:
        return self.data["maxMPH"]

    @property
    def maxTimestamp(self) -> int:
        return self.data["maxTimestamp"]

    @property
    def maxDateTimeISO(self) -> str:
        return self.data["maxDateTimeISO"]
