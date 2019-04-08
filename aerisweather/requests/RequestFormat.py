""" The @skip annotation allows us to create a nested enum structure, without including the child enums in the
 top level enum list. """

from aenum import Enum


class RequestFormat(Enum):
    """ Defines the available formats for each Aeris API endpoint's requests.

        For details on the use of each format value, see the Formats secton of the corresponding endpoint, such
            as the Air Quality endpoint's formats found here:
            https://www.aerisweather.com/support/docs/api/reference/endpoints/airquality/#params

        As of 4/8/2019 - All endpoints can use one of two formats, json (default) or geojson. Geojson is returned
        in the standard geojson format. http://geojson.org/
    """
    JSON = "json"
    GEOJSON = "geojson"
