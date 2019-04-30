from aerisweather.responses.Response import Response


class TropicalCyclonesResponse(Response):
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

        super().__init__(json_data=json_data)
        self.data = json_data

    @property
    def id(self):
        return self.data["id"]

    @property
    def profile(self) -> TropicalCyclonesProfile:
        return TropicalCyclonesProfile(self.data["profile"])

    @property
    def position(self) -> TropicalCyclonesPosition:
        return TropicalCyclonesPosition(self.data["position"])

    @property
    def track(self) -> TropicalCyclonesTrack:
        return TropicalCyclonesTrack(self.data["track"])

    @property
    def forecast(self) -> TropicalCyclonesForecast:
        return TropicalCyclonesForecast(self.data["forecast"])

    @property
    def breakPointAlerts(self) -> TropicalCyclonesBreakPointAlerts:
        return TropicalCyclonesBreakPointAlerts(self.data["breakPointAlerts"])

    @property
    def errorCone(self) -> TropicalCyclonesErrorCone:
        return TropicalCyclonesErrorCone(self.data["errorCone"])
