
import json
import unittest
from urllib.error import URLError

from aerisweather.aerisweather import AerisWeather
from aerisweather.requests.Endpoint import Endpoint, EndpointType
from aerisweather.requests.RequestFilter import RequestFilter
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.responses.AerisPlace import AerisPlace
from aerisweather.responses.AerisProfile import AerisProfileAlerts
from aerisweather.responses.AlertsResponse import AlertsResponse
from aerisweather.responses.AlertDetails import AlertDetails
from aerisweather.responses.AlertIncludes import AlertIncludes
from aerisweather.responses.AlertTimestamps import AlertTimestamps
from aerisweather.utils.AerisError import AerisError
from tests.keys import client_id, client_secret, app_id


class TestAlerts(unittest.TestCase):
    """ Defines tests modules for the Aeris API Alerts/Advisories class """

    def test_static_data(self):
        """ Test the code against a known source of data """

        file = open("./responses/alerts.txt", "r")

        try:
            json_obj = json.loads(file.read())

            alerts = AlertsResponse(json_obj["response"][0])
            assert alerts is not None
            assert alerts.id == "2ac0f0296cf81497a20c826d36f50305"

            details = alerts.details
            assert type(details) == AlertDetails
            assert details.type == "BH.S"
            assert details.name == "STATEMENT"
            assert details.loc == "TXZ238"
            assert details.emergency is False
            assert details.color == "40E0D0"
            assert details.cat == "beach"
            assert details.body == "...HIGH RIP CURRENT RISK TODAY...\n\n.ELEVATED SURF AND A HIGH RISK OF RIP " + \
                "CURRENTS WILL CONTINUE"
            assert details.bodyFull == "WHUS44 KHGX 290914\nCFWHGX\n\nCOASTAL HAZARD MESSAGE\nNATIONAL " + \
                "WEATHER SERVICE HOUSTON/GALVESTON"

            timestamps = alerts.timestamps
            assert type(timestamps) == AlertTimestamps
            assert timestamps.issued == 1522314840
            assert timestamps.issuedISO == "2018-03-29T04:14:00-05:00"
            assert timestamps.begins == 1522314840
            assert timestamps.beginsISO == "2018-03-29T04:14:00-05:00"
            assert timestamps.expires == 1522357200
            assert timestamps.expiresISO == "2018-03-29T16:00:00-05:00"
            assert timestamps.added == 1522318202
            assert timestamps.addedISO == "2018-03-29T05:10:02-05:00"

            assert alerts.poly == ""
            assert alerts.geoPoly is None

            includes = alerts.includes
            assert type(includes) == AlertIncludes
            assert includes.counties == []
            assert includes.fips == ["48039", "48071"]
            assert includes.wxzones == ["TXZ214", "TXZ236"]
            assert includes.zipcodes == [77404, 77414]

            place = alerts.place
            assert type(place) == AerisPlace
            assert place.name == "galveston"
            assert place.state == "tx"
            assert place.country == "us"

            profile = alerts.profile
            assert type(profile) == AerisProfileAlerts
            assert profile.tz == "America/Chicago"

            assert alerts.active is True

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
        """ Test the Alerts code against a live response from the API """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            endpoint = Endpoint(endpoint_type=EndpointType.ALERTS,
                                location=RequestLocation(postal_code="55124"),
                                action=None,
                                filter_=[RequestFilter.ALERTS.ALL],
                                sort=None,
                                params=None,
                                query=None)

            alerts_list = awx.request(endpoint=endpoint)

            for alert in alerts_list:  # type: AlertsResponse
                assert alert.place is not None
                timestamps = alert.timestamps
                assert type(timestamps) == AlertTimestamps
                assert timestamps.issued is not None
                includes = alert.includes
                assert type(includes) is AlertIncludes
                assert includes.wxzones is not None
                assert alert.active is True

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex

    def test_alerts_method(self):
        """ Test the AerisWeather.alerts method """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            alerts_list = awx.alerts(location=RequestLocation(postal_code="55124"),
                                     action=None,
                                     filter_=[RequestFilter.ALERTS.ALL],
                                     sort=None,
                                     params=None,
                                     query=None)

            for alert in alerts_list:  # type: AlertsResponse
                assert alert.place is not None
                timestamps = alert.timestamps
                assert type(timestamps) == AlertTimestamps
                assert timestamps.issued is not None
                includes = alert.includes
                assert type(includes) is AlertIncludes
                assert includes.wxzones is not None
                assert alert.active is True

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex


suite = unittest.TestLoader().loadTestsFromTestCase(TestAlerts)
unittest.TextTestRunner(verbosity=2).run(suite)
