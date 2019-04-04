
import json
from urllib.error import URLError

from aerisweather.aerisweather import AerisWeather
from aerisweather.requests.Endpoint import EndpointType, Endpoint
from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestFilter import RequestFilter
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.responses.ForecastPeriod import ForecastPeriod
from aerisweather.responses.ForecastsResponse import ForecastsResponse
from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.AerisProfile import AerisProfileForecasts
from aerisweather.utils.AerisError import AerisError
from tests.keys import client_id, client_secret, app_id


class TestForecasts:
    """ Defines tests modules for the Aeris API Forecasts class """

    def test_static_data(self):
        """ Test the Forecasts code against a known source of data """

        file = open("./responses/forecasts.txt", "r")

        try:
            json_obj = json.loads(file.read())

            forecast = ForecastsResponse(json_obj["response"][0])

            assert type(forecast.loc) is AerisLocation
            assert type(forecast.loc.long) is float
            assert forecast.loc.lat == 33.953
            assert forecast.loc.long == -84.55

            assert type(forecast.profile) is AerisProfileForecasts
            profile = forecast.profile
            assert profile.tz == "America/New_York"

            periods = forecast.periods
            assert len(periods) == 2
            assert type(periods[0]) == ForecastPeriod
            p0 = periods[0]
            assert p0.timestamp == 1521543600
            assert p0.validTime == "2018-03-20T07:00:00-04:00"
            assert p0.dateTimeISO == "2018-03-20T07:00:00-04:00"
            assert p0.maxTempC == 17
            assert p0.maxTempF == 63
            assert p0.minTempC == 1
            assert p0.minTempF == 34
            assert p0.avgTempC == 9
            assert p0.avgTempF == 48
            assert p0.tempC is None
            assert p0.tempF is None
            assert p0.pop == 44
            assert p0.precipMM == 1.1
            assert p0.iceaccum == 0
            assert p0.iceaccumMM == 0
            assert p0.iceaccumIN == 0
            assert p0.maxHumidity == 100
            assert p0.minHumidity == 75
            assert p0.humidity == 74
            assert p0.uvi == 5
            assert p0.pressureMB == 1001
            assert p0.pressureIN == 29.56
            assert p0.sky == 78
            assert p0.snowCM == 0
            assert p0.snowIN == 0
            assert p0.feelslikeC == 12
            assert p0.feelslikeF == 54
            assert p0.minFeelslikeC == 12
            assert p0.minFeelslikeF == 54
            assert p0.maxFeelslikeC == 17
            assert p0.maxFeelslikeF == 63
            assert p0.avgFeelslikeC == 15
            assert p0.avgFeelslikeF == 59
            assert p0.dewpointC == 12
            assert p0.dewpointF == 54
            assert p0.maxDewpointC == 12
            assert p0.maxDewpointF == 54
            assert p0.minDewpointC == 7
            assert p0.minDewpointF == 44
            assert p0.avgDewpointC == 10
            assert p0.avgDewpointF == 51
            assert p0.windDirDEG == 250
            assert p0.windDir == "WSW"
            assert p0.windDirMaxDEG == 280
            assert p0.windDirMax == "W"
            assert p0.windDirMinDEG == 240
            assert p0.windDirMin == "WSW"
            assert p0.windGustKTS == 18
            assert p0.windGustKPH == 33
            assert p0.windGustMPH == 21
            assert p0.windSpeedKTS == 9
            assert p0.windSpeedKPH == 16
            assert p0.windSpeedMPH == 10
            assert p0.windSpeedMaxKTS == 11
            assert p0.windSpeedMaxKPH == 21
            assert p0.windSpeedMaxMPH == 13
            assert p0.windSpeedMinKTS == 5
            assert p0.windSpeedMinKPH == 9
            assert p0.windSpeedMinMPH == 6
            assert p0.windDir80mDEG == 253
            assert p0.windDir80m == "WSW"
            assert p0.windDirMax80mDEG == 280
            assert p0.windDirMax80m == "W"
            assert p0.windDirMin80mDEG == 240
            assert p0.windDirMin80m == "WSW"
            assert p0.windGust80mKTS == 21
            assert p0.windGust80mKPH == 38
            assert p0.windGust80mMPH == 24
            assert p0.windSpeed80mKTS == 15
            assert p0.windSpeed80mKPH == 27
            assert p0.windSpeed80mMPH == 17
            assert p0.windSpeedMax80mKTS == 21
            assert p0.windSpeedMax80mKPH == 38
            assert p0.windSpeedMax80mMPH == 24
            assert p0.windSpeedMin80mKTS == 6
            assert p0.windSpeedMin80mKPH == 11
            assert p0.windSpeedMin80mMPH == 7
            assert p0.weather == "Mostly Cloudy with Scattered Showers"

            assert len(p0.weatherCoded) == 2
            assert p0.weatherCoded[0].timestamp == 1521572400
            assert p0.weatherCoded[0].wx == "S:L:RW"
            assert p0.weatherCoded[0].dateTimeISO == "2018-03-20T15:00:00-04:00"

            assert p0.weatherCoded[1].timestamp == 1521576000
            assert p0.weatherCoded[1].wx == "C:L:RW"
            assert p0.weatherCoded[1].dateTimeISO == "2018-03-20T16:00:00-04:00"

            assert p0.weatherPrimary == "Scattered Showers"
            assert p0.weatherPrimaryCoded == "C:L:RW"
            assert p0.cloudsCoded == "BK"
            assert p0.icon == "mcloudyr.png"
            assert p0.isDay is True
            assert p0.sunrise == 1521546045
            assert p0.sunriseISO == "2018-03-20T07:40:45-04:00"
            assert p0.sunset == 1521589810
            assert p0.sunsetISO == "2018-03-20T19:50:10-04:00"

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + aeris_err.__str__())
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex

        finally:
            file.close()

    def test_api_response(self):
        """ Test the code against a live response from the API """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            forecast_list = awx.forecasts(location=RequestLocation(postal_code="54601"),
                                          action=None,
                                          filter_=[RequestFilter.FORECASTS.DAY_NIGHT],
                                          sort=None,
                                          params={ParameterType.FORECASTS.LIMIT: "1"},
                                          query=None)

            for forecast in forecast_list:  # type: ForecastsResponse
                assert forecast is not None
                assert forecast.loc.long < 0
                assert forecast.interval is not None
                period = forecast.periods[0]
                assert type(period) is ForecastPeriod
                assert period.weather is not None
                assert period.validTime is not None

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex

    def test_forecasts_method(self):
        """ Test the AerisWeather.forecasts method """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            endpoint = Endpoint(endpoint_type=EndpointType.FORECASTS,
                                location=RequestLocation(postal_code="54601"),
                                action=None,
                                filter_=[RequestFilter.FORECASTS.DAY_NIGHT],
                                sort=None,
                                params={ParameterType.FORECASTS.LIMIT: "1"},
                                query=None)

            forecast_list = awx.request(endpoint=endpoint)

            for forecast in forecast_list:  # type: ForecastsResponse
                assert forecast is not None
                assert forecast.loc.long < 0
                assert forecast.interval is not None
                period = forecast.periods[0]
                assert type(period) is ForecastPeriod
                assert period.weather is not None
                assert period.validTime is not None

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex
