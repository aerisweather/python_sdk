

class RequestLocation:
    """
    Defines an object to store the location that we requesting data for. Using this class instead of just passing
    a str allows us to provide additional guidance as to the acceptable/required members of a proper location.
    Also, the location_str method allows us to generate the most accurate location based on the data the user provides.

    The location can be defined in one of three ways:
        - provide both latitude and longitude
        or
        - provide both ciy and state
        or
        provide a postal code (US or Canada only)
    """

    def __init__(self,
                 city: str=None,
                 state: str=None,
                 latitude: float=None,
                 longitude: float=None,
                 postal_code: str=None):
        """ Constructor """

        self.city = city
        self.state = state
        self.latitude = latitude
        self.longitude = longitude
        self.postal_code = postal_code

    def __str__(self):
        """ Build and return the most accurate location string from the variables known. """
        self.location_str()

    def location_str(self) -> str:
        """ Build and return the most accurate location string from the variables known. """

        ret = ""

        if self.latitude is not None and self.longitude is not None:
            ret = str(self.latitude) + "," + str(self.longitude)

        elif self.postal_code is not None:
            ret = self.postal_code

        elif self.city is not None and self.state is not None:
            ret = self.city + "," + self.state

        return ret
