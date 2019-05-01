from typing import List

from aerisweather.responses.AerisRelativeTo import AerisRelativeTo
from aerisweather.responses.Geometry import Geometry
from aerisweather.responses.Response import Response
from aerisweather.responses.TropicalCyclonesBreakPointAlerts import TropicalCyclonesBreakPointAlerts
from aerisweather.responses.TropicalCyclonesForecast import TropicalCyclonesForecast
from aerisweather.responses.TropicalCyclonesPosition import TropicalCyclonesPosition
from aerisweather.responses.TropicalCyclonesProfile import TropicalCyclonesProfile
from aerisweather.responses.TropicalCyclonesTrack import TropicalCyclonesTrack


class TropicalCyclonesResponse(Response):
    """ Defines an object for the data returned in an Aeris API response."""

    data = {}

    def __init__(self, json_data=None):
        """Constructor - Takes a single response json object from an Aeris API data response. """

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
    def track(self) -> List[TropicalCyclonesTrack]:
        tracks = self.data["track"]

        t_list = []  # type: [TropicalCyclonesTrack]
        for per in tracks:
            t = TropicalCyclonesTrack(per)
            t_list.append(t)

        return t_list

    @property
    def forecast(self) -> List[TropicalCyclonesForecast]:
        forecasts = self.data["forecast"]

        f_list = []  # type: [TropicalCyclonesForecast]
        for per in forecasts:
            f = TropicalCyclonesForecast(per)
            f_list.append(f)

        return f_list

    @property
    def breakPointAlerts(self) -> List[TropicalCyclonesBreakPointAlerts]:
        breaks = self.data["breakPointAlerts"]

        b_list = []  # type: [TropicalCyclonesBreakPointAlerts]
        for per in breaks:
            b = TropicalCyclonesBreakPointAlerts(per)
            b_list.append(b)

        return b_list

    @property
    def errorCone(self) -> Geometry:
        return Geometry(self.data['errorCone'])

    @property
    def relativeTo(self) -> AerisRelativeTo:
        return AerisRelativeTo(self.data['relativeTo'])
