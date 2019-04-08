
from .common_test_imports import *
from aerisweather.responses.ObservationsData import ObservationsData
from aerisweather.responses.ObservationsResponse import ObservationsResponse


class TestObservations:
    """ Defines tests modules for the Aeris API Observation class """

    def test_static_data(self):
        """ Test the Observation code against a known source of data """

        file = open("./responses/observations.txt", "r")

        try:
            json_obj = json.loads(file.read())

            obs = ObservationsResponse(json_obj["response"])

            assert obs.id == "KLSE"

            assert type(obs.loc) is AerisLocation
            assert type(obs.loc.long) is float
            assert obs.loc.lat == 43.883333333333
            assert obs.loc.long == -91.25

            assert type(obs.place) is AerisPlace
            place = obs.place
            assert place.name == "la crosse"
            assert place.state == "wi"
            assert place.country == "us"

            assert type(obs.profile) is AerisProfileObservations
            profile = obs.profile
            assert profile.tz == "America/Chicago"
            assert profile.elevM == 199
            assert profile.elevFT == 653

            assert obs.obTimestamp == 1520869980
            assert obs.obDateTime == "2018-03-12T10:53:00-05:00"

            assert type(obs.ob) is ObservationsData
            ob = obs.ob
            assert ob.timestamp == 1520869980
            assert ob.dateTimeISO == "2018-03-12T10:53:00-05:00"
            assert ob.tempC == 1.1
            assert ob.tempF == 34
            assert ob.dewpointC == -5
            assert ob.dewpointF == 23
            assert ob.humidity == 64
            assert ob.pressureMB == 1024
            assert ob.pressureIN == 30.24
            assert ob.spressureMB == 999
            assert ob.spressureIN == 29.5
            assert ob.altimeterMB == 1023
            assert ob.altimeterIN == 30.21
            assert ob.windKTS == 10
            assert ob.windKPH == 19
            assert ob.windMPH == 12
            assert ob.windSpeedKTS == 10
            assert ob.windSpeedKPH == 19
            assert ob.windSpeedMPH == 12
            assert ob.windDirDEG == 320
            assert ob.windDir == "NW"
            assert ob.windGustKTS is None
            assert ob.windGustKPH is None
            assert ob.windGustMPH is None
            assert ob.flightRule == "LIFR"
            assert ob.visibilityKM == 16.09344
            assert ob.visibilityMI == 10
            assert ob.weather == "Sunny"
            assert ob.weatherShort == "Sunny"
            assert ob.weatherCoded == "::CL"
            assert ob.weatherPrimary == "Sunny"
            assert ob.weatherPrimaryCoded == "::CL"
            assert ob.cloudsCoded == "CL"
            assert ob.icon == "sunny.png"
            assert ob.heatindexC == 1
            assert ob.heatindexF == 34
            assert ob.windchillC == -4
            assert ob.windchillF == 25
            assert ob.feelslikeC == -4
            assert ob.feelslikeF == 25
            assert ob.isDay is True
            assert ob.sunrise == 1520857243
            assert ob.sunriseISO == "2018-03-12T07:20:43-05:00"
            assert ob.sunset == 1520899695
            assert ob.sunsetISO == "2018-03-12T19:08:15-05:00"
            assert ob.snowDepthCM is None
            assert ob.snowDepthIN is None
            assert ob.precipMM == 0
            assert ob.precipIN == 0
            assert ob.solradWM2 == 510
            assert ob.solradMethod == "estimated"
            assert ob.ceilingFT is None
            assert ob.ceilingM is None
            assert ob.light == 80
            assert ob.QC == "O"
            assert ob.QCcode == 10
            assert ob.sky == 0

            assert obs.raw == "KLSE 121553Z 32010KT 10SM CLR 01/M05 A3022 RMK AO2 SLP242 T00111050"

            assert type(obs.relativeTo) is AerisRelativeTo
            rel = obs.relativeTo
            assert rel.lat == 43.80136
            assert rel.long == -91.23958
            assert rel.bearing == 355
            assert rel.bearingENG == "N"
            assert rel.distanceKM == 9.153
            assert rel.distanceMI == 5.687

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
        """ Test the Observation code against a live response from the API """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            endpoint = Endpoint(endpoint_type=EndpointType.OBSERVATIONS,
                                location=None,
                                action=RequestAction.OBSERVATIONS.CLOSEST,
                                filter_=[RequestFilter.OBSERVATIONS.MESONET],
                                sort=None,
                                params={ParameterType.OBSERVATIONS.P: "54601"},
                                query={RequestQuery.OBSERVATIONS.ID: "KLSE"})

            obs_list = awx.request(endpoint=endpoint)

            assert len(obs_list) > 0

            for obs in obs_list:
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
                assert relative_to.long < -91

                assert obs.obTimestamp.__class__ is int

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex

    def test_observations_method(self):
        """ Test the AerisWeather.observations method """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            obs_list = awx.observations(location=None,
                                        action=RequestAction.OBSERVATIONS.CLOSEST,
                                        filter_=[RequestFilter.OBSERVATIONS.MESONET],
                                        sort=None,
                                        params={ParameterType.OBSERVATIONS.P: "54601"},
                                        query={RequestQuery.OBSERVATIONS.ID: "KLSE"})

            for obs in obs_list:  # type: ObservationsResponse
                assert obs.id is not None

                loc = obs.loc
                assert loc is not None
                assert type(loc) is AerisLocation
                assert obs.loc.lat > 43

                place = obs.place
                assert place is not None
                assert place.state == "wi"

                profile = obs.profile
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
