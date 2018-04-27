
from aerisweather.utils import AerisDateTime


class RiversLowWaterRecords:
    """Defines an object for the Aeris API rivers low water records data returned in an Aeris API responses"""

    data = {}

    def __init__(self, json_data):
        """Constructor"""
        self.data = json_data

    @property
    def timestamp(self):
        """Returns the unix timestamp of the date the low water record occurred"""
        return self.data["timestamp"]

    @property
    def dateTimeISO(self):
        """Returns a Pyton DateTime object with the date time the low water record occurred"""
        return AerisDateTime.AerisDateTime().get_datetime_from_aeris_iso(self.data["dateTimeISO"])

    @property
    def heightFT(self):
        """Returns the water height in feet of the low water record"""
        return self.data["heightFT"]

    @property
    def heightM(self):
        """Returns the water height in meters of the low water record"""
        return self.data["heightM"]
