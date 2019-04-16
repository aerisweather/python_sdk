from aerisweather.responses.AlertDetails import AlertDetails
from aerisweather.responses.AlertIncludes import AlertIncludes
from aerisweather.responses.AlertsResponse import AlertsResponse
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

        file = open("./responses/geojson_alerts.txt", "r")

        try:
            geojson_obj = json.loads(file.read())

            geojson = GeoJsonResponse(geojson_obj["features"][0], EndpointType.ALERTS)

            assert geojson.type == "Feature"
            assert geojson.id is None

            geometry = geojson.geometry
            assert type(geometry) is Geometry
            assert geometry.type == "Polygon"
            assert len(geometry.coordinates[0]) == 6
            assert geometry.coordinates[0][0][0] == -91.42
            assert geometry.coordinates[0][0][1] == 44.01

            properties = geojson.properties
            assert type(properties) is AlertsResponse
            assert properties.id == "02660c46332b42ee47d2d3beb1ee043c"
            location = properties.loc
            assert location.long == -91.1152379047
            assert location.lat == 43.9065279033

            details = properties.details
            assert type(details) is AlertDetails
            assert details.type == "FL.W"
            assert details.name == "FLOOD WARNING"
            assert details.loc == "WIC063"
            assert details.emergency is False
            assert details.color == "00FF00"
            assert details.cat == "flood"

            timestamps = properties.timestamps
            assert timestamps.issued == 1554825960
            assert timestamps.issuedISO == "2019-04-09T11:06:00-05:00"
            assert timestamps.begins == 1554825960
            assert timestamps.beginsISO == "2019-04-09T11:06:00-05:00"
            assert timestamps.expires == 1554879960
            assert timestamps.expiresISO == "2019-04-10T02:06:00-05:00"
            assert timestamps.added == 1554825995
            assert timestamps.addedISO == "2019-04-09T11:06:35-05:00"

            assert properties.poly == "-91.42,44.01,-91.2,43.88,-91.22,43.57,-91.27,43.61,-91.45,43.99"
            assert properties.geoPoly["type"] == "Polygon"
            assert len(properties.geoPoly["coordinates"][0]) == 6

            includes = properties.includes
            assert type(includes) is AlertIncludes
            assert includes.counties[0] == "MNC055"
            assert includes.counties[1] == "WIC063"
            assert includes.fips[2] == "55123"
            assert includes.wxzones[1] == "WIZ041"
            assert includes.zipcodes[5] == "55919"

            place = properties.place
            assert type(place) is AerisPlace
            assert place.name == "la crosse"
            assert place.state == "wi"

            assert properties.profile.tz == "America/Chicago"

            assert properties.active is True

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
