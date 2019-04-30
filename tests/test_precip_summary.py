from aerisweather.responses.AerisProfile import AerisProfilePrecipSummary
from aerisweather.responses.PrecipSummaryPeriod import PrecipSummaryPeriod
from aerisweather.responses.PrecipSummaryPeriodSummary import PrecipSummaryPeriodSummary
from aerisweather.responses.PrecipSummaryPeriodSummaryPrecip import PrecipSummaryPeriodSummaryPrecip
from aerisweather.responses.PrecipSummaryPeriodSummaryRange import PrecipSummaryPeriodSummaryRange
from aerisweather.responses.PrecipSummaryResponse import PrecipSummaryResponse
from .common_test_imports import *


class TestPrecipSummary:
    """ Defines tests modules for the Aeris API Precip Summary class """

    def test_static_data(self):
        """ Test the code against a known source of data """

        file = open("./responses/precip_summary.txt", "r")

        try:
            json_obj = json.loads(file.read())

            precip_summary = PrecipSummaryResponse(json_obj["response"][0])

            location = precip_summary.loc
            assert type(location) is AerisLocation

            assert location.lat == approx(43.80136, rel=1e-2)
            assert location.long == approx(-91.23958, rel=1e-2)

            place = precip_summary.place
            assert type(place) is AerisPlace
            assert place.name == "la crosse"
            assert place.state == "wi"
            assert place.country == "us"

            periods = precip_summary.periods
            assert type(periods) is list

            period = periods[0]
            assert type(period) is PrecipSummaryPeriod

            summary = period.summary
            assert type(summary) is PrecipSummaryPeriodSummary
            assert summary.timestamp == 1556600400
            assert summary.dateTimeISO == "2019-04-30T00:00:00-05:00"

            rge = summary.range
            assert type(rge) is PrecipSummaryPeriodSummaryRange
            assert rge.fromTimestamp == 1556600400
            assert rge.fromDateTimeISO == "2019-04-30T00:00:00-05:00"
            assert rge.toTimestamp == 1556686799
            assert rge.toDateTimeISO == "2019-04-30T23:59:59-05:00"
            assert rge.count == 2

            precip = summary.precip
            assert type(precip) is PrecipSummaryPeriodSummaryPrecip
            assert precip.totalMM == approx(0.31, rel=1e-2)
            assert precip.totalIN == approx(0.01, rel=1e-2)
            assert precip.count == 2

            profile = precip_summary.profile
            assert type(profile) is AerisProfilePrecipSummary
            assert profile.tz == "America/Chicago"

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

            endpoint = Endpoint(endpoint_type=EndpointType.PRECIP_SUMMARY,
                                location=RequestLocation(postal_code="54660"),
                                action=None,
                                filter_=None,
                                sort=None,
                                params=None,
                                query=None)

            precip_list = awx.request(endpoint=endpoint)

            assert len(precip_list) > 0

            for precip_summary in precip_list:  # type: PrecipSummaryResponse
                location = precip_summary.loc
                assert type(location) is AerisLocation

                place = precip_summary.place
                assert type(place) is AerisPlace

                periods = precip_summary.periods
                assert type(periods) is list

                period = periods[0]
                assert type(period) is PrecipSummaryPeriod

                summary = period.summary
                assert type(summary) is PrecipSummaryPeriodSummary

                rge = summary.range
                assert type(rge) is PrecipSummaryPeriodSummaryRange

                precip = summary.precip
                assert type(precip) is PrecipSummaryPeriodSummaryPrecip

                profile = precip_summary.profile
                assert type(profile) is AerisProfilePrecipSummary

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

            precip_list = awx.precip_summary(location=RequestLocation(postal_code="54660"),
                                             action=None,
                                             filter_=None,
                                             sort=None,
                                             params=None,
                                             query=None)

            for precip_summary in precip_list:  # type: PrecipSummaryResponse
                location = precip_summary.loc
                assert type(location) is AerisLocation

                place = precip_summary.place
                assert type(place) is AerisPlace

                periods = precip_summary.periods
                assert type(periods) is list

                period = periods[0]
                assert type(period) is PrecipSummaryPeriod

                summary = period.summary
                assert type(summary) is PrecipSummaryPeriodSummary

                rge = summary.range
                assert type(rge) is PrecipSummaryPeriodSummaryRange

                precip = summary.precip
                assert type(precip) is PrecipSummaryPeriodSummaryPrecip

                profile = precip_summary.profile
                assert type(profile) is AerisProfilePrecipSummary

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex
