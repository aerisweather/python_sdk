import logging
from urllib.error import URLError

from aerisweather.requests.ParameterType import ParameterType

from aerisweather.requests.RequestAction import RequestAction

from aerisweather.aerisweather import AerisWeather
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.responses.ForecastPeriod import ForecastPeriod
from aerisweather.responses.ForecastsResponse import ForecastsResponse
from aerisweather.utils.AerisError import AerisError
from tests.keys import client_id, client_secret, app_id


class TestCustomRequests:
    """ Defines tests modules for custom or unknown endpoints, actions, parameters, etc. """

    def test_custom_action(self):
        """ Test using a non-defined (but valid) action with an endpoint. """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            action = RequestAction()
            action.custom = "closest"
            f_list = awx.forecasts(location=RequestLocation(postal_code="54660"),
                                   action=action,
                                   params={ParameterType.FORECASTS.P: "54660"})

            for forecast in f_list:
                assert type(forecast) is ForecastsResponse
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
