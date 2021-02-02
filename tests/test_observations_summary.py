
import json
import os
import unittest
from urllib.error import URLError

from aerisweather.aerisweather import AerisWeather
from aerisweather.requests.Endpoint import Endpoint, EndpointType
from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestAction import RequestAction
from aerisweather.requests.RequestFilter import RequestFilter
from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.AerisPlace import AerisPlace
from aerisweather.responses.AerisProfile import AerisProfileObservationsSummary
from aerisweather.responses.ObservationsSummaryDewPt import ObservationsSummaryDewPt
from aerisweather.responses.ObservationsSummaryPeriod import ObservationsSummaryPeriod
from aerisweather.responses.ObservationsSummaryPrecip import ObservationsSummaryPrecip
from aerisweather.responses.ObservationsSummaryPressure import ObservationsSummaryPressure
from aerisweather.responses.ObservationsSummaryQC import ObservationsSummaryQC
from aerisweather.responses.ObservationsSummaryRange import ObservationsSummaryRange
from aerisweather.responses.ObservationsSummaryRelativeHumidity import ObservationsSummaryRelativeHumidity
from aerisweather.responses.ObservationsSummaryResponse import ObservationsSummaryResponse
from aerisweather.responses.ObservationsSummarySky import ObservationsSummarySky
from aerisweather.responses.ObservationsSummarySolrad import ObservationsSummarySolrad
from aerisweather.responses.ObservationsSummaryStationPressure import ObservationsSummaryStationPressure
from aerisweather.responses.ObservationsSummaryTemp import ObservationsSummaryTemp
from aerisweather.responses.ObservationsSummaryVisibility import ObservationsSummaryVisibility
from aerisweather.responses.ObservationsSummaryWeather import ObservationsSummaryWeather
from aerisweather.responses.ObservationsSummaryWind import ObservationsSummaryWind
from aerisweather.utils.AerisError import AerisError
from tests.keys import client_id, client_secret, app_id

script_dir = os.path.dirname(__file__)


class TestObservationsSummary(unittest.TestCase):
    """ Defines tests modules for the Aeris API ObservationsSummary class """

    def test_static_data(self):
        """ Test the ObservationsSummary code against a known source of data """

        file = open(os.path.join(script_dir, "responses/observations_summary.txt"), "r")

        try:
            json_obj = json.loads(file.read())

            obs_sum = ObservationsSummaryResponse(json_obj["response"][0])

            assert obs_sum.id == "KLSE"
            loc = obs_sum.loc
            assert type(loc) is AerisLocation
            assert loc.long == -91.25
            assert loc.lat == 43.883333333333

            place = obs_sum.place
            assert type(place) is AerisPlace
            assert place.name == "la crosse"
            assert place.state == "wi"
            assert place.country == "us"

            periods = obs_sum.periods
            summary_period = periods[0]
            assert type(summary_period) is ObservationsSummaryPeriod
            assert summary_period.timestamp == 1523250000
            assert summary_period.dateTimeISO == "2018-04-09T00:00:00-05:00"
            assert summary_period.ymd == 20180409

            range_ = summary_period.range
            assert type(range_) is ObservationsSummaryRange
            assert range_.maxTimestamp == 1523299980
            assert range_.maxDateTimeISO == "2018-04-09T13:53:00-05:00"
            assert range_.minTimestamp == 1523253180
            assert range_.minDateTimeISO == "2018-04-09T00:53:00-05:00"
            assert range_.count == 23

            temp = summary_period.temp
            assert type(temp) is ObservationsSummaryTemp
            assert temp.maxC == 5
            assert temp.maxF == 41
            assert temp.minC == -3
            assert temp.minF == 26
            assert temp.avgC == -0.6
            assert temp.avgF == 30.9
            assert temp.count == 23

            dewpt = summary_period.dewpt
            assert type(dewpt) is ObservationsSummaryDewPt
            assert dewpt.maxC == -3
            assert dewpt.maxF == 27
            assert dewpt.minC == -9
            assert dewpt.minF == 15
            assert dewpt.avgC == -4.5
            assert dewpt.avgF == 24
            assert dewpt.count == 23

            rh = summary_period.rh
            assert type(rh) is ObservationsSummaryRelativeHumidity
            assert rh.max == 93
            assert rh.min == 38
            assert rh.avg == 78
            assert rh.count == 23

            pressure = summary_period.pressure
            assert type(pressure) is ObservationsSummaryPressure
            assert pressure.maxMB == 1024
            assert pressure.maxIN == 30.24
            assert pressure.minMB == 1020
            assert pressure.minIN == 30.12
            assert pressure.avgMB == 1021.4
            assert pressure.avgIN == 30.16
            assert pressure.count == 23

            visibility = summary_period.visibility
            assert type(visibility) is ObservationsSummaryVisibility
            assert visibility.maxKM == 16
            assert visibility.maxMI == 10
            assert visibility.minKM == 3
            assert visibility.minMI == 2
            assert visibility.count == 23
            assert visibility.avgKM == 11
            assert visibility.avgMI == 6.8

            wind = summary_period.wind
            assert type(wind) is ObservationsSummaryWind
            assert wind.maxKTS == 9
            assert wind.maxKPH == 17
            assert wind.maxMPH == 10
            assert wind.gustKTS == 15
            assert wind.gustKPH == 28
            assert wind.gustMPH == 17
            assert wind.count == 23
            assert wind.minKTS == 0
            assert wind.minKPH == 0
            assert wind.minMPH == 0
            assert wind.avgKTS == 2
            assert wind.avgKPH == 3.7
            assert wind.avgMPH == 2.3

            precip = summary_period.precip
            assert type(precip) is ObservationsSummaryPrecip
            assert precip.totalMM == 0.25
            assert precip.totalIN == 0.01
            assert precip.count == 12
            assert precip.trace is True
            assert precip.traceCount == 9
            assert precip.QC == "G"
            assert precip.method == "sum"
            assert precip.QCcode == 10

            weather = summary_period.weather
            assert type(weather) is ObservationsSummaryWeather
            assert weather.coded[0] == "::H"
            assert weather.coded[1] == ":L:S"
            assert weather.coded[2] == "::BR"
            assert weather.count == 3
            assert weather.phrase == "Mostly Cloudy with Haze"
            assert weather.primary == "Haze"
            assert weather.primaryCoded == "::H"
            assert weather.icon == "cloudy.png"

            sky = summary_period.sky
            assert type(sky) is ObservationsSummarySky
            assert sky.max == 100
            assert sky.min == 44
            assert sky.avg == 90
            assert sky.count == 23
            assert sky.coded[0] == "OV"
            assert sky.coded[1] == "SC"
            assert sky.coded[2] == "BK"

            solrad = summary_period.solrad
            assert type(solrad) is ObservationsSummarySolrad
            assert solrad.maxWM2 is None
            assert solrad.minWM2 is None
            assert solrad.avgWM2 is None
            assert solrad.totalWM2 is None
            assert solrad.method is None
            assert solrad.count == 0

            QC = summary_period.QC
            assert type(QC) is ObservationsSummaryQC
            assert QC.max == 10
            assert QC.min == 10
            assert QC.types[0] == "O"
            assert QC.count == 23

            spressure = summary_period.spressure
            assert type(spressure) is ObservationsSummaryStationPressure
            assert spressure.maxMB == 999
            assert spressure.maxIN == 29.5
            assert spressure.minMB == 995
            assert spressure.minIN == 29.38
            assert spressure.avgMB == 996.6
            assert spressure.avgIN == 29.43
            assert spressure.count == 23

            profile = obs_sum.profile
            assert type(profile) is AerisProfileObservationsSummary
            assert profile.tz == "America/Chicago"
            assert profile.elevM == 199
            assert profile.elevFT == 653
            assert profile.hasPrecip is True

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
        """ Test the ObservationSummary code against a live response from the API """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            endpoint = Endpoint(endpoint_type=EndpointType.OBSERVATIONS_SUMMARY,
                                location=None,
                                action=RequestAction.OBSERVATIONS_SUMMARY.CLOSEST,
                                filter_=[RequestFilter.OBSERVATIONS_SUMMARY.ALL_STATIONS],
                                sort=None,
                                params={ParameterType.OBSERVATIONS_SUMMARY.P: "54601"},
                                query=None)

            obs_sum_list = awx.request(endpoint=endpoint)

            for obs_sum in obs_sum_list:
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

    def test_observations_method(self):
        """ Test the AerisWeather.observations_summary method """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            obs_sum_list = awx.observations_summary(location=None,
                                                    action=RequestAction.OBSERVATIONS_SUMMARY.CLOSEST,
                                                    filter_=[RequestFilter.OBSERVATIONS_SUMMARY.ALL_STATIONS],
                                                    sort=None,
                                                    params={ParameterType.OBSERVATIONS_SUMMARY.P: "54601"},
                                                    query=None)

            for obs_sum in obs_sum_list:  # type: ObservationsSummaryResponse
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


suite = unittest.TestLoader().loadTestsFromTestCase(TestObservationsSummary)
unittest.TextTestRunner(verbosity=2).run(suite)
