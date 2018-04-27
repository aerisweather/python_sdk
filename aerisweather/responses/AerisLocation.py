

class AerisLocation:
    """ Defines an object for the Aeris API loc data returned in an Aeris API responses. """

    def __init__(self, json_data=None):
        """ Constructor """
        self.data = json_data

    @property
    def long(self)->float:
        """ Returns the longitude of the location as a float. """
        return self.data["long"]

    @property
    def lat(self) -> float:
        """ Returns the latitude of the location as a float. """
        return self.data["lat"]
