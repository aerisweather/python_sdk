

class LightningSummaryRange:
    """ Defines an object for the lightning summary's range data. """

    range = {}

    def __init__(self, json):
        """ Constructor - this takes an individual lightning summary's range json. """

        self.range = json

    @property
    def count(self) -> int:
        return self.range["count"]

    @property
    def fromTimestamp(self) -> int:
        return self.range["fromTimestamp"]

    @property
    def fromDateTimeISO(self) -> str:
        return self.range["fromDateTimeISO"]

    @property
    def toTimestamp(self) -> int:
        return self.range["toTimestamp"]

    @property
    def toDateTimeISO(self) -> str:
        return self.range["toDateTimeISO"]

    @property
    def maxTimestamp(self) -> int:
        return self.range["maxTimestamp"]

    @property
    def maxDateTimeISO(self) -> str:
        return self.range["maxDateTimeISO"]

    @property
    def minTimestamp(self) -> int:
        return self.range["minTimestamp"]

    @property
    def minDateTimeISO(self) -> str:
        return self.range["minDateTimeISO"]
