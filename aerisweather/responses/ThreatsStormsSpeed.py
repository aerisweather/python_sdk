

class ThreatsStormsSpeed:
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        self.data = json_data

    @property
    def minKTS(self) -> int:
        return self.data["minKTS"]

    @property
    def minKPH(self) -> int:
        return self.data["minKPH"]

    @property
    def minMPH(self) -> int:
        return self.data["minMPH"]

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
    def avgKTS(self) -> int:
        return self.data["avgKTS"]

    @property
    def avgKPH(self) -> int:
        return self.data["avgKPH"]

    @property
    def avgMPH(self) -> int:
        return self.data["avgMPH"]
