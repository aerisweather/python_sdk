

class ObservationsSummaryVisibility:
    """ Defines an object for the observations summary period visibility data. """

    vis = {}

    def __init__(self, vis_json):
        """
        Constructor - this takes an individual observations summary period's visibility json.
               {
                  maxKM": 16,
                  "maxMI": 10,
                  "minKM": 3,
                  "minMI": 2,
                  "count": 23,
                  "avgKM": 11,
                  "avgMI": 6.8
                },
        """

        self.vis = vis_json

    @property
    def maxKM(self) -> float:
        """ The maximum visibility in kilometers. Null if not available. """
        return self.vis["maxKM"]

    @property
    def maxMI(self) -> float:
        """ The maximum visibility in miles. Null if not available. """
        return self.vis["maxMI"]

    @property
    def minKM(self) -> float:
        """ The minimum visibility in kilometers. Null if not available. """
        return self.vis["minKM"]

    @property
    def minMI(self) -> float:
        """ The minimum visibility in miles. Null if not available. """
        return self.vis["minMI"]

    @property
    def avgKM(self) -> float:
        """ The average visibility in kilometers. Null if not available. """
        return self.vis["avgKM"]

    @property
    def avgMI(self) -> float:
        """ The average visibility in miles. Null if not available. """
        return self.vis["avgMI"]

    @property
    def count(self) -> int:
        """ The total number of observations that included visibility information. """
        return self.vis["count"]
