from datetime import datetime
from urllib.error import URLError
from typing import Dict
from pytest import approx
import pytest
import json

from aerisweather.utils.AerisDateTime import AerisDateTime
from aerisweather.aerisweather import AerisWeather
from aerisweather.endpoints.Endpoint import Endpoint
from aerisweather.endpoints.EndpointType import EndpointType
from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestAction import RequestAction
from aerisweather.requests.RequestFormat import RequestFormat
from aerisweather.requests.RequestFilter import RequestFilter
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.requests.RequestQuery import RequestQuery
from aerisweather.requests.RequestSort import RequestSort
from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.AerisPlace import AerisPlace
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
    AerisRelativeTo,
    AerisError,
    client_id,
    client_secret,
    app_id
]
