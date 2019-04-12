

class Geometry:
    """ Defines the Geometry object for the geometry data within a geojson response returned from the Aeris API. """

    data = {}

    def __init__(self, geometry_json_data=None):
        """Constructor"""

        self.data = geometry_json_data
        self.error = None

    @property
    def type(self)->str:
        return self.data["type"]

    @property
    def coordinates(self)->[float]:
        return self.data["coordinates"]
