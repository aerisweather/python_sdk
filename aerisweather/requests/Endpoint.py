from typing import Dict

from aenum import Enum

from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestAction import RequestAction
from aerisweather.requests.RequestFilter import RequestFilter
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.requests.RequestQuery import RequestQuery
from aerisweather.requests.RequestSort import RequestSort


class EndpointType(Enum):
    """ Defines the available endpoints for Aeris API requests.

        When requesting data from an unimplemented endpoint, use the CUSTOM type and set the name of the endpoint
            using the "custom" property.

        Examples:
            # ObservationSummary
            endpoint = Endpoint(endpoint_type=EndpointType.OBSERVATIONS_SUMMARY)

            # Custom Endpoint
            EndpointType.custom = "stormreports"
            endpt = Endpoint(EndpointType.CUSTOM, location=RequestLocation(postal_code="54660"))
    """

    ALERTS = "advisories"
    CONDITIONS = "conditions"
    CONVECTIVE_OUTLOOK = "convective/outlook"
    FORECASTS = "forecasts"
    OBSERVATIONS = "observations"
    OBSERVATIONS_SUMMARY = "observations/summary"
    PLACES = "places"
    CUSTOM = "custom"

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





