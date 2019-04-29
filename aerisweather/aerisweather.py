#
#      _
#     /_|   _ __ . _ | /| /  _    _/_ /_   _ __
#    /  | (- /  / _) |/ |/ (- ( \ /  / / (- /
#
#
from typing import Dict, List

from aerisweather.endpoints.AirQualityEndpoint import AirQualityEndpoint
from aerisweather.endpoints.AlertsEndpoint import AlertsEndpoint
from aerisweather.endpoints.CustomEndpoint import CustomEndpoint
from aerisweather.endpoints.ForecastsEndpoint import ForecastsEndpoint
from aerisweather.endpoints.LightningEndpoint import LightningEndpoint
from aerisweather.endpoints.LightningSummaryEndpoint import LightningSummaryEndpoint
from aerisweather.endpoints.ObservationsEndpoint import ObservationsEndpoint
from aerisweather.endpoints.ObservationsSummaryEndpoint import ObservationsSummaryEndpoint
from aerisweather.endpoints.PlacesEndpoint import PlacesEndpoint
from aerisweather.endpoints.Endpoint import Endpoint
from aerisweather.endpoints.EndpointType import EndpointType

from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestAction import RequestAction
from aerisweather.requests.RequestFilter import RequestFilter
from aerisweather.requests.RequestFormat import RequestFormat
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.requests.RequestQuery import RequestQuery
from aerisweather.requests.RequestSort import RequestSort

from aerisweather.responses.AirQualityResponse import AirQualityResponse
from aerisweather.responses.AlertsResponse import AlertsResponse
from aerisweather.responses.CustomResponse import CustomResponse
from aerisweather.responses.ForecastsResponse import ForecastsResponse
from aerisweather.responses.GeoJsonResponse import GeoJsonResponse
from aerisweather.responses.LightningResponse import LightningResponse
from aerisweather.responses.LightningSummaryResponse import LightningSummaryResponse
from aerisweather.responses.ObservationsArchiveResponse import ObservationsArchiveResponse
from aerisweather.responses.ObservationsResponse import ObservationsResponse
from aerisweather.responses.ObservationsSummaryResponse import ObservationsSummaryResponse
from aerisweather.responses.PlacesResponse import PlacesResponse

from aerisweather.utils.AerisError import AerisError
from aerisweather.utils.AerisNetwork import AerisNetwork
from aerisweather.responses.AerisResponseType import ResponseType, AerisResponseType


class AerisWeather(AirQualityEndpoint,
                   AlertsEndpoint,
                   ForecastsEndpoint,
                   LightningEndpoint,
                   LightningSummaryEndpoint,
                   ObservationsEndpoint,
                   ObservationsSummaryEndpoint,
                   PlacesEndpoint,
                   CustomEndpoint):

    """ Defines the main object for the aerisweather python library. """

    def __init__(self,
                 client_id: str,
                 client_secret: str,
                 app_id: str=""):
        """ Constructor

            Params:
                - client_id: AerisWeather API account client id
                - client_secret: AerisWeather API account client secret
                - app_id: Optional - Namespace or application id of the application using this library
        """

        self.app_id = app_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.url_host = "https://api.aerisapi.com/"

        self.location = None
        self.action = None
        self.filter_ = None
        self.sort = None
        self.params = None
        self.query = None
        self.format_ = None

    def request(self, endpoint):
        """ Makes the request to the Aeris API and returns the appropriate response array.

        Builds the API request URL, handles the response json, and raises an AerisError if the API returns an error.

        Params:
            - endpoint: An Endpoint object containing the EndpointType and any other optional parameters needed for
                for the API request.

        Returns:
            - a list of specific response objects, who's type is based on the request data
            - an empty list if there is no data
            - an AerisError object if there was an error condition reported by the api response
            - a URLError if there was an issue with sending the request
            - a generic Exception for all other issues
        """

        url = self.url(endpoint_type=endpoint.endpoint_type,
                       location=endpoint.location,
                       action=endpoint.action,
                       filter_=endpoint.filter_,
                       sort=endpoint.sort,
                       params=endpoint.params,
                       query=endpoint.query,
                       format_=endpoint.format_)

        network = AerisNetwork()
        json_obj = network.get_json(url, self.app_id)

        responses = []

        # Determine if we have a valid data response (json or geojson), or if there is an API error
        response_type = AerisResponseType.get_response_type(json_obj)

        if response_type is ResponseType.JSON:
            # determine if we have one response or an array
            if type(json_obj["response"]) is list:
                for resp in json_obj["response"]:
                    responses.append(self.response(response_type=ResponseType.JSON,
                                                   endpoint_type=endpoint.endpoint_type,
                                                   response_json=resp))
            else:
                responses.append(self.response(ResponseType.JSON, endpoint.endpoint_type, json_obj["response"]))

        elif response_type is ResponseType.GEOJSON:
            for resp in json_obj["features"]:
                responses.append(self.response(ResponseType.GEOJSON, endpoint.endpoint_type, resp))
        else:
            # we have some kind of error or major warning from the API
            raise AerisError.api_error(json_obj)

        return responses

    def url(self,
            endpoint_type: EndpointType,
            location: RequestLocation = None,
            action: RequestAction = None,
            filter_: [RequestFilter] = None,
            sort: RequestSort = None,
            params: Dict[str, str] = None,
            query: Dict[RequestQuery, str]=None,
            format_: RequestFormat = None) -> str:
        """ Generates the appropriate request url for a standard single API request.

        Generally called internally from the request method. Builds and returns a full API request URL based on the
            attributes passed in.

        Params:
            - endpoint_type: EndpointType - determines which Aeris API endpoint will be called
            - location: Optional - RequestLocation - the location for which the request is processed
            - action: Optional - RequestAction - the API request action option
            - filter_: Optional - [RequestFilter] - a list of API request filters
            - sort: Optional - RequestSort - the API request sort option
            - params: Optional - Dict[ParameterType, str] - a list of API request parameters
            - query: Optional - Dict[RequestQuery, str] - a list of API request quesries

        Returns:
            - url string
        """

        url = self.url_host

        if endpoint_type == EndpointType.CUSTOM:
            url += endpoint_type.custom + "/"
        else:
            url += endpoint_type.value + "/"

        if action is not None:
            url += action + "/"
        else:
            url += location.location_str()

        url += "?client_id=" + self.client_id
        url += "&client_secret=" + self.client_secret

        if params is not None:
            for param, value in params.items():
                url += "&" + param + "=" + value

        if sort is not None:
            url += "&sort=" + sort

        if format_ is not None:
            url += "&format=" + format_

        if filter_ is not None:
            if len(filter_) > 0:
                url += "&filter="
                for filt in filter_:
                    url += filt + ","

        out_query = self.query_str(query)

        if out_query is not None:
            url += "&query=" + out_query

        return url

    @staticmethod
    def response(response_type: ResponseType, endpoint_type: EndpointType, response_json):

        if response_type == ResponseType.JSON:
            """ 
            Determines the appropriate response object based on EndpointType and returns the completed response object.
    
            Given the endpoint type and the response json from the Aeris API, the method will return a fullfilled
            response object.
    
            Params:
                - endpoint_type: EndpointType
                - response_json - a single response portion of the json returned from the Aeris API
                    such as:
                        json_obj["response"]
    
            Returns:
                - a completed/fullfilled response object
            """
            if endpoint_type == EndpointType.AIR_QUALITY:
                return AirQualityResponse(response_json)
            elif endpoint_type == EndpointType.ALERTS:
                return AlertsResponse(response_json)
            elif endpoint_type == EndpointType.FORECASTS:
                return ForecastsResponse(response_json)
            elif endpoint_type == EndpointType.LIGHTNING:
                return LightningResponse(response_json)
            elif endpoint_type == EndpointType.LIGHTNING_SUMMARY:
                return LightningSummaryResponse(response_json)
            elif endpoint_type == EndpointType.OBSERVATIONS:
                return ObservationsResponse(response_json)
            elif endpoint_type == EndpointType.OBSERVATIONS_SUMMARY:
                return ObservationsSummaryResponse(response_json)
            elif endpoint_type == EndpointType.OBSERVATIONS_ARCHIVE:
                return ObservationsArchiveResponse(response_json)
            elif endpoint_type == EndpointType.PLACES:
                return PlacesResponse(response_json)
            else:
                return CustomResponse(response_json)

        elif response_type == ResponseType.GEOJSON:

            """ Returns: a completed/fullfilled geojson response object """

            return AerisWeather.geo_json_response(response_json, endpoint_type)

    @staticmethod
    def geo_json_response(geojson, endpoint_type):

        """
            Determines the appropriate response object based on EndpointType and returns the completed response object.

            Given the endpoint type and the response json from the Aeris API, the method will return an array of
            GeoJsonReponse objects. Each GeoJsonResponse object contains what is found in a geojson feature:
                - a type ("Feature")
                - an id
                - a Geometry object - contains
                    - type: point or polyline
                    - coordinates
                - a properties object (this is an a Response object, specific to the endpoint called)

            Params:
                - endpoint_type: EndpointType
                - geojson - The features array of the geojson response.

                              "features": [
                                {
                                  "type": "Feature",
                                  "id": "KCMY",
                                  ...
                                      43.966666666667
                                    ]
                                  },
                                  "properties": {
                                    "id": "KCMY",
                                    "loc": {
                                      "long": -90.733333333333,
                                      ...
        """
        return GeoJsonResponse(geo_json_data=geojson, endpoint_type=endpoint_type)

    @staticmethod
    def query_str(query_dict):
        """ Takes a RequestQuery object and returns a proper Aeris API url query

            Params:
                - query_dict: A dictionary containing a single RequestQuery and its value

            Returns:
                - str: a correctly formatted query attribute ready to be inserted into an API request url
        """

        out_query = ""

        if query_dict is not None:
            for q, value in query_dict.items():
                out_query += "&" + q + "=" + value
        else:
            out_query = None

        return out_query

    def batch_request(self,
                      endpoints: List[Endpoint],
                      global_location: RequestLocation = None,
                      global_filter_: [RequestFilter] = None,
                      global_sort: RequestSort = None,
                      global_params: Dict[ParameterType, str] = None,
                      global_query: Dict[RequestQuery, str] = None):
        """
        Makes the batch request to the Aeris API and returns the appropriate response array.

        If successful, the batch_request method will return a list of response objects. The list will contain the
            responses in the order they are requested. If a request results in multiple responses, those responses
            will be listed before continuing to the next request's response.

        Params:
            - endpoints: List[Endpoint] - a list of Endpoint objects, one for each request in the batch request
            - global_location: RequestLocation - a RequestLocation object that will be applied to each request, unless
                the request has a local RequestLocation
            - global_filter_: [RequestFilter] - a list of RequestFilters that will be applied to each request, unless
                the request has a local RequestFilter
            - global_sort: RequestSort  - a RequestSort object that will be applied to each request, unless
                the request has a local RequestSort
            - global_params: Dict[ParameterType, str] - a dictionary of parameters that will be applied to each
                request, unless the request has a local parameter dict
            - global_query: Dict[RequestQuery, str] - a dictionary of queries that will be applied to each
                request, unless the request has a local query dict

        Returns:
            - a list of specific response objects, who's type is based on the request data, in the order of the requests
            - an empty list if there is no data
            - an AerisError object if there was an error condition reported by the api response
            - a URLError if there was an issue with sending the request
            - a generic Exception for all other issues
        """

        url = self.batch_url(endpoints=endpoints,
                             global_location=global_location,
                             global_filter_=global_filter_,
                             global_sort=global_sort,
                             global_params=global_params,
                             global_query=global_query)

        network = AerisNetwork()
        json_obj = network.get_json(url, self.app_id)

        responses = []

        # Determine if we have a valid data response, or if there is an API error
        response_error = AerisError.api_error(json_obj)
        if response_error is None:
            endpoint_counter = 0
            for resp in json_obj["response"]["responses"]:

                # Batch response json - check for an error response here, for things like the alerts endpoint's
                # "warn_no_data" response.
                batch_error = AerisError.api_error(json_obj)
                if batch_error is None:
                    # get the appropriate response
                    for r in resp["response"]:
                        # check each response within the batch response for an error code
                        response_error = AerisError.api_error(resp)
                        if response_error is None:
                            endpoint_type = endpoints[endpoint_counter].endpoint_type
                            responses.append(self.response(ResponseType.JSON, endpoint_type, r))
                        else:
                            raise response_error
                else:
                    raise batch_error

                endpoint_counter += 1
        else:
            # we have some kind of error or major warning from the API
            raise response_error

        return responses

    def batch_url(self,
                  endpoints: List[Endpoint],
                  global_location: RequestLocation = None,
                  global_filter_: [RequestFilter] = None,
                  global_sort: RequestSort = None,
                  global_params: Dict[ParameterType, str] = None,
                  global_query: Dict[RequestQuery, str] = None) -> str:
        """ Generate the appropriate batch request url.

             The batch request also supports all of the standard endpoint parameters, such as p, limit, and query,
             except that when used, these batch parameters are considered global and applied to each individual
             request provided with the request's parameters. Note, however, that any parameters included within
             an individual request (within the requests parameter) will override those same global options found
             in the main batch request.

            Parameters can be passed to each individual endpoint as well but must be URL-encoded, use "%3F" for "?"
            and "%26" for "&".

            Example:
                https://api.aerisapi.com/batch?
                p=truckee,nv&client_id=###########&client_secret=########################
                &requests=
                /places/54660,
                /advisories%3Flimit=1%26radius=10mi,
                /observations%3Fp=54601

        Params:
            - endpoints: List[Endpoint] - a list of Endpoint objects, one for each request in the batch request
            - global_location: RequestLocation - a RequestLocation object that will be applied to each request, unless
                the request has a local RequestLocation
            - global_filter_: [RequestFilter] - a list of RequestFilters that will be applied to each request, unless
                the request has a local RequestFilter
            - global_sort: RequestSort  - a RequestSort object that will be applied to each request, unless
                the request has a local RequestSort
            - global_params: Dict[ParameterType, str] - a dictionary of parameters that will be applied to each
                request, unless the request has a local parameter dict
            - global_query: Dict[RequestQuery, str] - a dictionary of queries that will be applied to each
                request, unless the request has a local query dict

        Returns:
            - url string for the batch_request
        """

        url = self.url_host + "batch?client_id=" + self.client_id + "&client_secret=" + self.client_secret

        # add the global request parameters - these apply to all endpoints in the batch request
        if global_location is not None:
            url += "&p=" + global_location.location_str()

        if global_filter_ is not None:
            if len(global_filter_) > 0:
                url += "&filter="
                for filt in global_filter_:
                    url += filt + ","

        if global_params is not None:
            for param, value in global_params.items():
                url += "&" + param + "=" + value

        if global_sort is not None:
            url += "&sort=" + global_sort.value

        out_query = self.query_str(global_query)

        if out_query is not None:
            url += "&query=" + out_query

        # add the requests section
        url += "&requests="

        # add the specifc endpoint requests and their parameters
        for endpoint in endpoints:
            has_param = False
            url += "/" + endpoint.endpoint_type.value

            if endpoint.action is not None:
                url += "/" + endpoint.action.value

            if endpoint.location is not None:
                url += "%3Fp=" + endpoint.location.location_str()
                has_param = True

            if endpoint.filter_ is not None and len(endpoint.filter_) > 0:
                if has_param:
                    url += "%26filter="
                else:
                    url += "%3Ffilter="

                for filt in endpoint.filter_:
                    url += filt + ","

                has_param = True

            if endpoint.params is not None:
                for param, value in endpoint.params.items():
                    if has_param:
                        url += "%26"
                    else:
                        url += "%3F"

                    url += param + "=" + value + ","

                    has_param = True

            if endpoint.sort is not None:
                if has_param:
                    url += "%26sort="
                else:
                    url += "%3Fsort="

                url += endpoint.sort.value

                has_param = True

            out_query = self.query_str(endpoint.query)

            if out_query is not None:
                if has_param:
                    url += "%26query="
                else:
                    url += "%3Fquery="

                url += out_query

                # has_param = True

            # add a trailing comma in case there are more endpoints
            if not url.endswith(","):
                url += ","

        # strip unused trailing commas
        while url.endswith(","):
            url = url[:-1]
        return url
