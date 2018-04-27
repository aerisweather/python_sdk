""" The @skip annotation allows us to create a nested enum structure, without including the child enums in the
 top level enum list. """

from aenum import Enum, skip


class ParameterType(Enum):
    """ Defines the available parameter types for Aeris API requests. """

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
