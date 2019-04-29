

class LightningSummaryICHeight:
    """ Defines an object for the lightning summary's icHeight data. """

    height = {}

    def __init__(self, json):
        """ Constructor - this takes an individual lightning summary's icHeight json. """

        self.height = json

    @property
    def count(self) -> int:
        return self.height["count"]

    @property
    def min(self) -> int:
        return self.height["min"]

    @property
    def max(self) -> int:
        return self.height["max"]

    @property
    def avg(self) -> int:
        return self.height["avg"]
