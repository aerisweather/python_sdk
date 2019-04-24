from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestAction import RequestAction
from aerisweather.requests.RequestFilter import RequestFilter
from aerisweather.requests.RequestFormat import RequestFormat
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.requests.RequestQuery import RequestQuery
from aerisweather.requests.RequestSort import RequestSort
from aerisweather.endpoints.EndpointType import EndpointType

from typing import Dict


class Endpoint:
    """ Defines an object used to hold and transfer information regarding a specific Aeris API endpoint """

    def __init__(self,
                 endpoint_type: EndpointType = None,
                 location: RequestLocation = None,
                 action: RequestAction = None,
                 filter_: [RequestFilter] = None,
                 sort: RequestSort = None,
                 params: Dict[ParameterType, str] = None,
                 query: Dict[RequestQuery, str] = None,
                 format_: RequestFormat = None):
        """ Constructor

            The Endpoint class can be instantiated with no parameters if configuration is handled later. EndpointTypes
                that have been implemented are defined in the EndpointType enum. Undefined EndpointTypes can be
                requested using the Custom EndpointType.

            Params:
            - endpoint_type: Optional - EndpointType - determines which Aeris API endpoint will be called
            - location: Optional - RequestLocation - the location for which the request is processed
            - action: Optional - RequestAction - the API request action option
            - filter_: Optional - [RequestFilter] - a list of API request filters
            - sort: Optional - RequestSort - the API request sort option
            - params: Optional - Dict[ParameterType, str] - a list of API request parameters
            - query: Optional - Dict[RequestQuery, str] - a list of API request quesries
        """

        self.endpoint_type = endpoint_type
        self.location = location
        self.action = action
        self.filter_ = filter_
        self.sort = sort
        self.params = params
        self.query = query
        self.format_ = format_





