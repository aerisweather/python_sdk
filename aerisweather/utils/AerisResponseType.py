
from aenum import Enum


class RESPONSE_TYPE(Enum):
    """ Defines the expected return response formats from the API """
    JSON = "json"
    GEOJSON = "geojson"
    ERROR = "error"


class AerisResponseType(object):
    """ Defines the functions for determining what type of response was received from the API """

    @staticmethod
    def get_response_type(json)->str:

        if "features" in json:
            """ this is a geojson response """
            return RESPONSE_TYPE.GEOJSON

        if "success" in json:
            """ this is a normal json response """
            if json["error"] is not None:
                return RESPONSE_TYPE.ERROR
            else:
                return RESPONSE_TYPE.JSON

