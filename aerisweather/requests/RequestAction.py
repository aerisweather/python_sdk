""" The @skip annotation allows us to create a nested enum structure, without including the child enums in the
 top level enum list. """

from aenum import Enum, skip


class RequestAction(Enum):
    """ Defines the available parameter types for Aeris API requests. """

    @skip
    class ALERTS(Enum):
        ID = "id"
        CLOSEST = "closest"
        SEARCH = "search"
        WITHIN = "within"

    @skip
    class CONVECTIVE_OUTLOOK(Enum):
        AFFECTS = "affects"
        CONTAINS = "contains"
        ID = "id"
        SEARCH = "search"

    @skip
    class FORECASTS(Enum):
        ID = "id"
        CLOSEST = "closest"
        ROUTE = "route"

    @skip
    class OBSERVATIONS (Enum):
        CLOSEST = "closest"
        ID = "id"
        ROUTE = "route"
        SEARCH = "search"
        WITHIN = "within"

    @skip
    class OBSERVATIONS_SUMMARY(Enum):
        ID = "id"
        CLOSEST = "closest"
        SEARCH = "search"
        WITHIN = "within"

    @skip
    class PLACES(Enum):
        ID = "id"
        CLOSEST = "closest"
        SEARCH = "search"
        WITHIN = "within"
