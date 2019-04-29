

class LightningSummaryNumSensors:
    """ Defines an object for the lightning summary's numSensors data. """

    numsensors = {}

    def __init__(self, json):
        """ Constructor - this takes an individual lightning summary's numSensors json. """

        self.numsensors = json

    @property
    def count(self) -> int:
        return self.numsensors["count"]

    @property
    def min(self) -> int:
        return self.numsensors["min"]

    @property
    def max(self) -> int:
        return self.numsensors["max"]

    @property
    def avg(self) -> int:
        return self.numsensors["avg"]
