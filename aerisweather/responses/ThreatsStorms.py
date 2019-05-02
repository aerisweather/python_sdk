from aerisweather.responses.ThreatsStormsDBZ import ThreatsStormsDBZ
from aerisweather.responses.ThreatsStormsMDA import ThreatsStormsMDA
from aerisweather.responses.ThreatsStormsSpeed import ThreatsStormsSpeed
from aerisweather.responses.ThreatsStormsDirection import ThreatsStormsDirection
from aerisweather.responses.ThreatsStormsDistance import ThreatsStormsDistance
from aerisweather.responses.ThreatsStormsPhrase import ThreatsStormsPhrase


class ThreatsStorms:

    data = {}

    def __init__(self, json):
        """ Constructor """

        self.data = json

    @property
    def phrase(self) -> ThreatsStormsPhrase:
        if self.data is not None:
            return ThreatsStormsPhrase(self.data["phrase"])

    @property
    def distance(self) -> ThreatsStormsDistance:
        if self.data is not None:
            return ThreatsStormsDistance(self.data["distance"])

    @property
    def direction(self) -> ThreatsStormsDirection:
        if self.data is not None:
            return ThreatsStormsDirection(self.data["direction"])

    @property
    def approaching(self) -> bool:
        return self.data["approaching"]

    @property
    def speed(self) -> ThreatsStormsSpeed:
        if self.data is not None:
            return ThreatsStormsSpeed(self.data["speed"])

    @property
    def span(self) -> int:
        return self.data["span"]

    @property
    def hail(self) -> bool:
        return self.data["hail"]

    @property
    def rotation(self) -> bool:
        return self.data["rotation"]

    @property
    def tornadic(self) -> bool:
        return self.data["tornadic"]

    @property
    def advisories(self):
        return self.data["advisories"]

    @property
    def mda(self) -> ThreatsStormsMDA:
        if self.data is not None:
            return ThreatsStormsMDA(self.data["mda"])

    @property
    def dbz(self) -> ThreatsStormsDBZ:
        if self.data is not None:
            return ThreatsStormsDBZ(self.data["dbz"])