from typing import List


class TropicalCyclonesPositionLocation:
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        super().__init__(json_data=json_data)
        self.data = json_data

    @property
    def type(self) -> str:
        return self.data["type"]

    @property
    def coordinates(self) -> List:
        coords = self.data["coordinates"]

        c_list = []  # type: List
        for c in coords:
            c_list.append(c)

        return c_list

