

class ThreatsStormsDBZ:

    data = {}

    def __init__(self, json):
        """ Constructor """

        self.data = json

    @property
    def min(self):
        if self.data is not None:
            return self.data["min"]

    @property
    def max(self):
        if self.data is not None:
            return self.data["max"]

    @property
    def avg(self):
        if self.data is not None:
            return self.data["avg"]
