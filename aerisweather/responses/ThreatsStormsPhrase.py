

class ThreatsStormsPhrase:

    data = {}

    def __init__(self, json):
        """ Constructor """

        self.data = json

    @property
    def long(self):
        if self.data is not None:
            return self.data["long"]

    @property
    def short(self):
        if self.data is not None:
            return self.data["short"]
