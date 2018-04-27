

class ObservationsSummarySolrad:
    """ Defines an object for the observations summary period solar radiation data. """

    solrad = {}

    def __init__(self, json):
        """
        Constructor - this takes an individual observations summary period's sky json.
               {
                  "maxWM2": null,
                  "minWM2": null,
                  "avgWM2": null,
                  "totalWM2": null,
                  "method": null,
                  "count": 0
                },
        """

        self.solrad = json

    @property
    def maxWM2(self) -> int:
        """ The maximum reported solar radiation. Null if not available. """
        return self.solrad["maxWM2"]

    @property
    def minWM2(self) -> int:
        """ The minimum reported solar radiation. Null if not available. """
        return self.solrad["minWM2"]

    @property
    def avgWM2(self) -> int:
        """ The average reported solar radiation. Null if not available. """
        return self.solrad["avgWM2"]

    @property
    def totalWM2(self) -> int:
        return self.solrad["totalWM2"]

    @property
    def method(self) -> [str]:
        return self.solrad["method"]

    @property
    def count(self) -> int:
        """ Total number of observations that reported solar radiation. """
        return self.solrad["count"]
