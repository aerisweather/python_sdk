

class ObservationsSummaryTemp:
    """ Defines an object for the observations summary period temp data. """

    temp = {}

    def __init__(self, temp_json):
        """
        Constructor - this takes an individual observations summary period's temperature json.
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

        self.temp = temp_json

    @property
    def maxC(self) -> float:
        """  The maximum temperature in Celsius. Null if unavailable. """
        return self.temp["maxC"]

    @property
    def maxF(self) -> float:
        """  The maximum temperature in Fahrenheit. Null if unavailable. """
        return self.temp["maxF"]

    @property
    def minC(self) -> float:
        """  The minimum temperature in Celsius. Null if unavailable. """
        return self.temp["minC"]

    @property
    def minF(self) -> float:
        """  The minimum temperature in Fahrenheit. Null if unavailable. """
        return self.temp["minF"]

    @property
    def avgC(self) -> float:
        """  The average temperature in Celsius. Null if unavailable. """
        return self.temp["avgC"]

    @property
    def avgF(self) -> float:
        """  The average temperature in Fahrenheit. Null if unavailable. """
        return self.temp["avgF"]

    @property
    def count(self) -> int:
        """ The total number of observations that included temperature information. """
        return self.temp["count"]
