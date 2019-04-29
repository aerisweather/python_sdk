

class LightningSummaryPulse:
    """ Defines an object for the lightning summary's pulse data. """

    pulse = {}

    def __init__(self, json):
        """ Constructor - this takes an individual lightning summary's pulse json. """

        self.pulse = json

    @property
    def count(self) -> int:
        return self.pulse["count"]

    @property
    def cg(self) -> int:
        return self.pulse["cg"]

    @property
    def ic(self) -> int:
        return self.pulse["ic"]

    @property
    def negative(self) -> int:
        return self.pulse["negative"]

    @property
    def positive(self) -> int:
        return self.pulse["positive"]
