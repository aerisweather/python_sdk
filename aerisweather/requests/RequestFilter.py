""" The @skip annotation allows us to create a nested enum structure, without including the child enums in the
 top level enum list. """

from aenum import Enum, skip


class RequestFilter(Enum):
    """ Defines the available filters for each Aeris API endpoint's requests.

        For details on the use of each filter value, see the Filters secton of the corresponding endpoint, such
            as the Forecasts endpoint's filters found here:
            https://www.aerisweather.com/support/docs/api/reference/endpoints/forecasts/#filters.
    """

    @skip
    class ALERTS(Enum):
        ADVISORY = "advisory"
        ALL = "all"
        ALL_COUNTRIES = "allcountries"
        BEACH = "beach"
        CANADA = "canada"
        COUNTY = "county"
        DISTINCT = "distinct"
        EMERGENCY = "emergency"
        FIRE = "fire"
        FLOOD = "flood"
        FORECAST = "forecast"
        HAS_SMALL_POLY = "hassmallpoly"
        MARINE = "marine"
        NON_MARINE = "nonmarine"
        NON_PRECIP = "nonprecip"
        NOW = "now"
        OUTLOOK = "outlook"
        STATEMENT = "statement"
        SEVERE = "severe"
        SYNOPSIS = "synopsis"
        TORNADO = "tornado"
        TROPICAL = "tropical"
        TSUNAMI = "tsunami"
        WARNING = "warning"
        WATCH = "watch"
        WIND = "wind"
        WINTER = "winter"
        USA = "usa"

    @skip
    class CONVECTIVE_OUTLOOK(Enum):
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

    @skip
    class FORECASTS(Enum):
        DAY = "day"
        DAY_NIGHT = "daynight"
        HR = "#hr"
        PRECISE = "precise"

    @skip
    class OBSERVATIONS(Enum):
        ALL_STATIONS = "allstations"
        ALLOW_NO_SKY = "allownosky"
        HAS_PRECIP = "hasprecip"
        METAR = "metar"
        MESONET = "mesonet"
        PWS = "pws"

    @skip
    class OBSERVATIONS_SUMMARY(Enum):
        ALL_STATIONS = "allstations"
        HAS_PRECIP = "hasprecip"
        MESONET = "mesonet"
        METAR = "metar"
        OFFICAL = "official"
        PWS = "pws"

    @skip
    class PLACES(Enum):
        AIRPORT = "airport"
        AMUSEMENT = "amusement"
        BRIDGE = "bridge"
        CAMP = "camp"
        CHURCH = "church"
        COUNTY = "county"
        DIVISIONS = "divisions"
        FEATURE = "feature"
        FORT = "fort"
        GOLF = "golf"
        LAKE = "lake"
        NEIGHBORHOOD = "neighborhood"
        PARISH = "parish"
        PARK = "park"
        POINTS_OF_INTEREST = "poi"
        PORT = "port"
        POPULATED_PLACES = "ppl"
        RESERVE = "reserve"
        SCHOOL = "school"
        STADIUM = "stadium"
        TEMPLE = "temple"
        TRAIL = "trail"
        TUNNEL = "tunnel"
        UNIVERSITY = "university"
        WORSHIP = "worship"
