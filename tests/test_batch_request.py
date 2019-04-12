
from urllib.error import URLError

from aerisweather.aerisweather import AerisWeather
from aerisweather.endpoints.Endpoint import Endpoint, EndpointType
from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.responses.ForecastPeriod import ForecastPeriod
from aerisweather.responses.ForecastsResponse import ForecastsResponse
from aerisweather.responses.ObservationsResponse import ObservationsResponse
from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.ObservationsSummaryResponse import ObservationsSummaryResponse
from aerisweather.responses.ObservationsSummaryTemp import ObservationsSummaryTemp
from aerisweather.utils.AerisError import AerisError
from tests.keys import client_id, client_secret, app_id


class TestBatchRequests:
    """ Defines tests modules for batch requests to the Aeris API """

    def test_api_batch_response(self):
        """ Test against a batch response from the API """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            endpoint = Endpoint(endpoint_type=EndpointType.OBSERVATIONS,
                                location=None,
                                action=None,
                                filter_=None,
                                sort=None,
                                params={ParameterType.OBSERVATIONS.LIMIT: "3"})

            endpoint2 = Endpoint(endpoint_type=EndpointType.FORECASTS,
                                 params={ParameterType.FORECASTS.LIMIT: "3"})

            endpoint3 = Endpoint(endpoint_type=EndpointType.OBSERVATIONS_SUMMARY)

            endpoints = [endpoint, endpoint2, endpoint3]

            response_list = awx.batch_request(endpoints=endpoints,
                                              global_location=RequestLocation(postal_code="54660"))

            for resp in response_list:

                if type(resp) is ObservationsResponse:

                    # Observations
                    obs = resp
                    assert type(obs) is ObservationsResponse
                    assert obs.id is not None

                    loc = obs.loc
                    assert loc is not None
                    assert type(loc) is AerisLocation
                    assert obs.loc.lat > 43

                    place = obs.place
                    assert place is not None
                    # assert place.name == "la crosse"
                    assert place.state == "wi"

                    profile = obs.profile
                    assert profile is not None
                    assert profile.elevFT > 600

                    relative_to = obs.relativeTo
                    assert relative_to.long < -80

                    assert obs.obTimestamp.__class__ is int

                elif type(resp) is ForecastsResponse:

                    # Forecasts
                    forecast = resp
                    assert type(forecast) is ForecastsResponse

                    loc = forecast.loc
                    assert loc is not None
                    assert type(loc) is AerisLocation
                    assert forecast.loc.lat > 43

                    assert forecast.interval is not None

                    period = forecast.periods[0]
                    assert type(period) is ForecastPeriod
                    assert period.weather is not None
                    assert period.validTime is not None

                elif type(resp) is ObservationsSummaryResponse:

                    # ObservationsSummary
                    obs_sum = resp
                    assert type(obs_sum) is ObservationsSummaryResponse
                    assert obs_sum.id is not None

                    loc = obs_sum.loc
                    assert loc is not None
                    assert type(loc) is AerisLocation
                    assert obs_sum.loc.lat > 43

                    place = obs_sum.place
                    assert place is not None
                    # assert place.name == "la crosse"
                    assert place.state == "wi"

                    periods = obs_sum.periods
                    assert periods is not None

                    temp = periods[0].temp
                    assert type(temp) is ObservationsSummaryTemp
                    assert temp.avgF > -10

                    profile = obs_sum.profile
                    assert profile is not None
                    assert profile.elevFT > 600

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex
