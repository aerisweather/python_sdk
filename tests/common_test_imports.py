
import json

from typing import Dict
from urllib.error import URLError
from aerisweather.aerisweather import AerisWeather
from aerisweather.requests import RequestFormat
from aerisweather.requests.Endpoint import Endpoint, EndpointType
from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestAction import RequestAction
from aerisweather.requests.RequestFilter import RequestFilter
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.requests.RequestQuery import RequestQuery
from aerisweather.requests.RequestSort import RequestSort
from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.AerisPlace import AerisPlace
from aerisweather.responses.AerisProfile import AerisProfileObservations
from aerisweather.responses.AerisRelativeTo import AerisRelativeTo
from aerisweather.utils.AerisError import AerisError
from tests.keys import client_id, client_secret, app_id

common_imports = [
    Dict,
    URLError,
    AerisWeather,
    Endpoint,
    EndpointType,
    ParameterType,
    RequestAction,
    RequestFilter,
    RequestFormat,
    RequestLocation,
    RequestQuery,
    RequestSort,
    AerisLocation,
    AerisPlace,
    AerisProfileObservations,
    AerisRelativeTo,
    AerisError,
    client_id,
    client_secret,
    app_id
]
