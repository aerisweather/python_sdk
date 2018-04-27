

class ObservationsSummaryPrecip:
    """ Defines an object for the observations summary period precip data. """

    precip = {}

    def __init__(self, precip_json):
        """
        Constructor - this takes an individual observations summary period's precip json.
               {
                  "totalMM": 0.25,
                  "totalIN": 0.01,
                  "count": 12,
                  "trace": true,
                  "traceCount": 9,
                  "QC": "G",
                  "method": "sum",
                  "QCcode": 10
                },
        """

        self.precip = precip_json

    @property
    def totalMM(self) -> float:
        """  The total liquid equivalent precipitation in millimeters. Null if not available. """
        return self.precip["totalMM"]

    @property
    def totalIN(self) -> float:
        """  The total liquid equivalent precipitation in inches. Null if not available. """
        return self.precip["totalIN"]

    @property
    def trace(self) -> bool:
        """ True if at least one observation reported a trace of precipitation.. """
        return self.precip["trace"]

    @property
    def traceCount(self) -> int:
        """  The total number of observations that reported a trace of precipitation. """
        return self.precip["traceCount"]

    @property
    def QC(self) -> str:
        return self.precip["QC"]

    @property
    def method(self) -> str:
        return self.precip["method"]

    @property
    def QCcode(self) -> int:
        return self.precip["QCcode"]

    @property
    def count(self) -> int:
        """ The total number of observations that included temperature information. """
        return self.precip["count"]
