from aerisweather.responses.TropicalCyclonesDetails import TropicalCyclonesDetails
from aerisweather.responses.TropicalCyclonesDetailsMovement import TropicalCyclonesDetailsMovement
from aerisweather.responses.TropicalCyclonesLocation import TropicalCyclonesLocation
from aerisweather.responses.TropicalCyclonesPosition import TropicalCyclonesPosition
from aerisweather.responses.TropicalCyclonesProfile import TropicalCyclonesProfile
from aerisweather.responses.TropicalCyclonesProfileLifespan import TropicalCyclonesProfileLifespan
from aerisweather.responses.TropicalCyclonesProfilePressure import TropicalCyclonesProfilePressure
from aerisweather.responses.TropicalCyclonesProfileWindSpeed import TropicalCyclonesProfileWindSpeed
from aerisweather.responses.TropicalCyclonesResponse import TropicalCyclonesResponse
from .common_test_imports import *


class TestTropicalCyclones:
    """ Defines tests modules for the Aeris API TropicalCyclones class """

    def test_static_data(self):
        """ Test the code against a known source of data """

        file = open("./responses/tropicalcyclones.txt", "r")

        try:
            json_obj = json.loads(file.read())

            trop = TropicalCyclonesResponse(json_obj["response"][0])
            assert type(trop) is TropicalCyclonesResponse

            assert trop.id == "2017-AL-80"

            profile = trop.profile
            assert type(profile) is TropicalCyclonesProfile
            assert profile.basinOrigin == "AL"
            assert profile.basinCurrent == "AL"

            assert profile.basins[0] == "AL"
            assert profile.name == "Nate"
            assert profile.year == 2017
            assert profile.event == 16
            assert profile.isActive is True

            lifespan = profile.lifespan
            assert type(lifespan) is TropicalCyclonesProfileLifespan
            assert lifespan.startTimestamp == 1507129200
            assert lifespan.startDateTimeISO == "2017-10-04T10:00:00-05:00"
            assert lifespan.endTimestamp is None
            assert lifespan.endDateTimeISO is None

            assert profile.maxStormType == "H"
            assert profile.maxStormCat == "H1"

            windSpeed = profile.windSpeed
            assert type(windSpeed) is TropicalCyclonesProfileWindSpeed
            assert windSpeed.maxKTS == 78.1
            assert windSpeed.maxKPH == 145
            assert windSpeed.maxMPH == 90
            assert windSpeed.maxTimestamp == 1507388400
            assert windSpeed.maxDateTimeISO == "2017-10-07T10:00:00-05:00"

            pressure = profile.pressure
            assert type(pressure) is TropicalCyclonesProfilePressure
            assert pressure.minMB == 981
            assert pressure.minIN == 28.97
            assert pressure.minTimestamp == 1507410000
            assert pressure.minDateTimeISO == "2017-10-07T16:00:00-05:00"

            assert profile.boundingBox[0] == 12.2
            assert profile.boundingBox[1] == -89.3
            assert profile.boundingBox[2] == 42
            assert profile.boundingBox[3] == -70

            assert profile.tz == "America/Cancun"

            position = trop.position
            assert type(position) is TropicalCyclonesPosition

            locn = position.location
            assert type(locn) is TropicalCyclonesLocation
            assert locn.type == "Point"
            assert locn.coordinates[0] == -85
            assert locn.coordinates[1] == 18.7

            details = position.details
            assert type(details) is TropicalCyclonesDetails
            assert details.basin == "AL"
            assert details.stormType == "TS"
            assert details.stormCat == "TS"
            assert details.stormName == "Tropical Storm Nate"
            assert details.stormShortName == "Nate"
            assert details.advisoryNumber == "9"

            movement = details.movement
            assert type(movement) is TropicalCyclonesDetailsMovement
            assert movement.directionDEG == 337.5
            assert movement.direction == "NNW"
            assert movement.speedKTS == 18.2
            assert movement.speedKPH == 34
            assert movement.speedMPH == 21

            assert details.windSpeedKTS == 43.4
            assert details.windSpeedKPH == 80
            assert details.windSpeedMPH == 50
            assert details.gustSpeedKTS is None
            assert details.gustSpeedKPH is None
            assert details.gustSpeedMPH is None
            assert details.pressureMB == 996
            assert details.pressureIN == 29.41

            assert position.timestamp == 1507302000
            assert position.dateTimeISO == "2017-10-06T10:00:00-05:00"

            loc = position.loc
            assert type(loc) is AerisLocation
            assert loc.long == -85
            assert loc.lat == 18.7

            track = trop.track
            assert type(track) is list
            t_location = track[0].location
            assert t_location.type == "Point"
            assert t_location.coordinates[0] == -81.9
            assert t_location.coordinates[1] == 12.2

            details = position.details
            assert type(details) is TropicalCyclonesDetails
            assert details.basin == "AL"
            assert details.stormType == "TS"
            assert details.stormCat == "TS"
            assert details.stormName == "Tropical Storm Nate"
            assert details.stormShortName == "Nate"
            assert details.advisoryNumber == "9"

            movement = details.movement
            assert type(movement) is TropicalCyclonesDetailsMovement
            assert movement.directionDEG == 337.5
            assert movement.direction == "NNW"
            assert movement.speedKTS == 18.2
            assert movement.speedKPH == 34
            assert movement.speedMPH == 21

            assert details.windSpeedKTS == 43.4
            assert details.windSpeedKPH == 80
            assert details.windSpeedMPH == 50
            assert details.gustSpeedKTS is None
            assert details.gustSpeedKPH is None
            assert details.gustSpeedMPH is None
            assert details.pressureMB == 996
            assert details.pressureIN == 29.41

            assert position.timestamp == 1507302000
            assert position.dateTimeISO == "2017-10-06T10:00:00-05:00"
            loc = position.loc
            assert type(loc) is AerisLocation
            assert loc.long == -85
            assert loc.lat == 18.7

            forecast = trop.forecast
            assert type(forecast) is list
            location = forecast[0].location
            assert type(location) is TropicalCyclonesLocation
            assert location.type == "Point"
            assert location.coordinates[0] == -86.3
            assert location.coordinates[1] == 21.3

            details = position.details
            assert type(details) is TropicalCyclonesDetails
            assert details.basin == "AL"
            assert details.stormType == "TS"
            assert details.stormCat == "TS"
            assert details.stormName == "Tropical Storm Nate"
            assert details.stormShortName == "Nate"
            assert details.advisoryNumber == "9"

            movement = details.movement
            assert type(movement) is TropicalCyclonesDetailsMovement
            assert movement.directionDEG == 337.5
            assert movement.direction == "NNW"
            assert movement.speedKTS == 18.2
            assert movement.speedKPH == 34
            assert movement.speedMPH == 21

            assert details.windSpeedKTS == 43.4
            assert details.windSpeedKPH == 80
            assert details.windSpeedMPH == 50
            assert details.gustSpeedKTS is None
            assert details.gustSpeedKPH is None
            assert details.gustSpeedMPH is None
            assert details.pressureMB == 996
            assert details.pressureIN == 29.41

            assert position.timestamp == 1507302000
            assert position.dateTimeISO == "2017-10-06T10:00:00-05:00"

            loc = position.loc
            assert loc.long == -85
            assert loc.lat == 18.7
            breakpoints = trop.breakPointAlerts
            assert type(breakpoints) is list
            assert breakpoints[0].alertType == "TR.A"
            coords = breakpoints[0].coords
            assert coords.type == "LineString"
            assert coords.coordinates[0][0] == -86.4
            assert coords.coordinates[0][1] == 30.38

            assert coords.coordinates[1][0] == -86.33
            assert coords.coordinates[1][1] == 30.48

            errorCone = trop.errorCone
            assert errorCone.type == "Polygon"
            assert errorCone.coordinates[0][0][0] == -85.04926
            assert errorCone.coordinates[0][0][1] == 18.36815

            assert errorCone.coordinates[0][1][0] == -85.01604
            assert errorCone.coordinates[0][1][1] == 18.36752

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

            endpoint = Endpoint(endpoint_type=EndpointType.TROPICAL_CYCLONES,
                                location=RequestLocation(postal_code="54660"),
                                action=None,
                                filter_={RequestFilter.TROPICAL_CYCLONE.TEST},
                                sort=None,
                                params={ParameterType.TROPICAL_CYCLONE.RADIUS: "2000miles"},
                                query=None)

            trop_list = awx.request(endpoint=endpoint)

            for trop in trop_list:  # type: TropicalCyclonesResponse
                assert type(trop) is TropicalCyclonesResponse

                profile = trop.profile
                assert type(profile) is TropicalCyclonesProfile

                lifespan = profile.lifespan
                assert type(lifespan) is TropicalCyclonesProfileLifespan

                windSpeed = profile.windSpeed
                assert type(windSpeed) is TropicalCyclonesProfileWindSpeed

                pressure = profile.pressure
                assert type(pressure) is TropicalCyclonesProfilePressure

                position = trop.position
                assert type(position) is TropicalCyclonesPosition

                locn = position.location
                assert type(locn) is TropicalCyclonesLocation

                details = position.details
                assert type(details) is TropicalCyclonesDetails

                movement = details.movement
                assert type(movement) is TropicalCyclonesDetailsMovement

                loc = position.loc
                assert type(loc) is AerisLocation

                track = trop.track
                assert type(track) is list

                details = position.details
                assert type(details) is TropicalCyclonesDetails

                movement = details.movement
                assert type(movement) is TropicalCyclonesDetailsMovement

                loc = position.loc
                assert type(loc) is AerisLocation

                forecast = trop.forecast
                assert type(forecast) is list
                location = forecast[0].location
                assert type(location) is TropicalCyclonesLocation

                details = position.details
                assert type(details) is TropicalCyclonesDetails

                movement = details.movement
                assert type(movement) is TropicalCyclonesDetailsMovement

                breakpoints = trop.breakPointAlerts
                assert type(breakpoints) is list

                coords = breakpoints[0].coords
                assert coords.type == "LineString"

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex

    def test_tropicalcyclones_function(self):
        """ Test the code against a live response from the API """

        try:
            awx = AerisWeather(app_id=app_id,
                               client_id=client_id,
                               client_secret=client_secret)

            trop_list = awx.tropical_cyclones(location=RequestLocation(postal_code="54660"),
                                              action=None,
                                              filter_={RequestFilter.TROPICAL_CYCLONE.TEST},
                                              sort=None,
                                              params={ParameterType.TROPICAL_CYCLONE.RADIUS: "2000miles"},
                                              query=None)

            for trop in trop_list:  # type: TropicalCyclonesResponse
                assert type(trop) is TropicalCyclonesResponse

                profile = trop.profile
                assert type(profile) is TropicalCyclonesProfile

                lifespan = profile.lifespan
                assert type(lifespan) is TropicalCyclonesProfileLifespan

                windSpeed = profile.windSpeed
                assert type(windSpeed) is TropicalCyclonesProfileWindSpeed

                pressure = profile.pressure
                assert type(pressure) is TropicalCyclonesProfilePressure

                position = trop.position
                assert type(position) is TropicalCyclonesPosition

                locn = position.location
                assert type(locn) is TropicalCyclonesLocation

                details = position.details
                assert type(details) is TropicalCyclonesDetails

                movement = details.movement
                assert type(movement) is TropicalCyclonesDetailsMovement

                loc = position.loc
                assert type(loc) is AerisLocation

                track = trop.track
                assert type(track) is list

                details = position.details
                assert type(details) is TropicalCyclonesDetails

                movement = details.movement
                assert type(movement) is TropicalCyclonesDetailsMovement

                loc = position.loc
                assert type(loc) is AerisLocation

                forecast = trop.forecast
                assert type(forecast) is list
                location = forecast[0].location
                assert type(location) is TropicalCyclonesLocation

                details = position.details
                assert type(details) is TropicalCyclonesDetails

                movement = details.movement
                assert type(movement) is TropicalCyclonesDetailsMovement

                breakpoints = trop.breakPointAlerts
                assert type(breakpoints) is list

                coords = breakpoints[0].coords
                assert coords.type == "LineString"

        except URLError as url_err:
            print("URL Error: " + url_err.reason)
            raise url_err

        except AerisError as aeris_err:
            print("AerisError: " + str(aeris_err))
            raise aeris_err

        except Exception as ex:
            print(ex.args)
            raise ex
