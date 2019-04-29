

class LightningSummaryPeakAmpValues:
    """ Defines an object for the lightning summary's peak amp value data.
        Used with the peakAmp.all, peakAmp.positive and peakAmp.negative data.
    """

    peak_values = {}

    def __init__(self, json):
        """ Constructor """

        self.peak_values = json

    @property
    def min(self) -> int:
        return self.peak_values["min"]

    @property
    def max(self) -> int:
        return self.peak_values["max"]

    @property
    def avg(self) -> int:
        return self.peak_values["avg"]
