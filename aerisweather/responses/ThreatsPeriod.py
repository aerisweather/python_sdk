from aerisweather.responses.ThreatsStorms import ThreatsStorms


class ThreatsPeriod:

    period = {}

    def __init__(self, period_json):
        """ Constructor """

        self.period = period_json

    @property
    def timestamp(self) -> int:
        return self.period["timestamp"]

    @property
    def dateTimeISO(self) -> str:
        return self.period["dateTimeISO"]

    @property
    def storms(self) -> ThreatsStorms:
        return ThreatsStorms(self.period["storms"])
