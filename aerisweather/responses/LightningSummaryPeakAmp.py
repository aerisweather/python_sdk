from aerisweather.responses.LightningSummaryPeakAmpValues import LightningSummaryPeakAmpValues


class LightningSummaryPeakAmp:
    """ Defines an object for the lightning summary's peak amp data. """

    peak = {}

    def __init__(self, json):
        """ Constructor - this takes an individual lightning summary's peak amp json. """

        self.peak = json

    @property
    def count(self) -> int:
        return self.peak["count"]

    @property
    def all(self) -> LightningSummaryPeakAmpValues:
        return LightningSummaryPeakAmpValues(self.peak["all"])

    @property
    def positive(self) -> LightningSummaryPeakAmpValues:
        return LightningSummaryPeakAmpValues(self.peak["positive"])

    @property
    def negative(self) -> LightningSummaryPeakAmpValues:
        return LightningSummaryPeakAmpValues(self.peak["negative"])
