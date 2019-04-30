from aerisweather.responses.PrecipSummaryPeriodSummary import PrecipSummaryPeriodSummary


class PrecipSummaryPeriod:

    period = {}

    def __init__(self, period_json):
        """ Constructor """

        self.period = period_json

    @property
    def summary(self) -> PrecipSummaryPeriodSummary:
        return PrecipSummaryPeriodSummary(self.period["summary"])
