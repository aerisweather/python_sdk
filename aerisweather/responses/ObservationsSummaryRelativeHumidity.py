

class ObservationsSummaryRelativeHumidity:
    """ Defines an object for the observations summary period relative humidity data. """

    rh = {}

    def __init__(self, rh_json):
        """
        Constructor - this takes an individual observations summary period's relative humidity json.
               {
                  maxC": 5,
                  "maxF": 41,
                  "minC": -3,
                  "minF": 26,
                  "avgC": -0.6,
                  "avgF": 30.9,
                  "count": 23
                },
        """

        self.rh = rh_json

    @property
    def max(self) -> int:
        """ The maximum relative humidity (0-100%). Null if not available. """
        return self.rh["max"]

    @property
    def min(self) -> int:
        """ The minimum relative humidity (0-100%). Null if not available. """
        return self.rh["min"]

    @property
    def avg(self) -> float:
        """  The average dew point in Celsius. Null if unavailable. """
        return self.rh["avg"]

    @property
    def count(self) -> int:
        """ The total number of observations that included relative humidity information. """
        return self.rh["count"]
