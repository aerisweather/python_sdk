

class ThreatsStormsDistance:

    data = {}

    def __init__(self, json):
        """ Constructor """

        self.data = json

    @property
    def minKM(self):
        if self.data is not None:
            return self.data["minKM"]

    @property
    def minMI(self):
        if self.data is not None:
            return self.data["minMI"]

    @property
    def maxKM(self):
        if self.data is not None:
            return self.data["maxKM"]

    @property
    def maxMI(self):
        if self.data is not None:
            return self.data["maxMI"]

    @property
    def avgKM(self):
        if self.data is not None:
            return self.data["avgKM"]

    @property
    def avgMI(self):
        if self.data is not None:
            return self.data["avgMI"]