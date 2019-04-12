

class Pollutant:
    """Defines an object for the Aeris API Ait Quality pollutant data returned in an Aeris API responses"""

    data = {}

    def __init__(self, json_data):
        """ Constructor """
        self.data = json_data

    @property
    def type(self) -> str:
        """ The type abbreviation of the pollutant:
                co = carbon monoxide
                no2 = nitrogen dioxide
                o3 = ozone
                pm1 = partical matter (<1µm)
                pm10 = partical matter (<10µm)
                pm2.5 = partical matter (<2.5µm)
                so2 = sulfer dioxide """
        return self.data["type"]

    @property
    def name(self) -> str:
        """ Name of the pollutant """
        return self.data["name"]

    @property
    def valuePPB(self):
        """ The pollutant measurement in parts per billion. Null if this unit is not utilized
                pm2.5 & pm10 do not utilize PPB. """
        return self.data["valuePPB"]

    @property
    def valueUGM3(self):
        """ The pollutant measurement in parts per micrograms per cubic meter. Null if this unit is not utilized. """
        return self.data["valueUGM3"]

    @property
    def aqi(self) -> int:
        """  The pollutant measurement converted to the common AQI value, from 0 to 500 """
        return self.data["aqi"]

    @property
    def category(self) -> str:
        """ The Air Quality category based on the AQI """
        return self.data["category"]

    @property
    def color(self) -> str:
        """ The 6 character hexadecimal color code for the specific category. """
        return self.data["color"]