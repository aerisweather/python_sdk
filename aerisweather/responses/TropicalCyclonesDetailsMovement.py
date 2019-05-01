

class TropicalCyclonesDetailsMovement:
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        self.data = json_data

    @property
    def directionDEG(self) -> int:
        return self.data["directionDEG"]

    @property
    def direction(self) -> str:
        return self.data["direction"]

    @property
    def speedKTS(self) -> int:
        return self.data["speedKTS"]

    @property
    def speedKPH(self) -> int:
        return self.data["speedKPH"]

    @property
    def speedMPH(self) -> int:
        return self.data["speedMPH"]
