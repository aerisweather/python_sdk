from aerisweather.responses.AerisProfile import AerisProfile
from aerisweather.responses.ThreatsPeriod import ThreatsPeriod
from aerisweather.responses.ThreatsResponse import ThreatsResponse
from aerisweather.responses.ObservationsResponse import ObservationsResponse
from aerisweather.responses.ThreatsStorms import ThreatsStorms
from aerisweather.responses.ThreatsStormsDBZ import ThreatsStormsDBZ
from aerisweather.responses.ThreatsStormsDirection import ThreatsStormsDirection
from aerisweather.responses.ThreatsStormsDistance import ThreatsStormsDistance
from aerisweather.responses.ThreatsStormsMDA import ThreatsStormsMDA
from aerisweather.responses.ThreatsStormsPhrase import ThreatsStormsPhrase
from aerisweather.responses.ThreatsStormsSpeed import ThreatsStormsSpeed
from .common_test_imports import *


class TestThreats:
    """ Defines tests modules for the Aeris API Threats class """

    def test_static_data(self):
        """ Test the Observation code against a known source of data """

        file = open("./responses/threats.txt", "r")

        try:
            json_obj = json.loads(file.read())

            threat = ThreatsResponse(json_obj["response"][0])
            assert type(threat) is ThreatsResponse

            loc = threat.loc
            assert type(loc) is AerisLocation
            assert loc.lat == 43.97858
            assert loc.long == -90.50402

            place = threat.place
            assert type(place) is AerisPlace
            assert place.name == "tomah"
            assert place.state == "wi"
            assert place.country == "us"

            profile = threat.profile
            assert type(profile) is AerisProfile
            assert profile.tz == "America/Chicago"

            periods = threat.periods
            assert type(periods) is list

            period = periods[0]
            assert type(period) is ThreatsPeriod
            assert period.timestamp == 1556750299
            assert period.dateTimeISO == "2019-05-01T17:38:19-05:00"

            storms = period.storms
            assert type(storms) is ThreatsStorms

            phrase = storms.phrase
            assert type(phrase) is ThreatsStormsPhrase
            assert phrase.long == "An area of heavy precipitation is approaching from the SW with frequent lightning possible."
            assert phrase.short == "An area of heavy precipitation is approaching from the SW with frequent lightning possible."

            distance = storms.distance
            assert type(distance) is ThreatsStormsDistance
            assert distance.minKM == 531.2
            assert distance.minMI == 330.1
            assert distance.maxKM == 531.2
            assert distance.maxMI == 330.1
            assert distance.avgKM == 531.2
            assert distance.avgMI == 330.1

            direction = storms.direction
            assert type(direction) is ThreatsStormsDirection
            assert direction.toDEG == 54
            assert direction.to == "NE"
            assert direction.fromDEG == 234
            assert direction.from_ == "SW"

            assert storms.approaching is True

            speed = storms.speed
            assert type(speed) is ThreatsStormsSpeed
            assert speed.minKTS == 39
            assert speed.minKPH == 72.2
            assert speed.minMPH == 44.9
            assert speed.maxKTS == 39
            assert speed.maxKPH == 72.2
            assert speed.maxMPH == 44.9
            assert speed.avgKTS == 39
            assert speed.avgKPH == 72.2
            assert speed.avgMPH == 44.9

            assert storms.span == 45
            assert storms.hail is None
            assert storms.rotation is False
            assert storms.tornadic is False
            assert storms.advisories is None

            mda = storms.mda
            assert type(mda) is ThreatsStormsMDA
            assert mda.max is None
            assert mda.min is None

            dbz = storms.dbz
            assert type(dbz) is ThreatsStormsDBZ
            assert dbz.min == 41
            assert dbz.max == 41
            assert dbz.avg == 41

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

            endpoint = Endpoint(endpoint_type=EndpointType.THREATS,
                                location=RequestLocation(postal_code="54601"),
                                action=None,
                                filter_=None,
                                sort=None,
                                params={ParameterType.THREATS.RADIUS: "4000miles"},
                                query=None)

            t_list = awx.request(endpoint=endpoint)

            assert len(t_list) > 0

            for threat in t_list:
                assert type(threat) is ThreatsResponse

                loc = threat.loc
                assert type(loc) is AerisLocation

                place = threat.place
                assert type(place) is AerisPlace

                profile = threat.profile
                assert type(profile) is AerisProfile

                periods = threat.periods
                assert type(periods) is list

                period = periods[0]
                assert type(period) is ThreatsPeriod

                storms = period.storms
                assert type(storms) is ThreatsStorms

                storms = period.storms
                if storms is not None:
                    assert type(storms) is ThreatsStorms

                    phrase = storms.phrase
                    if phrase is not None:
                        assert type(phrase) is ThreatsStormsPhrase

                    distance = storms.distance
                    if distance is not None:
                        assert type(distance) is ThreatsStormsDistance

                    direction = storms.direction
                    if direction is not None:
                        assert type(direction) is ThreatsStormsDirection

                    speed = storms.speed
                    if speed is not None:
                        assert type(speed) is ThreatsStormsSpeed

                    mda = storms.mda
                    if mda is not None:
                        assert type(mda) is ThreatsStormsMDA

                    dbz = storms.dbz
                    if dbz is not None:
                        assert type(dbz) is ThreatsStormsDBZ

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

            t_list = awx.threats(location=RequestLocation(postal_code="54601"),
                                 action=None,
                                 filter_=None,
                                 sort=None,
                                 params={ParameterType.THREATS.RADIUS: "4000miles"},
                                 query=None)

            for threat in t_list:
                assert type(threat) is ThreatsResponse

                loc = threat.loc
                assert type(loc) is AerisLocation

                place = threat.place
                assert type(place) is AerisPlace

                profile = threat.profile
                assert type(profile) is AerisProfile

                periods = threat.periods
                assert type(periods) is list

                period = periods[0]
                assert type(period) is ThreatsPeriod

                storms = period.storms
                if storms is not None:
                    assert type(storms) is ThreatsStorms

                    phrase = storms.phrase
                    if phrase is not None:
                        assert type(phrase) is ThreatsStormsPhrase

                    distance = storms.distance
                    if distance is not None:
                        assert type(distance) is ThreatsStormsDistance

                    direction = storms.direction
                    if direction is not None:
                        assert type(direction) is ThreatsStormsDirection

                    speed = storms.speed
                    if speed is not None:
                        assert type(speed) is ThreatsStormsSpeed

                    mda = storms.mda
                    if mda is not None:
                        assert type(mda) is ThreatsStormsMDA

                    dbz = storms.dbz
                    if dbz is not None:
                        assert type(dbz) is ThreatsStormsDBZ

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex
