

class ThreatsStormsDirection:

    period = {}

    def __init__(self, period_json):
        """ Constructor """

        self.period = period_json

    @property
    def toDEG(self) -> int:
        return self.period["toDEG"]

    @property
    def to(self) -> str:
        return self.period["to"]

    @property
    def fromDEG(self) -> int:
        return self.period["fromDEG"]

    @property
    def from_(self) -> str:
        return self.period["from"]
