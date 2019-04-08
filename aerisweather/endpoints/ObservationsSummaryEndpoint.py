
from .common_endpoint_imports import *


class ObservationsSummaryEndpoint(object):
    """ Defines the curtesy function for requesting observations summary data from the API. """

    def observations_summary(self,
                             location: RequestLocation = None,
                             action: RequestAction = None,
                             filter_: [RequestFilter] = None,
                             sort: RequestSort = None,
                             params: Dict[ParameterType, str] = None,
                             query: Dict[RequestQuery, str] = None,
                             format_: RequestFormat = None):
        """ Performs an API request to get observations summary data for a specified location.

            Params:
                - location: Optional - RequestLocation - the location for which the request is processed
                - action: Optional - RequestAction - the API request action option
                - filter_: Optional - [RequestFilter] - a list of API request filters
                - sort: Optional - RequestSort - the API request sort option
                - params: Optional - Dict[ParameterType, str] - a list of API request parameters
                - query: Optional - Dict[RequestQuery, str] - a list of API request quesries
                - format_: Optional - RequestFormat - the API request format option (json (default) or geojson)

            Returns:
                - a list of ObservationsSummaryResponse objects if successful
                - an empty list if there is no data
        """

        endpoint = Endpoint(endpoint_type=EndpointType.OBSERVATIONS_SUMMARY,
                            location=location,
                            action=action,
                            filter_=filter_,
                            sort=sort,
                            params=params,
                            query=query,
                            format_=format_)

        return self.request(endpoint=endpoint)