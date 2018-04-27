

class ObservationsSummaryDewPt:
    """ Defines an object for the observations summary period temp data. """

    dewpt = {}

    def __init__(self, dewpt_json):
        """
        Constructor - this takes an individual observations summary period's dewpoint json.
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

        self.dewpt = dewpt_json

    @property
    def maxC(self) -> float:
        """  The maximum dew point in Celsius. Null if unavailable. """
        return self.dewpt["maxC"]

    @property
    def maxF(self) -> float:
        """  The maximum dew point in Fahrenheit. Null if unavailable. """
        return self.dewpt["maxF"]

    @property
    def minC(self) -> float:
        """  The minimum dew point in Celsius. Null if unavailable. """
        return self.dewpt["minC"]

    @property
    def minF(self) -> float:
        """  The minimum dew point in Fahrenheit. Null if unavailable. """
        return self.dewpt["minF"]

    @property
    def avgC(self) -> float:
        """  The average dew point in Celsius. Null if unavailable. """
        return self.dewpt["avgC"]

    @property
    def avgF(self) -> float:
        """  The average dew point in Fahrenheit. Null if unavailable. """
        return self.dewpt["avgF"]

    @property
    def count(self) -> int:
        """ The total number of observations that included dew point information. """
        return self.dewpt["count"]
