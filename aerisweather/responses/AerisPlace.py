

class AerisPlace:
    """ Defines an object for the Aeris API place data returned in an Aeris API response """

    def __init__(self, json_data):
        """ Constructor """
        self.data = json_data

    @property
    def name(self):
        """Returns the string name of the place"""
        return self.data["name"]

    @property
    def state(self):
        """ The abbreviated state or province for the location. """
        return self.data["state"]

    @property
    def country(self):
        """ The abbreviated country for the location. """
        return self.data["country"]


class AerisPlacePlaces(AerisPlace):
    """ Defines an object for the API Place data returned in a Places response """
    @property
    def stateFull(self):
        """ The full state or province for the location. """
        return self.data["stateFull"]

    @property
    def countryFull(self):
        """ The abbreviated country for the location. """
        return self.data["countryFull"]

    @property
    def region(self):
        """ The region for the location (primarily for US-based locations). """
        return self.data["region"]

    @property
    def regionFull(self):
        """ The full region for the location (primarily for US-based locations). """
        return self.data["regionFull"]

    @property
    def continent(self):
        """ The continent abbreviation the location belongs to. """
        return self.data["continent"]

    @property
    def continentFull(self):
        """ The full continent abbreviation the location belongs to. """
        return self.data["continentFull"]
