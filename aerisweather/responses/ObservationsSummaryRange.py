

class ObservationsSummaryRange:
    """ Defines an object for the observations summary period range data. """

    range = {}

    def __init__(self, range_json):
        """
        Constructor - this takes an individual observations summary period's range json.
               {
                  "maxTimestamp": 1523299980,
                  "maxDateTimeISO": "2018-04-09T13:53:00-05:00",
                  "minTimestamp": 1523253180,
                  "minDateTimeISO": "2018-04-09T00:53:00-05:00",
                  "count": 23
                },
        """

        self.range = range_json

    @property
    def maxTimestamp(self) -> int:
        """ UNIX timestamp of the maximum (latest) observation time in the summary. """
        return self.range["maxTimestamp"]

    @property
    def maxDateTimeISO(self) -> str:
        """ ISO 8601 of the maximum (latest) observation time in the summary. """
        return self.range["maxDateTimeISO"]

    @property
    def minTimestamp(self) -> int:
        """ UNIX timestamp of the minimum (earliest) observation time in the summary. """
        return self.range["minTimestamp"]

    @property
    def minDateTimeISO(self) -> str:
        """ ISO 8601 of the minimum (earliest) observation time in the summary. """
        return self.range["minDateTimeISO"]

    @property
    def count(self) -> int:
        """ The total number of observations used to make the summary. """
        return self.range["count"]
