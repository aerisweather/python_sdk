

class RiversCategories:
    """ Defines an object for the Aeris API rivers categories data returned in an Aeris API responses """

    def __init__(self, json_data):
        """ Constructor """
        self.data = json_data

    def getActionFT(self):
        """ Returns the height, in feet, when the waterbody nears flood stage """
        return self.data["actionFT"]

    def getActionM(self):
        """ Returns the height, in meters, when the waterbody nears flood stage """
        return self.data["actionM"]

    def getFloodFT(self):
        """ Returns the height, in feet, that flooding begins """
        return self.data["floodFT"]

    def getFloodM(self):
        """ Returns the height, in meters, that flooding begins """
        return self.data["floodM"]

    def getModerateFT(self):
        """ Returns the height, in feet, that moderate flooding begins """
        return self.data["moderateFT"]

    def getModerateM(self):
        """ Returns the height, in meters, that moderate flooding begins """
        return self.data["moderateM"]

    def getMajorFT(self):
        """ Returns the height, in feet, that major flooding begins """
        return self.data["majorFT"]

    def getMajorM(self):
        """ Returns the height, in meters, that major flooding begins """
        return self.data["majorM"]

    def getLowthreshFT(self):
        """ Returns the height, in feet, that the water body is considered to be low """
        return self.data["lowthreshFT"]

    def getLowthreshM(self):
        """ Returns the height, in meters, that the water body is considered to be low """
        return self.data["lowthreshM"]
