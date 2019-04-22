
from .CommonEndpointImports import *


class CustomEndpoint(object):
    """ Defines the curtesy function for requesting data from the API that is not provided by one of the standard
    endpoint functions. """

    def custom_endpoint(self,
                        location: RequestLocation = None,
                        action: RequestAction = None,
                        filter_: [RequestFilter] = None,
                        sort: RequestSort = None,
                        params: Dict[ParameterType, str] = None,
                        query: Dict[RequestQuery, str] = None,
                        format_: RequestFormat = None):
        """ Performs an API request to get custom endpoint data for a specified location.

            When calling custom_endpoint, in addition to setting the EndpointType of the Endpoint object to CUSTOM,
                the EndpointType.custom value must be set to the string value of the endpoint you are requesting. See
                the examples section to see hwo this is done.

            Params:
                - location: Optional - RequestLocation - the location for which the request is processed
                - action: Optional - RequestAction - the API request action option
                - filter_: Optional - [RequestFilter] - a list of API request filters
                - sort: Optional - RequestSort - the API request sort option
                - params: Optional - Dict[ParameterType, str] - a list of API request parameters
                - query: Optional - Dict[RequestQuery, str] - a list of API request quesries
                - format_: Optional - RequestFormat - the API request format option (json (default) or geojson)

            Returns:
                - a list of CustomResponse objects if successful
                - an empty list if there is no data

            Examples:
                # You can also use the custom endpoint type to request data from a known valid endpoint, for cases
                # where new API data fields have not yet been added to an endpoint's response class.
                EndpointType.custom = "forecasts"
                f_list = awx.request(endpoint=Endpoint(endpoint_type=EndpointType.CUSTOM,
                                                       location=RequestLocation(postal_code="54660")))
                forecast = f_list[0]
                period = forecast.periods[0]  # type: ForecastPeriod

                # Valid endpoint, not in our Endpoint Enum - run this to test a beta or pre-release endpoint
                EndpointType.custom = "stormreports"
                endpt = Endpoint(EndpointType.CUSTOM, location=RequestLocation(postal_code="54660"))
                resp_list = awx.request(endpt)
                response = resp_list[0]
        """

        endpoint = Endpoint(endpoint_type=EndpointType.CUSTOM,
                            location=location,
                            action=action,
                            filter_=filter_,
                            sort=sort,
                            params=params,
                            query=query,
                            format_=format_)

        return self.request(endpoint=endpoint)
