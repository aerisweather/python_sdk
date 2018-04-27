from aerisweather.responses import RiversCrestsHistoric, RiversCrestsRecent


class RiversCrests:
    """ Defines an object for the Aeris API rivers crests data returned in an Aeris API responses """

    def __init__(self, json_data):
        """ Constructor """
        self.data = json_data

    @property
    def recent(self):
        """Returns an array of recent crests objects"""
        recent_crests = []

        for crest in self.data["recent"]:
            rcrest = RiversCrestsRecent.RiversCrestsRecent(crest)
            recent_crests.append(rcrest)
        
        return recent_crests

    @property
    def historic(self):
        """Returns an array of historic crests"""
        historic_crests = []

        for crest in self.data["historic"]:
            hist_crest = RiversCrestsHistoric.RiversCrestsHistoric(crest)
            historic_crests.append(hist_crest)

        return historic_crests
