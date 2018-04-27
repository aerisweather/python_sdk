

class ObservationsSummaryQC:
    """ Defines an object for the observations summary period QC data. """

    qc = {}

    def __init__(self, json):
        """
        Constructor - this takes an individual observations summary period's QC json.
               {
                  "max": 10,
                  "min": 10,
                  "types": [
                    "O"
                  ],
                  "count": 23
                },
        """

        self.qc = json

    @property
    def max(self) -> int:
        return self.qc["max"]

    @property
    def min(self) -> int:
        return self.qc["min"]

    @property
    def types(self) -> [str]:
        return self.qc["types"]

    @property
    def count(self) -> int:
        """ Total number of observations that reported QC data. """
        return self.qc["count"]
