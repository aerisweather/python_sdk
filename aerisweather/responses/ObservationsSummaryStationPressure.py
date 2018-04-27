

class ObservationsSummaryStationPressure:
    """ Defines an object for the observations summary period station pressure data. """

    pressure = {}

    def __init__(self, pressure_json):
        """
        Constructor - this takes an individual observations summary period's station pressure json.
               {
                  "maxMB": 1024,
                  "maxIN": 30.24,
                  "minMB": 1020,
                  "minIN": 30.12,
                  "avgMB": 1021.4,
                  "avgIN": 30.16,
                  "count": 23
                },
        """

        self.pressure = pressure_json

    @property
    def maxMB(self) -> int:
        """ The maximum MSLP in millibars. Null if not available. """
        return self.pressure["maxMB"]

    @property
    def maxIN(self) -> float:
        """ The maximum MSLP in inches mercury. Null if not available. """
        return self.pressure["maxIN"]

    @property
    def minMB(self) -> int:
        """ The minimum MSLP in millibars. Null if not available. """
        return self.pressure["minMB"]

    @property
    def minIN(self) -> float:
        """ The minimum MSLP in inches mercury. Null if not available. """
        return self.pressure["minIN"]

    @property
    def avgMB(self) -> int:
        """ The average MSLP in millibars. Null if not available. """
        return self.pressure["avgMB"]

    @property
    def avgIN(self) -> float:
        """ The average MSLP in inches mercury. Null if not available. """
        return self.pressure["avgIN"]

    @property
    def count(self) -> int:
        """ The total number of observations that included pressure information. """
        return self.pressure["count"]
