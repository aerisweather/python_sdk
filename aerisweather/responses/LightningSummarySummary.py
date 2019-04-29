from aerisweather.responses.LightningSummaryNumSensors import LightningSummaryNumSensors
from aerisweather.responses.LightningSummaryICHeight import LightningSummaryICHeight
from aerisweather.responses.LightningSummaryPeakAmp import LightningSummaryPeakAmp
from aerisweather.responses.LightningSummaryPulse import LightningSummaryPulse
from aerisweather.responses.LightningSummaryRange import LightningSummaryRange


class LightningSummarySummary:
    """ Defines an object for the lightning summary's summary data. """

    summary = {}

    def __init__(self, json):
        """ Constructor - this takes an individual lightning summary's summary json. """

        self.summary = json

    @property
    def range(self) -> LightningSummaryRange:
        return LightningSummaryRange(self.summary["range"])

    @property
    def pulse(self) -> LightningSummaryPulse:
        return LightningSummaryPulse(self.summary["pulse"])

    @property
    def peakAmp(self) -> LightningSummaryPeakAmp:
        return LightningSummaryPeakAmp(self.summary["peakAmp"])

    @property
    def icHeight(self) -> LightningSummaryICHeight:
        return LightningSummaryICHeight(self.summary["icHeight"])

    @property
    def numSensors(self) -> LightningSummaryNumSensors:
        return LightningSummaryNumSensors(self.summary["numSensors"])