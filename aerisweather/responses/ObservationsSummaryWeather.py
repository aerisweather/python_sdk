

class ObservationsSummaryWeather:
    """ Defines an object for the observations summary period weather data. """

    wx = {}

    def __init__(self, json):
        """
        Constructor - this takes an individual observations summary period's weather json.
               {
                  coded": [
                    "::H",
                    ":L:S",
                    "::BR"
                  ],
                  "count": 3,
                  "phrase": "Mostly Cloudy with Haze",
                  "primary": "Haze",
                  "primaryCoded": "::H",
                  "icon": "cloudy.png"
                },
        """

        self.wx = json

    @property
    def coded(self) -> [str]:
        """ Array of observed weather observations. Null if not available. Refer to the coded weather doc
        for possible values. """
        return self.wx["coded"]

    @property
    def phrase(self) -> str:
        """ The general weather phrase for the summary period. Null if not available. """
        return self.wx["phrase"]

    @property
    def primary(self) -> str:
        """ The primary weather string that occurred during the summary period. Null if not available. """
        return self.wx["primary"]

    @property
    def primaryCoded(self) -> str:
        """ The primary weather coded string. Null if not available. Refer to the coded weather doc for
        possible values. """
        return self.wx["primaryCoded"]

    @property
    def icon(self) -> str:
        """ The standard Aeris icon string. Null if not available. """
        return self.wx["icon"]

    @property
    def count(self) -> int:
        """ The total number of observations that reported observed weather. """
        return self.wx["count"]
