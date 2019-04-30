

class PrecipSummaryPeriodSummaryRange:
    """ Defines an object for the precip summary's range data. """

    range = {}

    def __init__(self, json):
        """ Constructor """

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
