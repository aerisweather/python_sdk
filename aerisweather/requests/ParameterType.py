""" The @skip annotation allows us to create a nested enum structure, without including the child enums in the
 top level enum list. """

from aenum import Enum, skip


class ParameterType(Enum):
    """ Defines the available parameter types for each Aeris API endpoint's requests.

        For details on the use of each parameter value, see the Parameters secton of the corresponding endpoint, such
            as the Forecasts endpoint's parameters found here:
            https://www.aerisweather.com/support/docs/api/reference/endpoints/forecasts/#params.
    """

    @skip
    class ALERTS(Enum):
        CALLBACK = "callback"
        FIELDS = "fields"
        FILTER = "filter"
        FORMAT = "format"
        LIMIT = "limit"
        P = "p"
        QUERY = "query"
        RADIUS = "radius"
        SKIP = "skip"
        SORT = "sort"

    @skip
    class CONDITIONS(Enum):
        P = "p"
        FOR = "for"
        FROM = "from"
        TO = "to"
        PLIMIT = "plimit"
        PSKIP = "pskip"
        PSORT = "psort"

    @skip
    class FORECASTS(Enum):
        CALLBACK = "callback"
        FIELDS = "fields"
        FILTER = "filter"
        FROM = "from"
        LIMIT = "limit"
        P = "p"
        PLIMIT = "plimit"
        PSKIP = "pskip"
        QUERY = "query"
        SKIP = "skip"
        TO = "to"

    @skip
    class OBSERVATIONS(Enum):
        CALLBACK = "callback"
        FIELDS = "fields"
        FILTER = "filter"
        FROM = "from"
        LIMIT = "limit"
        RADIUS = "radius"
        P = "p"
        QUERY = "query"
        SORT = "sort"
        SKIP = "skip"
        TO = "to"

    @skip
    class OBSERVATIONS_SUMMARY (Enum):
        CALLBACK = "callback"
        FIELDS = "fields"
        FILTER = "filter"
        FROM = "from"
        LIMIT = "limit"
        P = "p"
        PLIMIT = "plimit"
        PSKIP = "pskip"
        PSORT = "psort"
        QUERY = "query"
        RADIUS = "radius"
        SORT = "sort"
        SKIP = "skip"
        TO = "to"

    @skip
    class PLACES (Enum):
        CALLBACK = "callback"
        FIELDS = "fields"
        FILTER = "filter"
        FORMAT = "format"
        LIMIT = "limit"
        P = "p"
        QUERY = "query"
        RADIUS = "radius"
        SORT = "sort"
        SKIP = "skip"
