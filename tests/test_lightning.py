from aerisweather.responses.LightningObservationPulse import LightningObservationPulse
from aerisweather.responses.LightningObservation import LightningObservation
from aerisweather.responses.LightningResponse import LightningResponse
from .common_test_imports import *


class TestLightning:
    """ Defines tests modules for the Aeris API Lightning class """

    def test_static_data(self):
        """ Test the code against a known source of data """

        file = open("./responses/lightning.txt", "r")

        try:
            json_obj = json.loads(file.read())

            lt = LightningResponse(json_obj["response"][0])

            assert lt.id == "5cc207e8faae190634e6a642"

            location = lt.loc
            assert type(location) is AerisLocation
            assert location.long == approx(-89.15427)
            assert location.lat == approx(37.35702)

            ob = lt.ob
            assert type(ob) is LightningObservation
            assert ob.timestamp == 1556219867
            assert ob.dateTimeISO == "2019-04-25T19:17:47+00:00"
            assert ob.age == 199

            pulse = ob.pulse
            assert type(pulse) is LightningObservationPulse
            assert pulse.type == "cg"
            assert pulse.peakamp == -8246
            assert pulse.numSensors == 19
            assert pulse.icHeightM == 0
            assert pulse.icHeightFT == 0

            assert lt.recTimestamp == 1556219880
            assert lt.recISO == "2019-04-25T19:18:00+00:00"
            assert lt.age == 199

            rel = lt.relativeTo
            assert type(rel) == AerisRelativeTo
            assert rel.lat == approx(43.80136)
            assert rel.long == approx(-91.23958)
            assert rel.bearing == 167
            assert rel.bearingENG == "SSE"
            assert rel.distanceKM == approx(737.83)
            assert rel.distanceMI == approx(458.466)

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

            lght_list = awx.lightning(location=RequestLocation(postal_code="54601"),
                                      action=None,
                                      filter_=None,
                                      sort=None,
                                      params={ParameterType.LIGHTNING.RADIUS: "2000miles",
                                              ParameterType.LIGHTNING.LIMIT: "1"},
                                      query=None)

            for lght in lght_list:  # type: LightningResponse

                assert type(lght.loc) is AerisLocation
                assert type(lght.loc.long) is float
                ob = lght.ob
                assert type(ob) is LightningObservation

                pulse = ob.pulse
                assert type(pulse) is LightningObservationPulse

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex

    def test_lightning_method(self):
        """ Test the AerisWeather.lightning method """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            lght_list = awx.lightning(location=RequestLocation(postal_code="55124"),
                                        action=None,
                                        filter_=None,
                                        sort=None,
                                        params={ParameterType.LIGHTNING.RADIUS: "2000miles",
                                                ParameterType.LIGHTNING.LIMIT: "1"},
                                        query=None)

            for lght in lght_list:  # type: LightningResponse

                assert type(lght.loc) is AerisLocation
                assert type(lght.loc.long) is float
                ob = lght.ob
                assert type(ob) is LightningObservation

                pulse = ob.pulse
                assert type(pulse) is LightningObservationPulse

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex
