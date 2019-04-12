
import json
from urllib.error import URLError

from aerisweather.aerisweather import AerisWeather
from aerisweather.endpoints.Endpoint import Endpoint, EndpointType
from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestAction import RequestAction
from aerisweather.requests.RequestFilter import RequestFilter
from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.AerisPlace import AerisPlacePlaces
from aerisweather.responses.AerisProfile import AerisProfilePlaces
from aerisweather.responses.PlacesResponse import PlacesResponse
from aerisweather.utils.AerisError import AerisError
from tests.keys import client_id, client_secret, app_id


class TestPlaces:
    """ Defines tests modules for the Aeris API Places class """

    def test_static_data(self):
        """ Test the Places code against a known source of data """

        file = open("./responses/places.txt", "r")

        try:
            json_obj = json.loads(file.read())

            places = PlacesResponse(json_obj["response"])
            assert type(places) is PlacesResponse

            loc = places.loc
            assert type(loc) is AerisLocation
            assert type(loc.long) is float
            assert loc.lat == 43.80136
            assert loc.long == -91.23958

            place = places.place
            assert type(place) is AerisPlacePlaces
            assert place.name == "La Crosse"
            assert place.state == "WI"
            assert place.stateFull == "Wisconsin"
            assert place.country == "US"
            assert place.countryFull == "United States"
            assert place.region == "usnc"
            assert place.regionFull == "North Central"
            assert place.continent == "na"
            assert place.continentFull == "North America"

            profile = places.profile
            assert type(profile) is AerisProfilePlaces
            assert profile.elevM == 204
            assert profile.elevFT == 669
            assert profile.pop == 52306
            assert profile.tz == "America/Chicago"
            assert profile.tzName == "CDT"
            assert profile.tzOffset == -18000
            assert profile.isDST is True

            wxzone = profile.wxzone
            assert type(wxzone) is list
            assert wxzone[0] == "WIZ041"

            firezone = profile.firezone
            assert type(firezone) is list
            assert firezone[0] == "WIZ041"

            fips = profile.fips
            assert type(fips) is list
            assert fips[0] == "55063"

            countyid = profile.countyid
            assert type(countyid) is list
            assert countyid[0] == "WIC063"

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
        """ Test the Places code against a live response from the API """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            endpoint = Endpoint(endpoint_type=EndpointType.PLACES,
                                location=None,
                                action=RequestAction.PLACES.CLOSEST,
                                filter_=[RequestFilter.PLACES.AIRPORT],
                                sort=None,
                                params={ParameterType.PLACES.P: "54601"})

            places_list = awx.request(endpoint=endpoint)

            for places in places_list:

                assert type(places) is PlacesResponse

                loc = places.loc
                assert type(loc) is AerisLocation
                assert type(loc.long) is not None

                place = places.place
                assert type(place) is AerisPlacePlaces
                assert place.name is not None
                assert place.state == "WI"
                assert place.stateFull == "Wisconsin"
                assert place.country == "US"
                assert place.countryFull == "United States"
                assert place.region == "usnc"
                assert place.regionFull == "North Central"
                assert place.continent == "na"
                assert place.continentFull == "North America"

                profile = places.profile
                assert type(profile) is AerisProfilePlaces
                assert profile.elevM is not None

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex

    def test_places_method(self):
        """ Test the AerisWeather.places method """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            places_list = awx.places(location=None,
                                     action=RequestAction.PLACES.CLOSEST,
                                     filter_=[RequestFilter.PLACES.AIRPORT],
                                     sort=None,
                                     params={ParameterType.PLACES.P: "54601"})

            for places in places_list:
                assert type(places) is PlacesResponse

                loc = places.loc
                assert type(loc) is AerisLocation
                assert type(loc.long) is not None

                place = places.place
                assert type(place) is AerisPlacePlaces
                assert place.name is not None
                assert place.state == "WI"
                assert place.stateFull == "Wisconsin"
                assert place.country == "US"
                assert place.countryFull == "United States"
                assert place.region == "usnc"
                assert place.regionFull == "North Central"
                assert place.continent == "na"
                assert place.continentFull == "North America"

                profile = places.profile
                assert type(profile) is AerisProfilePlaces
                assert profile.elevM is not None

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex
