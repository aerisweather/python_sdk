from aerisweather.responses.LightningSummaryICHeight import LightningSummaryICHeight
from aerisweather.responses.LightningSummaryNumSensors import LightningSummaryNumSensors
from aerisweather.responses.LightningSummaryPeakAmp import LightningSummaryPeakAmp
from aerisweather.responses.LightningSummaryPeakAmpValues import LightningSummaryPeakAmpValues
from aerisweather.responses.LightningSummaryPulse import LightningSummaryPulse
from aerisweather.responses.LightningSummaryRange import LightningSummaryRange
from aerisweather.responses.LightningSummaryResponse import LightningSummaryResponse
from aerisweather.responses.LightningSummarySummary import LightningSummarySummary
from .common_test_imports import *


class TestLightningSummary:
    """ Defines tests modules for the Aeris API LightningSummary class """

    def test_static_data(self):
        """ Test the code against a known source of data """

        file = open("./responses/lightning_summary.txt", "r")

        try:
            json_obj = json.loads(file.read())

            ltsum = LightningSummaryResponse(json_obj["response"][0])
            assert type(ltsum) is LightningSummaryResponse

            summary = ltsum.summary
            assert type(summary) is LightningSummarySummary

            sumrange = summary.range
            assert type(sumrange) is LightningSummaryRange
            assert sumrange.count == 21
            assert sumrange.fromTimestamp == 1556545169
            assert sumrange.fromDateTimeISO == "2019-04-29T13:39:29+00:00"
            assert sumrange.toTimestamp == 1556545469
            assert sumrange.toDateTimeISO == "2019-04-29T13:44:29+00:00"
            assert sumrange.maxTimestamp == 1556545400
            assert sumrange.maxDateTimeISO == "2019-04-29T13:43:20+00:00"
            assert sumrange.minTimestamp == 1556545193
            assert sumrange.minDateTimeISO == "2019-04-29T13:39:53+00:00"

            pulse = summary.pulse
            assert type(pulse) is LightningSummaryPulse
            assert pulse.count == 21
            assert pulse.cg == 21
            assert pulse.ic == 0
            assert pulse.negative == 18
            assert pulse.positive == 3

            peak_amp = summary.peakAmp
            assert type(peak_amp) is LightningSummaryPeakAmp
            assert peak_amp.count == 21

            peak_all = peak_amp.all
            assert type(peak_all)  is LightningSummaryPeakAmpValues
            assert peak_all.min == 6365
            assert peak_all.max == 51510
            assert peak_all.avg == 27362

            peak_pos = peak_amp.positive
            assert type(peak_pos) is LightningSummaryPeakAmpValues
            assert peak_pos.min == 31770
            assert peak_pos.max == 42504
            assert peak_pos.avg == 36278

            peak_neg = peak_amp.negative
            assert type(peak_neg) is LightningSummaryPeakAmpValues
            assert peak_neg.min == 6365
            assert peak_neg.max == 51510
            assert peak_neg.avg == 25876

            ic_height = summary.icHeight
            assert type(ic_height) is LightningSummaryICHeight
            assert ic_height.count == 21
            assert ic_height.min == 0
            assert ic_height.max == 0
            assert ic_height.avg == 0

            num_sensors = summary.numSensors
            assert type(num_sensors) is LightningSummaryNumSensors
            assert num_sensors.count == 21
            assert num_sensors.min == 5
            assert num_sensors.max == 20
            assert num_sensors.avg == 15

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

            lght_sum_list = awx.lightning_summary(location=None,
                                                  action=RequestAction.LIGHTNING_SUMMARY.CLOSEST,
                                                  filter_=None,
                                                  sort=None,
                                                  params={ParameterType.LIGHTNING_SUMMARY.P: "55124",
                                                          ParameterType.LIGHTNING_SUMMARY.RADIUS: "2000miles"},
                                                  query=None)

            for lght_sum in lght_sum_list:  # type: LightningSummaryResponse

                summary = lght_sum.summary
                assert type(summary) is LightningSummarySummary

                sumrange = summary.range
                assert type(sumrange) is LightningSummaryRange

                pulse = summary.pulse
                assert type(pulse) is LightningSummaryPulse

                peak_amp = summary.peakAmp
                assert type(peak_amp) is LightningSummaryPeakAmp

                peak_all = peak_amp.all
                assert type(peak_all) is LightningSummaryPeakAmpValues

                peak_pos = peak_amp.positive
                assert type(peak_pos) is LightningSummaryPeakAmpValues

                peak_neg = peak_amp.negative
                assert type(peak_neg) is LightningSummaryPeakAmpValues

                ic_height = summary.icHeight
                assert type(ic_height) is LightningSummaryICHeight

                num_sensors = summary.numSensors
                assert type(num_sensors) is LightningSummaryNumSensors

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

            lght_sum_list = awx.lightning_summary(location=None,
                                                  action=RequestAction.LIGHTNING_SUMMARY.CLOSEST,
                                                  filter_=None,
                                                  sort=None,
                                                  params={ParameterType.LIGHTNING_SUMMARY.P: "55124",
                                                          ParameterType.LIGHTNING_SUMMARY.RADIUS: "2000miles"},
                                                  query=None)

            for lght_sum in lght_sum_list:  # type: LightningSummaryResponse
                summary = lght_sum.summary
                assert type(summary) is LightningSummarySummary

                sumrange = summary.range
                assert type(sumrange) is LightningSummaryRange

                pulse = summary.pulse
                assert type(pulse) is LightningSummaryPulse

                peak_amp = summary.peakAmp
                assert type(peak_amp) is LightningSummaryPeakAmp

                peak_all = peak_amp.all
                assert type(peak_all) is LightningSummaryPeakAmpValues

                peak_pos = peak_amp.positive
                assert type(peak_pos) is LightningSummaryPeakAmpValues

                peak_neg = peak_amp.negative
                assert type(peak_neg) is LightningSummaryPeakAmpValues

                ic_height = summary.icHeight
                assert type(ic_height) is LightningSummaryICHeight

                num_sensors = summary.numSensors
                assert type(num_sensors) is LightningSummaryNumSensors

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex
