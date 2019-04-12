
from .common_test_imports import *
from aerisweather.responses.AerisProfile import AerisProfileAirQuality
from aerisweather.responses.AirQualityPeriod import AirQualityPeriod
from aerisweather.responses.AirQualityResponse import AirQualityResponse


class TestAirQuality:
    """ Defines tests modules for the Aeris API Air Quality class """

    def test_static_data(self):
        """ Test the code against a known source of data """

        file = open("./responses/airquality.txt", "r")

        try:
            json_obj = json.loads(file.read())

            aqi = AirQualityResponse(json_obj["response"][0])

            assert aqi.id is None

            assert type(aqi.loc) is AerisLocation
            assert type(aqi.loc.long) is float
            assert aqi.loc.lat == 43.97858
            assert aqi.loc.long == -90.50402

            place = aqi.place
            assert place.name == "tomah"
            assert place.state == "wi"
            assert place.country == "us"

            periods = aqi.periods
            assert len(periods) == 1
            assert type(periods[0]) == AirQualityPeriod
            p0 = periods[0]
            assert p0.dateTimeISO == "2019-04-09T10:00:00-05:00"
            assert p0.timestamp == 1554822000
            assert p0.aqi == 30
            assert p0.category == "good"
            assert p0.color == "00E400"
            assert p0.method == "airnow"
            assert p0.dominant == "o3"

            pollutants = p0.pollutants
            poll0 = pollutants[0]
            assert poll0.type == "o3"
            assert poll0.name == "ozone"
            assert poll0.valuePPB == 33
            assert poll0.valueUGM3 == 68
            assert poll0.aqi == 30
            assert poll0.category == "good"
            assert poll0.color == "00E400"

            assert type(aqi.profile) is AerisProfileAirQuality
            profile = aqi.profile
            assert profile.tz == "America/Chicago"
            sources = aqi.profile.sources
            assert sources[0]["name"] == "CAMS"

            stations = aqi.profile.stations
            assert stations is None

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
