from aerisweather.responses.PrecipSummaryPeriodSummaryPrecip import PrecipSummaryPeriodSummaryPrecip
from aerisweather.responses.PrecipSummaryPeriodSummaryRange import PrecipSummaryPeriodSummaryRange


class PrecipSummaryPeriodSummary:
    """ Defines an object for the precip summary's summary data. """

    summary = {}

    def __init__(self, json):
        """ Constructor """

        self.summary = json

    @property
    def timestamp(self) -> int:
        return self.summary["timestamp"]

    @property
    def dateTimeISO(self) -> str:
        return self.summary["dateTimeISO"]

    @property
    def range(self) -> PrecipSummaryPeriodSummaryRange:
        return PrecipSummaryPeriodSummaryRange(self.summary["range"])

    @property
    def precip(self) -> PrecipSummaryPeriodSummaryPrecip:
        return PrecipSummaryPeriodSummaryPrecip(self.summary["precip"])
