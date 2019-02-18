import sys
import json
import logging
from urllib import request
from urllib.error import URLError

from aerisweather.version import __version__


class AerisNetwork:
    """ Defines networking methods used with the AerisWeather API """

    @staticmethod
    def get_json(url: str, app_id: str):
        """ Returns a json object containing an AerisWeather API response """

        try:
            req = request.Request(url)
            try:
                req.add_header('Referer', app_id)
                req.add_header('User-Agent',
                               "AerisPythonSDK/" + __version__ + "/Python/" + sys.version.replace('\n', ''))

            except URLError:
                # we don't need the extra headers, so let it pass if it fails here
                pass

            resp = request.urlopen(req)

            return json.loads(resp.read())
        except URLError as err:
            logging.basicConfig(level=logging.ERROR)
            logger = logging.getLogger('AerisNetwork:get_json ')
            logger.error(err)

            raise err
