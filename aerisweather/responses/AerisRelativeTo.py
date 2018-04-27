

class AerisRelativeTo:
    """Defines the base class for Aeris API relative position data returned in an Aeris API responses"""

    def __init__(self, json_data):
        """ Constructor """
        self.data = json_data

    @property
    def lat(self):
        """ Returns the Latitude coordinate of the location used for the requests """
        return self.data["lat"]

    @property
    def long(self):
        """ Returns the Longitude coordinate of the location used for the requests """
        return self.data["long"]

    @property
    def bearing(self):
        """ Returns the Bearing in degrees of the record's location relative to the location used for the requests """
        return self.data["bearing"]

    @property
    def bearingENG(self):
        """ Returns the Cardinal direction of the record relative to the location used for the requests. """
        return self.data["bearingENG"]

    @property
    def distanceKM(self):
        """ Returns the Distance, in kilometers, from the requested location to the record's actual location. """
        return self.data["distanceKM"]

    @property
    def distanceMI(self):
        """ Returns the Distance, in miles, from the requested location to the record's actual location. """
        return self.data["distanceMI"]
