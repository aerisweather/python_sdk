from typing import Dict

from aenum import Enum

from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestAction import RequestAction
from aerisweather.requests.RequestFilter import RequestFilter
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.requests.RequestQuery import RequestQuery
from aerisweather.requests.RequestSort import RequestSort


class EndpointType(Enum):
    """ Defines the available endpoints for Aeris API requests. """

    ALERTS = "advisories"
    CONVECTIVE_OUTLOOK = "convective/outlook"
    FORECASTS = "forecasts"
    OBSERVATIONS = "observations"
    OBSERVATIONS_SUMMARY = "observations/summary"
    PLACES = "places"
    CUSTOM = "custom"

    # def __init__(self):
    __custom_endpoint_type_name = ""

    @property
    def custom(self):
        """ Returns the string name of the custom/generic endpoint used when CUSTOM is the endpoint type """
        return self.__custom_endpoint_type_name

    @custom.setter
    def custom(self, endpoint_type: str):
        """ Sets the string name of the custom/generic endpoint used when CUSTOM is the endpoint type """
        self.__custom_endpoint_type_name = endpoint_type


class Endpoint:
    """ Defines an object used to hold and transfer information regarding a specific Aeris API endpoint """

    def __init__(self,
                 endpoint_type: EndpointType = None,
                 location: RequestLocation = None,
                 action: RequestAction = None,
                 filter_: [RequestFilter] = None,
                 sort: RequestSort = None,
                 params: Dict[ParameterType, str] = None,
                 query: Dict[RequestQuery, str] = None):
        """ Constructor"""

        self.endpoint_type = endpoint_type
        self.location = location
        self.action = action
        self.filter_ = filter_
        self.sort = sort
        self.params = params
        self.query = query





