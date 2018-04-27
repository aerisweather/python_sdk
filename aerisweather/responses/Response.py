
from aerisweather.responses.AerisLocation import AerisLocation


class Response:
    """ Defines the base Response object for the data returned from the Aeris API. """

    data = {}

    def __init__(self, json_data=None):
        """Constructor"""

        self.data = json_data
        self.error = None

    @property
    def loc(self)->AerisLocation:
        """ Returns a location json object. """
        loc = AerisLocation(self.data["loc"])
        return loc
