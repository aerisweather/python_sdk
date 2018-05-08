""" The @skip annotation allows us to create a nested enum structure, without including the child enums in the
 top level enum list. """

from aenum import Enum, skip


class RequestSort(Enum):
    """ Defines the available sort options for each Aeris API endpoint's requests.

        For details on the use of each sort value, see the Sorting secton of the corresponding endpoint, such
            as the Observations endpoint's sorts found here:
            https://www.aerisweather.com/support/docs/api/reference/endpoints/observations/#sorting.
    """

    @skip
    class ALERTS (Enum):
        COUNTRY = "country"
        DEWPT = "dewpt"
        GUST = "gust"
        ID = "id"
        NAME = "name"
        PRESSURE = "pressure"
        RH = "rh"
        STATE = "state"
        TEMP = "temp"
        WIND = "wind"
        WIN_DIR = "winddir"

    @skip
    class CONVECTIVE_OUTLOOK (Enum):
        ALL = "all"
        ALLHAIL = "allhail"
        ALLTORN = "alltorn"
        ALLWIND = "allwind"
        CAT = "cat"
        CONHAZO = "conhazo"
        DAY1 = "day1"
        DAY2 = "day2"
        DAY3 = "day3"
        DAY4 = "day4"
        DAY5 = "day5"
        DAY6 = "day6"
        DAY7 = "day7"
        DAY8 = "day8"
        ENHANCED = "enhanced"
        GENERAL = "general"
        HAIL = "hail"
        HIGH = "high"
        MARGINAL = "marginal"
        MODERATE = "moderate,mod"
        PROB = "prob"
        SLIGHT = "slight"
        TORN = "torn"
        WIND = "wind"
        XHAIL = "xhail,sighail"
        XTORN = "xtorn,sigtorn"
        XWIND = "xwind.sigwind"

    # Forecast Endpoint has no defined query items
    # class FORECASTS (Enum):

    @skip
    class OBSERVATIONS(Enum):
        CLOSEST = "closest"
        ID = "id"
        ROUTE = "route"
        SEARCH = "search"
        WITHIN = "within"

    # ObservationsSummary Endpoint has no defined query items
    # class OBSERVATIONS_SUMMARY (Enum):

    @skip
    class PLACES(Enum):
        COUNTRY = "country"
        HAS_ZIP = "haszip"
        POP = "pop"
        NAME = "name"
        STATE = "state"
