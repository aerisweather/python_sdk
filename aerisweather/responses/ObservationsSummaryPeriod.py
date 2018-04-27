
from aerisweather.responses.ObservationsSummaryDewPt import ObservationsSummaryDewPt
from aerisweather.responses.ObservationsSummaryPrecip import ObservationsSummaryPrecip
from aerisweather.responses.ObservationsSummaryPressure import ObservationsSummaryPressure
from aerisweather.responses.ObservationsSummaryQC import ObservationsSummaryQC
from aerisweather.responses.ObservationsSummaryRange import ObservationsSummaryRange
from aerisweather.responses.ObservationsSummaryRelativeHumidity import ObservationsSummaryRelativeHumidity
from aerisweather.responses.ObservationsSummarySky import ObservationsSummarySky
from aerisweather.responses.ObservationsSummarySolrad import ObservationsSummarySolrad
from aerisweather.responses.ObservationsSummaryStationPressure import ObservationsSummaryStationPressure
from aerisweather.responses.ObservationsSummaryTemp import ObservationsSummaryTemp
from aerisweather.responses.ObservationsSummaryVisibility import ObservationsSummaryVisibility
from aerisweather.responses.ObservationsSummaryWeather import ObservationsSummaryWeather
from aerisweather.responses.ObservationsSummaryWind import ObservationsSummaryWind


class ObservationsSummaryPeriod:
    """ Defines an object for the observations summary period data. """

    period = {}

    def __init__(self, period_json):
        """
        Constructor - this takes an individual observations summary period's json.
                        {
                        "timestamp": 1521543600,
                        "dateTimeISO...
        """

        self.summary = period_json["summary"]

    @property
    def timestamp(self) -> int:
        """ UNIX timestamp of the summary. Midnight local time. """
        return self.summary["timestamp"]

    @property
    def dateTimeISO(self) -> str:
        """ ISO 8601 of the valid time of the summary. """
        return self.summary["dateTimeISO"]

    @property
    def ymd(self) -> int:
        """ The year, month and date in YYYYMMDD format. Example: Jan 7, 2014: 20140107 """
        return self.summary["ymd"]

    @property
    def range(self) -> ObservationsSummaryRange:
        """ Returns an ObservationsSummaryRange object """
        return ObservationsSummaryRange(self.summary["range"])

    @property
    def temp(self) -> ObservationsSummaryTemp:
        """ Returns an ObservationsSummaryTemp object """
        return ObservationsSummaryTemp(self.summary["temp"])

    @property
    def dewpt(self) -> ObservationsSummaryDewPt:
        """ Returns an ObservationsSummaryDewPt object """
        return ObservationsSummaryDewPt(self.summary["dewpt"])

    @property
    def rh(self) -> ObservationsSummaryRelativeHumidity:
        """ Returns an ObservationsSummaryRelativeHumidity object """
        return ObservationsSummaryRelativeHumidity(self.summary["rh"])

    @property
    def pressure(self) -> ObservationsSummaryPressure:
        """ Returns an ObservationsSummaryPressure object """
        return ObservationsSummaryPressure(self.summary["pressure"])

    @property
    def spressure(self) -> ObservationsSummaryStationPressure:
        """ Returns an ObservationsSummaryStationPressure object """
        return ObservationsSummaryStationPressure(self.summary["spressure"])

    @property
    def weather(self) -> ObservationsSummaryWeather:
        """ Returns an ObservationsSummaryWeather object """
        return ObservationsSummaryWeather(self.summary["weather"])

    @property
    def visibility(self) -> ObservationsSummaryVisibility:
        """ Returns an ObservationsSummaryVisibility object """
        return ObservationsSummaryVisibility(self.summary["visibility"])

    @property
    def wind(self) -> ObservationsSummaryWind:
        """ Returns an ObservationsSummaryWind object """
        return ObservationsSummaryWind(self.summary["wind"])

    @property
    def precip(self) -> ObservationsSummaryPrecip:
        """ Returns an ObservationsSummaryPrecip object """
        return ObservationsSummaryPrecip(self.summary["precip"])

    @property
    def sky(self) -> ObservationsSummarySky:
        """ Returns an ObservationsSummarySky object """
        return ObservationsSummarySky(self.summary["sky"])

    @property
    def solrad(self) -> ObservationsSummarySolrad:
        """ Returns an ObservationsSummarySolrad object """
        return ObservationsSummarySolrad(self.summary["solrad"])

    @property
    def QC(self) -> ObservationsSummaryQC:
        """ Returns an ObservationsSummaryQC object """
        return ObservationsSummaryQC(self.summary["QC"])
