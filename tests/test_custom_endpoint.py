import logging
import unittest
from urllib.error import URLError

from aerisweather.aerisweather import AerisWeather
from aerisweather.requests.Endpoint import Endpoint, EndpointType
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.responses.AerisProfile import AerisProfileRiversGauges
from aerisweather.responses.CustomResponse import CustomResponse
from aerisweather.responses.ForecastPeriod import ForecastPeriod
from aerisweather.responses.ForecastsResponse import ForecastsResponse
from aerisweather.responses.RiversCrests import RiversCrests
from aerisweather.responses.RiversCrestsRecent import RiversCrestsRecent
from aerisweather.utils.AerisError import AerisError
from tests.keys import client_id, client_secret, app_id


class TestCustomEndpoint(unittest.TestCase):
    """ Defines tests modules for custom or unknown endpoints and their attributes """

    def test_api_response(self):
        """ Test against a live response from the API """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            # Valid endpoint, not in our Endpoint Enum - run this to test a beta or pre-release endpoint
            EndpointType.custom = "stormreports"
            endpt = Endpoint(EndpointType.CUSTOM, location=RequestLocation(postal_code="54660"))
            try:
                resp_list = awx.request(endpt)

                if len(resp_list) > 0:
                    response = resp_list[0]
                    assert type(response) is CustomResponse
                else:
                    print(EndpointType.custom + ": no data")
            except AerisError as ae_ex:
                logging.basicConfig(level=logging.ERROR)
                logger = logging.getLogger(' stormreports endpoint test ')
                logger.error(str(ae_ex))
            except Exception as ex:
                logging.basicConfig(level=logging.ERROR)
                logger = logging.getLogger(' stormreports endpoint test ')
                logger.error(str(ex))

            # You can also use the custom endpoint type to request data from a known valid endpoint, for cases
            # where new API data fields have not yet been added to an endpoint's response class.
            EndpointType.custom = "forecasts"
            f_list = awx.request(endpoint=Endpoint(endpoint_type=EndpointType.CUSTOM,
                                                   location=RequestLocation(postal_code="54660")))

            forecast = f_list[0]
            assert type(forecast) is CustomResponse
            assert len(forecast.periods) > 0
            period = forecast.periods[0]  # type: ForecastPeriod
            assert period.weather is not None

            # Another example, with lots of nested lists, etc.
            # rivers/gauges
            EndpointType.custom = "rivers/gauges"
            rg_list = awx.request(endpoint=Endpoint(endpoint_type=EndpointType.CUSTOM,
                                                    location=RequestLocation(postal_code="57101")))

            if len(rg_list) > 0:
                rg = rg_list[0]
                assert type(rg) is CustomResponse
                profile = rg.profile  # type: AerisProfileRiversGauges
                crests = profile.crests  # type: RiversCrests
                recent = crests.recent  # type: [RiversCrestsRecent]
                assert len(recent) > 0
                assert recent[0].heightFT is not None
            else:
                print(str(EndpointType.custom) + ": no data")

            # Unknown and invalid endpoint
            EndpointType.custom = "bogus/endpoint"
            print(str(EndpointType.custom) + ": expecting invalid request")

            invalid_list = awx.request(endpoint=Endpoint(endpoint_type=EndpointType.CUSTOM,
                                                         location=RequestLocation(postal_code="57101")))
            # the results of this call will be a thrown AerisError exception.

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            assert aeris_err.code == "invalid_request"
            print("AerisError: " + "Level: " + aeris_err.level.value + " - " + str(aeris_err))
            # raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex

    def test_custom_endpoint_method(self):
        """ Test the AerisWeather.custom_endpoint method """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            EndpointType.custom = "forecasts"
            f_list = awx.custom_endpoint(location=RequestLocation(postal_code="54660"))

            for forecast in f_list:
                assert type(forecast) is CustomResponse
                assert len(forecast.periods) > 0
                period = forecast.periods[0]  # type: ForecastPeriod
                assert period.weather is not None

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex


suite = unittest.TestLoader().loadTestsFromTestCase(TestCustomEndpoint)
unittest.TextTestRunner(verbosity=2).run(suite)
