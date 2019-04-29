from aerisweather.responses.ObservationsArchiveData import ObservationsArchiveData
from aerisweather.responses.AerisProfile import AerisProfileObservationsArchive
from aerisweather.responses.ObservationsArchivePeriod import ObservationsArchivePeriod
from aerisweather.responses.ObservationsArchiveResponse import ObservationsArchiveResponse
from .common_test_imports import *


class TestObservationsArchive:
    """ Defines tests modules for the Aeris API Observation Archive class """

    def test_static_data(self):
        """ Test the Observation code against a known source of data """

        file = open("./responses/observations_archive.txt", "r")

        try:
            json_obj = json.loads(file.read())

            obs_archive = ObservationsArchiveResponse(json_obj["response"])

            assert obs_archive.id == "KLSE"

            assert type(obs_archive.loc) is AerisLocation
            assert type(obs_archive.loc.long) is float
            assert obs_archive.loc.lat == 43.883333333333
            assert obs_archive.loc.long == -91.25

            assert type(obs_archive.place) is AerisPlace
            place = obs_archive.place
            assert place.name == "la crosse"
            assert place.state == "wi"
            assert place.country == "us"

            assert type(obs_archive.profile) is AerisProfileObservationsArchive
            profile = obs_archive.profile
            assert profile.tz == "America/Chicago"

            period = obs_archive.periods[0]
            assert type(period) is ObservationsArchivePeriod
            ob = period.ob
            assert type(ob) is ObservationsArchiveData
            assert ob.timestamp == 1556517180
            assert ob.dateTimeISO == "2019-04-29T00:53:00-05:00"
            assert ob.tempC == 9.4
            assert ob.tempF == 49
            assert ob.dewpointC == -5.6
            assert ob.dewpointF == 22
            assert ob.humidity == 35
            assert ob.pressureMB == 1018
            assert ob.pressureIN == 30.06
            assert ob.spressureMB == 995
            assert ob.spressureIN == 29.38
            assert ob.altimeterMB == 1019
            assert ob.altimeterIN == 30.09
            assert ob.windKTS == 5
            assert ob.windKPH == 9
            assert ob.windMPH == 6
            assert ob.windSpeedKTS == 5
            assert ob.windSpeedKPH == 9
            assert ob.windSpeedMPH == 6
            assert ob.windDirDEG == 110
            assert ob.windDir == "ESE"
            assert ob.windGustKTS is None
            assert ob.windGustKPH is None
            assert ob.windGustMPH is None
            assert ob.flightRule == "VFR"
            assert ob.visibilityKM == 16.09344
            assert ob.visibilityMI == 10
            assert ob.weather == "Cloudy"
            assert ob.weatherShort == "Cloudy"
            assert ob.weatherCoded == "::OV"
            assert ob.weatherPrimary == "Cloudy"
            assert ob.weatherPrimaryCoded == "::OV"
            assert ob.cloudsCoded == "OV"
            assert ob.icon == "cloudyn.png"
            assert ob.heatindexC == 9
            assert ob.heatindexF == 49
            assert ob.windchillC == 8
            assert ob.windchillF == 46
            assert ob.feelslikeC == 8
            assert ob.feelslikeF == 46
            assert ob.isDay is False
            assert ob.sunrise == 1556535510
            assert ob.sunriseISO == "2019-04-29T05:58:30-05:00"
            assert ob.sunset == 1556586361
            assert ob.sunsetISO == "2019-04-29T20:06:01-05:00"
            assert ob.snowDepthCM is None
            assert ob.snowDepthIN is None
            assert ob.precipMM == 0
            assert ob.precipIN == 0
            assert ob.solradWM2 == 0
            assert ob.solradMethod == "estimated"
            assert ob.ceilingFT == 10000
            assert ob.ceilingM == 3048
            assert ob.light == 0
            assert ob.QC == "O"
            assert ob.QCcode == 10
            assert ob.tempMax6hrC == 11.1
            assert ob.tempMax6hrF == 52
            assert ob.tempMin6hrC == 9.4
            assert ob.tempMin6hrF == 49
            assert ob.sky == 100

            assert period.raw == "KLSE 290553Z AUTO 11005KT 10SM OVC100 09/M06 A3008 RMK AO2 SLP186 T00941056 10111 20094 401331006 55002"

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

            endpoint = Endpoint(endpoint_type=EndpointType.OBSERVATIONS_ARCHIVE,
                                location=None,
                                action=RequestAction.OBSERVATIONS_ARCHIVE.CLOSEST,
                                filter_=None,
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
                                        filter_=None,
                                        sort=None,
                                        params={ParameterType.OBSERVATIONS.P: "54601"},
                                        query={RequestQuery.OBSERVATIONS.ID: "KLSE"})

            for obs in obs_list:  # type: ObservationsArchiveResponse
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

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex
