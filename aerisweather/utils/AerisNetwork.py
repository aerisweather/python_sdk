import sys
import json
import logging
import requests
from urllib.error import URLError

from aerisweather.version import __version__


class AerisNetwork:
    """ Defines networking methods used with the AerisWeather API """

    @staticmethod
    def get_json(url: str, app_id: str):
        """ Returns a json object containing an AerisWeather API response """

        if url.find("http:"):
            url.replace("http:", "https:")
        else:
            if not url.find("https:"):
                url = "https://" + url

        try:
            header = ""
            try:
                header = {'Referer': app_id,
                          'User-Agent': 'AerisPythonSDK/' + __version__ + '/Python/' +
                                          sys.version.replace('\n', '')}

            except URLError:
                # we don't need the extra headers, so let it pass if it fails here
                pass

            resp = requests.get(url, headers=header)

            return json.loads(resp.text)
        except URLError as err:
            logging.basicConfig(level=logging.ERROR)
            logger = logging.getLogger('AerisNetwork:get_json ')
            logger.error(err)

            raise err
