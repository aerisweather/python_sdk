

class PrecipSummaryPeriodSummaryPrecip:
    """ Defines an object for the precip summary's range data. """

    precip = {}

    def __init__(self, json):
        """ Constructor """

        self.precip = json

    @property
    def count(self) -> int:
        return self.precip["count"]

    @property
    def totalMM(self) -> float:
        return self.precip["totalMM"]

    @property
    def totalIN(self) -> float:
        return self.precip["totalIN"]
