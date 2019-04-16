

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
    def coordinates(self):
        """ Returns the coordinates data from a geojson response. Can be one or more sets or groups of coordinates
         too, if there are multiple polygons.

         Example 1, Single polygon:

         "coordinates": [
              [
                -91.42,
                44.01
              ],
              [
                -91.2,
                43.88
              ],
              [
                -91.22,
                43.57
              ]
        ]

        Example 2, Multiple polygons:

            "coordinates": [
            [
                [
                    -91.42,
                    44.01
                ],
                [
                    -91.2,
                    43.88
                ]
            ],
            [
                [
                    -91.22,
                    43.57
                ],
                [
                    -91.27,
                    43.61
                ]
            ]
        ]
        """
        return self.data["coordinates"]
