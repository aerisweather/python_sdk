from typing import List


class TropicalCyclonesPositionDetails:
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        super().__init__(json_data=json_data)
        self.data = json_data

    @property
    def basin(self) -> str:
        return self.data["basin"]

    @property
    def stormType(self) -> str:
        return self.data["stormType"]

    @property
    def stormCat(self) -> str:
        return self.data["stormCat"]

    @property
    def stormName(self) -> str:
        return self.data["stormName"]

    @property
    def stormShortName(self) -> str:
        return self.data["stormShortName"]

    @property
    def advisoryNumber(self) -> str:
        return self.data["advisoryNumber"]

    @property
    def movement(self) -> TropicalCyclonesPositionMovement:
        return TropicalCyclonesPositionMovement(self.data["movement"])

    @property
    def windSpeedKTS(self) -> int:
        return self.data["windSpeedKTS"]

    @property
    def windSpeedKPH(self) -> int:
        return self.data["windSpeedKPH"]

    @property
    def windSpeedMPH(self) -> int:
        return self.data["windSpeedMPH"]

    @property
    def gustSpeedKTS(self) -> int:
        return self.data["gustSpeedKTS"]

    @property
    def gustSpeedKPH(self) -> int:
        return self.data["gustSpeedKPH"]

    @property
    def gustSpeedMPH(self) -> int:
        return self.data["gustSpeedMPH"]

    @property
    def pressureMB(self) -> float:
        return self.data["pressureMB"]

    @property
    def pressureIN(self) -> float:
        return self.data["pressureIN"]