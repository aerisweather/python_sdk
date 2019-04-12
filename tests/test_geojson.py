from aerisweather.responses.ForecastPeriod import ForecastPeriod
from aerisweather.responses.ForecastsResponse import ForecastsResponse
from aerisweather.responses.Geometry import Geometry
from aerisweather.responses.ObservationsResponse import ObservationsResponse
from .common_test_imports import *
from aerisweather.responses.GeoJsonResponse import GeoJsonResponse


class TestGeoJson:
    """ Defines tests modules for the geojson data """

    def test_static_geojson(self):
        """ Test against a known source of data """

        file = open("./responses/observations.txt", "r")

        # try:
        #     json_obj = json.loads(file.read())
        #
        #     obs = ObservationsResponse(json_obj["response"])
        #
        #     assert obs.id == "KLSE"
        #
        #     assert type(obs.loc) is AerisLocation
        #     assert type(obs.loc.long) is float
        #     assert obs.loc.lat == 43.883333333333
        #     assert obs.loc.long == -91.25
        #
        #     assert type(obs.place) is AerisPlace
        #     place = obs.place
        #     assert place.name == "la crosse"
        #     assert place.state == "wi"
        #     assert place.country == "us"
        #
        #     assert type(obs.profile) is AerisProfileObservations
        #     profile = obs.profile
        #     assert profile.tz == "America/Chicago"
        #     assert profile.elevM == 199
        #     assert profile.elevFT == 653
        #
        #     assert obs.obTimestamp == 1520869980
        #     assert obs.obDateTime == "2018-03-12T10:53:00-05:00"
        #
        #     assert type(obs.ob) is ObservationsData
        #     ob = obs.ob
        #     assert ob.timestamp == 1520869980
        #     assert ob.dateTimeISO == "2018-03-12T10:53:00-05:00"
        #     assert ob.tempC == 1.1
        #     assert ob.tempF == 34
        #     assert ob.dewpointC == -5
        #     assert ob.dewpointF == 23
        #     assert ob.humidity == 64
        #     assert ob.pressureMB == 1024
        #     assert ob.pressureIN == 30.24
        #     assert ob.spressureMB == 999
        #     assert ob.spressureIN == 29.5
        #     assert ob.altimeterMB == 1023
        #     assert ob.altimeterIN == 30.21
        #     assert ob.windKTS == 10
        #     assert ob.windKPH == 19
        #     assert ob.windMPH == 12
        #     assert ob.windSpeedKTS == 10
        #     assert ob.windSpeedKPH == 19
        #     assert ob.windSpeedMPH == 12
        #     assert ob.windDirDEG == 320
        #     assert ob.windDir == "NW"
        #     assert ob.windGustKTS is None
        #     assert ob.windGustKPH is None
        #     assert ob.windGustMPH is None
        #     assert ob.flightRule == "LIFR"
        #     assert ob.visibilityKM == 16.09344
        #     assert ob.visibilityMI == 10
        #     assert ob.weather == "Sunny"
        #     assert ob.weatherShort == "Sunny"
        #     assert ob.weatherCoded == "::CL"
        #     assert ob.weatherPrimary == "Sunny"
        #     assert ob.weatherPrimaryCoded == "::CL"
        #     assert ob.cloudsCoded == "CL"
        #     assert ob.icon == "sunny.png"
        #     assert ob.heatindexC == 1
        #     assert ob.heatindexF == 34
        #     assert ob.windchillC == -4
        #     assert ob.windchillF == 25
        #     assert ob.feelslikeC == -4
        #     assert ob.feelslikeF == 25
        #     assert ob.isDay is True
        #     assert ob.sunrise == 1520857243
        #     assert ob.sunriseISO == "2018-03-12T07:20:43-05:00"
        #     assert ob.sunset == 1520899695
        #     assert ob.sunsetISO == "2018-03-12T19:08:15-05:00"
        #     assert ob.snowDepthCM is None
        #     assert ob.snowDepthIN is None
        #     assert ob.precipMM == 0
        #     assert ob.precipIN == 0
        #     assert ob.solradWM2 == 510
        #     assert ob.solradMethod == "estimated"
        #     assert ob.ceilingFT is None
        #     assert ob.ceilingM is None
        #     assert ob.light == 80
        #     assert ob.QC == "O"
        #     assert ob.QCcode == 10
        #     assert ob.sky == 0
        #
        #     assert obs.raw == "KLSE 121553Z 32010KT 10SM CLR 01/M05 A3022 RMK AO2 SLP242 T00111050"
        #
        #     assert type(obs.relativeTo) is AerisRelativeTo
        #     rel = obs.relativeTo
        #     assert rel.lat == 43.80136
        #     assert rel.long == -91.23958
        #     assert rel.bearing == 355
        #     assert rel.bearingENG == "N"
        #     assert rel.distanceKM == 9.153
        #     assert rel.distanceMI == 5.687
        #
        # except URLError as url_err:
        #     print("URL Error: " + url_err.reason)
        #     raise url_err
        #
        # except AerisError as aeris_err:
        #     print("AerisError: " + aeris_err.__str__())
        #     raise aeris_err
        #
        # except Exception as ex:
        #     print(ex.args)
        #     raise ex
        #
        # finally:
        #     file.close()

    def test_api_response_obs(self):
        """ Test against a live response from the API """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            endpoint = Endpoint(endpoint_type=EndpointType.OBSERVATIONS,
                                location=None,
                                action=RequestAction.OBSERVATIONS.CLOSEST,
                                filter_=None,
                                sort=None,
                                params={ParameterType.OBSERVATIONS.P: "54660",
                                        ParameterType.OBSERVATIONS.LIMIT: "2",
                                        ParameterType.OBSERVATIONS.RADIUS: "100miles"},
                                query=None,
                                format_=RequestFormat.GEOJSON)

            obs_geo_list = awx.request(endpoint=endpoint)

            assert len(obs_geo_list) > 0

            for obsgeo in obs_geo_list:  # type: GeoJsonResponse
                assert obsgeo.type == "Feature"

                assert type(obsgeo.geometry) is Geometry

                if obsgeo.id == "KCMY":
                    assert obsgeo.geometry.type == "Point"
                    assert obsgeo.geometry.coordinates[0] == -90.733333333333
                    assert obsgeo.geometry.coordinates[1] == 43.966666666667

                    properties = obsgeo.properties
                    assert type(properties) is ObservationsResponse
                    assert properties.place.state == "wi"

                    relative_to = properties.relativeTo
                    assert type(relative_to) is AerisRelativeTo
                    assert relative_to.bearing == 266

                elif obsgeo.id == "KVOK":
                    assert obsgeo.geometry.type == "Point"
                    assert obsgeo.geometry.coordinates[0] == -90.266666666667
                    assert obsgeo.geometry.coordinates[1] == 43.916666666667

                    properties = obsgeo.properties
                    assert type(properties) is ObservationsResponse
                    assert properties.place.state == "wi"

                    relative_to = properties.relativeTo
                    assert type(relative_to) is AerisRelativeTo
                    assert relative_to.bearing == 110

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex

    def test_api_response_forecast(self):
        """ Test against a live response from the API """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            endpoint = Endpoint(endpoint_type=EndpointType.FORECASTS,
                                location=None,
                                action=RequestAction.FORECASTS.CLOSEST,
                                filter_=None,
                                sort=None,
                                params={ParameterType.FORECASTS.P: "54660",
                                        ParameterType.FORECASTS.LIMIT: "2"},
                                query=None,
                                format_=RequestFormat.GEOJSON)

            fcast_geo_list = awx.request(endpoint=endpoint)

            assert len(fcast_geo_list) > 0

            for fcastgeo in fcast_geo_list:  # type: GeoJsonResponse
                assert fcastgeo.type == "Feature"
                assert fcastgeo.endpoint_type == EndpointType.FORECASTS
                assert type(fcastgeo.geometry) is Geometry

                assert fcastgeo.geometry.type == "Point"
                assert fcastgeo.geometry.coordinates[0] == -90.504
                assert fcastgeo.geometry.coordinates[1] == 43.979

                properties = fcastgeo.properties
                assert type(properties) is ForecastsResponse
                assert properties.interval == "day"

                assert len(properties.periods) > 0
                periods = properties.periods
                assert type(periods[0]) == ForecastPeriod
                assert periods[0].avgTempF is not None

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex

    # def test_api_response_aqi(self):
    #     """ Test against a live response from the API """
    #
    #     try:
    #         awx = AerisWeather(app_id=app_id,
    #                            client_id=client_id,
    #                            client_secret=client_secret)
    #
    #         endpoint = Endpoint(endpoint_type=EndpointType.AIR_QUALITY,
    #                             location=None,
    #                             action=RequestAction.AIR_QUALITY.CLOSEST,
    #                             filter_=None,
    #                             sort=None,
    #                             params={ParameterType.AIR_QUALITY.P: "54660",
    #                                     ParameterType.AIR_QUALITY.LIMIT: "2",
    #                                     ParameterType.AIR_QUALITY.RADIUS: "100miles"},
    #                             query=None,
    #                             format_=RequestFormat.GEOJSON)
    #
    #         aqi_geo_list = awx.request(endpoint=endpoint)
    #
    #         assert len(aqi_geo_list) > 0
    #
    #         for aqigeo in aqi_geo_list:  # type: GeoJsonResponse
    #             assert aqigeo.type == "Feature"
    #             assert aqigeo.endpoint_type == EndpointType.AIR_QUALITY
    #             assert type(aqigeo.geometry) is Geometry
    #
    #     except URLError as url_err:
    #         print("URL Error: " + url_err.reason)
    #         raise url_err
    #
    #     except AerisError as aeris_err:
    #         print("AerisError: " + str(aeris_err))
    #         raise aeris_err
    #
    #     except Exception as ex:
    #         print(ex.args)
    #         raise ex