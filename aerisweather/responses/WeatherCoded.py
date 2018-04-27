
class WeatherCoded:
    """ Defines an object for the weather coded json returned in an Aeris API forecast response """

    data = {}

    def __init__(self, json_data=None):
        """Constructor"""

        self.data = json_data

    @property
    def timestamp(self) -> int:
        """ UNIX timestamp for the beginning of this period. """
        return self.data["timestamp"]

    @property
    def wx(self) -> str:
        """ Returns the description text of the error """
        return self.data["wx"]

    @property
    def dateTimeISO(self) -> str:
        """ ISO 8601 of the valid time """
        return self.data["dateTimeISO"]
