

class TropicalCyclonesProfileLifespan:
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        self.data = json_data

    @property
    def startTimestamp(self) -> int:
        return self.data["startTimestamp"]

    @property
    def startDateTimeISO(self) -> str:
        return self.data["startDateTimeISO"]

    @property
    def endTimestamp(self) -> int:
        return self.data["endTimestamp"]

    @property
    def endDateTimeISO(self) -> str:
        return self.data["endDateTimeISO"]
