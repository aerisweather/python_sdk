

class TropicalCyclonesProfilePressure:
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        super().__init__(json_data=json_data)
        self.data = json_data

    @property
    def minMB(self) -> int:
        return self.data["minMB"]

    @property
    def minIN(self) -> int:
        return self.data["minIN"]

    @property
    def minTimestamp(self) -> int:
        return self.data["minTimestamp"]

    @property
    def minDateTimeISO(self) -> str:
        return self.data["minDateTimeISO"]
