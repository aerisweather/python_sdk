

class ObservationsSummarySky:
    """ Defines an object for the observations summary period sky data. """

    sky = {}

    def __init__(self, json):
        """
        Constructor - this takes an individual observations summary period's sky json.
               {
                  max": 100,
                  "min": 44,
                  "avg": 90,
                  "count": 23,
                  "coded": [
                    "OV",
                    "SC",
                    "BK"
                  ]
                },
        """

        self.sky = json

    @property
    def max(self) -> int:
        """ The maximum sky coverage (0-100, 0 = clear, 100 = overcast). Null if not available. """
        return self.sky["max"]

    @property
    def min(self) -> int:
        """ The minimum sky coverage (0-100, 0 = clear, 100 = overcast). Null if not available. """
        return self.sky["min"]

    @property
    def avg(self) -> int:
        """ The average sky coverage (0-100, 0 = clear, 100 = overcast). Null if not available. """
        return self.sky["avg"]

    @property
    def coded(self) -> [str]:
        """ The coded reported sky coverages. Refer to the coded weather doc for possible values."""
        return self.sky["coded"]

    @property
    def count(self) -> int:
        """ Total number of observations that reported cloud coverage. """
        return self.sky["count"]
