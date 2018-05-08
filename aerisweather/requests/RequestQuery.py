""" The @skip annotation allows us to create a nested enum structure, without including the child enums in the
 top level enum list. """

from aenum import Enum, skip


class RequestQuery(Enum):
    """ Defines the available query options for each Aeris API endpoint's requests.

        For details on the use of each query value, see the Queries secton of the corresponding endpoint, such
            as the Observations endpoint's queries found here:
            https://www.aerisweather.com/support/docs/api/reference/endpoints/observations/#queries.
    """

    @skip
    class ALERTS(Enum):
        ACTIVE = "active"
        ADDED = "added"
        BEGINS = "begins"
        COUNTRY = "country"
        EMERGENCY = "emergency"
        EXPIRES = "expires"
        ID = "id"
        ISSUED = "issued"
        LOC = "loc"
        NAME = "name"
        SIG = "sig"
        SIGP = "sigp"
        STATE = "state"
        TYPE = "type"

    # Forecast Endpoint has no defined query items
    # class FORECASTS (Enum):

    @skip
    class OBSERVATIONS (Enum):
        COUNTRY = "country"
        DEWPT = "dewpt"
        ELEV = "elev"
        HAS_PRECIP = "hasprecip"
        ID = "id"
        GUST = "gust"
        NAME = "name"
        PRECIP = "precip"
        PRESSURE = "pressure"
        QC = "qc"
        QC_CODE = "qccode"
        RH = "rh"
        STATE = "state"
        TEMP = "temp"
        WIND = "wind"
        WIND_DIR = "winddir"

    @skip
    class OBSERVATIONS_SUMMARY(Enum):
        AVG_DEWPT = "avgdewpt"
        AVG_PRES = "avgp"
        AVG_RH = "avgrh"
        AVG_VIS = "avgv"
        AVGT = "avgt"
        COUNT = "count"
        COUNTRY = "country"
        DATE = "dt"
        ELEV = "elev"
        GUST = "gust"
        HAS_PRECIP = "hasprecip"
        ID = "id"
        MAX_DEWPT = "maxdewpt"
        MAX_PRES = "maxp"
        MAX_RH = "maxrh"
        MAX_VIS = "maxv"
        MAXT = "maxt"
        MIN_DEWPT = "mindewpt"
        MIN_PRES = "minp"
        MIN_RH = "minrh"
        MIN_VIS = "minv"
        MINT = "mint"
        NAME = "name"
        PRECIP = "precip"
        PRECIPC = "precipc"
        STATE = "state"
        WIND = "wind"

    @skip
    class PLACES(Enum):
        ALT_NAME = "altname"
        COUNTRY = "country"
        NAME = "name"
        POP = "pop"
        STATE = "state"
