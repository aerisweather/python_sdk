
from typing import Dict

from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestAction import RequestAction
from aerisweather.requests.RequestFilter import RequestFilter
from aerisweather.requests.RequestFormat import RequestFormat
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.requests.RequestQuery import RequestQuery
from aerisweather.requests.RequestSort import RequestSort
from aerisweather.endpoints.EndpointType import EndpointType
from aerisweather.endpoints.Endpoint import Endpoint

common_imports = [
    Dict,
    Endpoint,
    EndpointType,
    ParameterType,
    RequestAction,
    RequestFilter,
    RequestFormat,
    RequestLocation,
    RequestQuery,
    RequestSort
]
