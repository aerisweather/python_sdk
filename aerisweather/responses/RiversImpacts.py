

class RiversImpacts:
    """Defines an object for the Aeris API rivers impacts data returned in an Aeris API responses"""

    data = {}

    def __init__(self, json_data):
        """ Constructor """
        self.data = json_data

    @property
    def heightFT(self):
        """Returns the height in feet that the impact begins to occur."""
        return self.data["heightFT"]

    @property
    def getHeightM(self):
        """Returns the height in meters that the impact begins to occur."""
        return self.data["heightM"]

    @property
    def getText(self):
        """Returns the impact description"""
        return self.data["text"]
