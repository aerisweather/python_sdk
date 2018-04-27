

class ObservationsSummaryWind:
    """ Defines an object for the observations summary period wind data. """

    wind = {}

    def __init__(self, wind_json):
        """
        Constructor - this takes an individual observations summary period's wind json.
               {
                  maxKTS": 9,
                  "maxKPH": 17,
                  "maxMPH": 10,
                  "gustKTS": 15,
                  "gustKPH": 28,
                  "gustMPH": 17,
                  "count": 23,
                  "minKTS": 0,
                  "minKPH": 0,
                  "minMPH": 0,
                  "avgKTS": 2,
                  "avgKPH": 3.7,
                  "avgMPH": 2.3
                },
        """

        self.wind = wind_json

    @property
    def maxKTS(self) -> float:
        """ The maximum wind speed in knots. Null if not available. """
        return self.wind["maxKTS"]

    @property
    def maxKPH(self) -> float:
        """ The maximum wind speed in kilometers per hour. Null if not available. """
        return self.wind["maxKPH"]

    @property
    def maxMPH(self) -> float:
        """ The maximum wind speed in miles per hour. Null if not available. """
        return self.wind["maxMPH"]

    @property
    def minKTS(self) -> float:
        """ The minimum wind speed in knots. Null if not available. """
        return self.wind["minKTS"]

    @property
    def minKPH(self) -> float:
        """ The minimum wind speed in kilometers per hour. Null if not available."""
        return self.wind["minKPH"]

    @property
    def minMPH(self) -> float:
        """ The minimum wind speed in miles per hour. Null if not available. """
        return self.wind["minMPH"]

    @property
    def avgKTS(self) -> float:
        """ The average wind speed in knots. Null if not available."""
        return self.wind["avgKTS"]

    @property
    def avgKPH(self) -> float:
        """ The average wind speed in kilometers per hour. Null if not available. """
        return self.wind["avgKPH"]

    @property
    def avgMPH(self) -> float:
        """ The average wind speed in miles per hour. Null if not available. """
        return self.wind["avgMPH"]

    @property
    def gustKTS(self) -> float:
        """ The minimum temperature in Knots. Null if unavailable. """
        return self.wind["gustKTS"]

    @property
    def gustKPH(self) -> float:
        """ The maximum wind gust in kilometers per hour. Null if not available. """
        return self.wind["gustKPH"]

    @property
    def gustMPH(self) -> float:
        """ The maximum wind gust in miles per hour. Null if not available. """
        return self.wind["gustMPH"]

    @property
    def count(self) -> int:
        """ The total number of observations that included wind information. """
        return self.wind["count"]
