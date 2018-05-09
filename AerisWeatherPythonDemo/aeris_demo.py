""" Provided to show example use cases for the AerisWeather Python library. """

from aerisweather.aerisweather import AerisWeather
from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.requests.RequestAction import RequestAction
from aerisweather.requests.RequestFilter import RequestFilter
from keys import client_id, client_secret, app_id

# Set the AerisWeather client id and secret.
aeris = AerisWeather(client_id=client_id, client_secret=client_secret, app_id=app_id)

# Create a RequestLocation object to be used with any endpoint requests.
loc = RequestLocation(city="tomah", state="wi")


""" Observations Request Example 1 """
# Create a simple observations request with no options. We will receive a list of ObservationsResponse objects
obs_list = aeris.observations(location=loc)

for obs in obs_list:
    # get the AerisPlace responses object
    place = obs.place

    # get the observations data object
    ob = obs.ob

    # get some observations data
    tempF = ob.tempF
    weather = ob.weather

    print()
    print("Observations Example 1:")
    print("The current weather for " + place.name + ", " + place.state + ":")
    print("Conditions are currently " + weather + " with a temp of " + str(tempF) + "°F")


""" Observations Request Example 2 """
# Make the API request and get a list of ObservationResponse objects from the response
# (Note: we don't need a RequestLocation object, since we're using Closest with the "p" parameter.)
obs_list = aeris.observations(action=RequestAction.OBSERVATIONS.CLOSEST,
                              filter_=[RequestFilter.OBSERVATIONS.ALL_STATIONS],
                              params={ParameterType.OBSERVATIONS.P: "tomah,wi",
                                      ParameterType.OBSERVATIONS.FIELDS: "place, ob.tempF,ob.weather"})
for obs in obs_list:
    place = obs.place
    ob = obs.ob
    tempF = ob.tempF
    weather = ob.weather

    print()
    print("Observations Example 2:")
    print("The current weather for " + place.name + ", " + place.state + ":")
    print("Conditions are currently " + weather + " with a temp of " + str(tempF) + "°F")


""" Forecasts Request Example 1 """
forecast_list = aeris.forecasts(location=loc,
                                params={
                                    ParameterType.FORECASTS.FIELDS:
                                        "period.maxTempF,period.minTempF,period.weather,period.isDay"})

for forecast in forecast_list:  # type: ForecastResponse
    if forecast.isDay:
        day = forecast.periods[0]
        night = forecast.periods[1]
    else:
        day = forecast.periods[1]
        night = forecast.periods[0]

    print()
    print("Forecast Example:")
    print("Today expect " + day.weather + " with a high temp of " + str(day.maxTempF) + "°")
    print("Tonight will be " + night.weather + " with a low temp of " + str(night.minTempF) + "°")


""" Alerts Request Example 1 """
alerts_list = aeris.alerts(location=RequestLocation(postal_code="54660"),
                           filter_=[RequestFilter.ALERTS.ALL],
                           params={ParameterType.ALERTS.FIELDS: "timestamps,details",
                                   ParameterType.FORECASTS.LIMIT: "2"})

for alert in alerts_list:
    print()
    print("Alerts Example:")
    print("Issued: " + str(alert.timestamps.issued))
    print("Details: " + alert.details.body)

""" Observations Summary Request Example 1 """
obs_sum_list = aeris.observations_summary(location=RequestLocation(postal_code="54660"),
                                          filter_=[RequestFilter.OBSERVATIONS_SUMMARY.ALL_STATIONS],
                                          params=None)

for os in obs_sum_list:
    print()
    print("Observations Summary Example:")
    print("Location: " + os.place.name + ", " + os.place.state)
    print("YMD: " + str(os.periods[0].ymd))
    print("Average Temp: " + str(os.periods[0].temp.avgF) + "°")
