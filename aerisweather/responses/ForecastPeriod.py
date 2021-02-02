
from typing import List
from aerisweather.responses.WeatherCoded import WeatherCoded


class ForecastPeriod:
    """ Defines an object for the forecast period data. """

    period = {}

    def __init__(self, period_json):
        """
        Constructor - this takes an individual forecast period's json.
                        {
                        "timestamp": 1521543600,
                        "validTi...
        """

        self.period = period_json

    @property
    def timestamp(self) -> int:
        """ UNIX timestamp of the forecast valid time """
        return self.period["timestamp"]

    @property
    def validTime(self) -> str:
        """ Localized valid time of the forecast. (Deprecated. Use dateTimeISO) """
        return self.period["validTime"]

    @property
    def dateTimeISO(self) -> str:
        """ ISO 8601 of the valid time of the forecast. """
        return self.period["dateTimeISO"]

    @property
    def maxTempC(self) -> int:
        """ Max expected temperature in Celsius. - Provided with filter=day (Default) and for the day time periods
        with filter=daynight """
        return self.period["maxTempC"]

    @property
    def maxTempF(self) -> int:
        """ Max expected temperature in F. - Provided with filter=day (Default) and for the day time periods
        with filter=daynight """
        return self.period["maxTempF"]

    @property
    def minTempC(self) -> int:
        """ Min expected temperature in Celsius. - Provided with filter=day (Default) and for the day time periods
        with filter=daynight """
        return self.period["minTempC"]

    @property
    def minTempF(self) -> int:
        """ Min expected temperature in F. - Provided with filter=day (Default) and for the day time periods
        with filter=daynight """
        return self.period["minTempF"]

    @property
    def avgTempC(self) -> int:
        """ Average temperature in Celsius. """
        return self.period["avgTempC"]

    @property
    def avgTempF(self) -> int:
        """  Average temperature in Fahrenheit. """
        return self.period["avgTempF"]

    @property
    def tempC(self) -> int:
        """ Temperature in Celsius. Value will be null when using filter=day or filter=daynight """
        return self.period["tempC"]

    @property
    def tempF(self) -> int:
        """  Temperature in Fahrenheit. Value will be null when using filter=day or filter=daynight. """
        return self.period["tempF"]

    @property
    def pop(self) -> int:
        """ Probability of precipitation. A percentage from 0 - 100%. None if unavailable. """
        return self.period["pop"]

    @property
    def precipMM(self) -> int:
        """ Precipitation expected in millimeters. The total liquid equivalent of all precipitation. """
        return self.period["precipMM"]

    @property
    def precipIN(self) -> int:
        """ Precipitation expected in inches. The total liquid equivalent of all precipitation. """
        return self.period["precipIN"]

    @property
    def iceaccum(self) -> float:
        """ The amount of ice accumulated in mm. """
        return self.period["iceaccum"]

    @property
    def iceaccumMM(self) -> float:
        """ The amount of ice accumulated in mm. """
        return self.period["iceaccumMM"]

    @property
    def iceaccumIN(self) -> float:
        """ The amount of ice accumulated in inches. """
        return self.period["iceaccumIN"]

    @property
    def maxHumidity(self) -> int:
        """ Maximum humidity percentage """
        return self.period["maxHumidity"]

    @property
    def minHumidity(self) -> int:
        """ Minimum humidity percentage. """
        return self.period["minHumidity"]

    @property
    def humidity(self) -> int:
        """ Minimum humidity percentage. """
        return self.period["humidity"]

    @property
    def uvi(self) -> int:
        """ The ultraviolet index. Integer from 0 - 12, null if unavailable. Available for the first five days
        of the forecasts """
        return self.period["uvi"]

    @property
    def pressureMB(self) -> float:
        """ Barometric pressure in millibars. """
        return self.period["pressureMB"]

    @property
    def pressureIN(self) -> float:
        """ Barometric pressure in inches mercury. """
        return self.period["pressureIN"]

    @property
    def sky(self) -> int:
        """ Sky cover percentage, 0 = clear, 100 = cloudy. """
        return self.period["sky"]

    @property
    def snowCM(self) -> float:
        """ Snowfall amount in centimeters. """
        return self.period["snowCM"]

    @property
    def snowIN(self) -> float:
        """ Snowfall amount in inches. """
        return self.period["snowIN"]

    @property
    def feelslikeC(self) -> int:
        """ The apparent temperature in Celsius. - Not used/valid when using filter=day or filter=daynight """
        return self.period["feelslikeC"]

    @property
    def feelslikeF(self) -> int:
        """ The apparent temperature in Fahrenheit. - Not used/valid when using filter=day or filter=daynight. """
        return self.period["feelslikeF"]

    @property
    def minFeelslikeC(self) -> int:
        """ The minimum apparent temperature in Celsius. """
        return self.period["minFeelslikeC"]

    @property
    def minFeelslikeF(self) -> int:
        """ The minimum apparent temperature in Fahrenheit. """
        return self.period["minFeelslikeF"]

    @property
    def maxFeelslikeC(self) -> int:
        """ The maximum apparent temperature in Celsius. """
        return self.period["maxFeelslikeC"]

    @property
    def maxFeelslikeF(self) -> int:
        """ The maximum apparent temperature in Fahrenheit. """
        return self.period["maxFeelslikeF"]

    @property
    def avgFeelslikeC(self) -> int:
        """ The average apparent temperature in Celsius. """
        return self.period["avgFeelslikeC"]

    @property
    def avgFeelslikeF(self) -> int:
        """ The average apparent temperature in Fahrenheit. """
        return self.period["avgFeelslikeF"]

    @property
    def dewpointC(self) -> int:
        """ The dew point temperature in Celsius. - Not used/valid when using filter=day or filter=daynight """
        return self.period["dewpointC"]

    @property
    def dewpointF(self) -> int:
        """ The dew point temperature in Fahrenheit. - Not used/valid when using filter=day or filter=daynight """
        return self.period["dewpointF"]

    @property
    def maxDewpointC(self) -> int:
        """ The maximum dew point temperature in Celsius. """
        return self.period["maxDewpointC"]

    @property
    def maxDewpointF(self) -> int:
        """ The maximum dew point temperature in Fahrenheit. """
        return self.period["maxDewpointF"]

    @property
    def minDewpointC(self) -> int:
        """ The minimum dew point temperature in Celsius. """
        return self.period["minDewpointC"]

    @property
    def minDewpointF(self) -> int:
        """ The minimum dew point temperature in Fahrenheit. """
        return self.period["minDewpointF"]

    @property
    def avgDewpointC(self) -> int:
        """ The average dew point temperature in Celsius. """
        return self.period["avgDewpointC"]

    @property
    def avgDewpointF(self) -> int:
        """ The average dew point temperature in Fahrenheit. """
        return self.period["avgDewpointF"]

    @property
    def windDirDEG(self) -> int:
        """ The wind direction in degrees. - Not used/valid when using filter=day or filter=daynight """
        return self.period["windDirDEG"]

    @property
    def windDir(self) -> str:
        """ Wind direction in cardinal coordinates. - Not used/valid when using filter=day or filter=daynight """
        return self.period["windDir"]

    @property
    def windDirMaxDEG(self) -> int:
        """ The wind direction in degrees (0=North) at the time of maximum wind speed (windSpeedMaxMPH). """
        return self.period["windDirMaxDEG"]

    @property
    def windDirMax(self) -> str:
        """  Wind direction in cardinal coordinates at the time of maximum wind speed (windSpeedMaxMPH). """
        return self.period["windDirMax"]

    @property
    def windDirMinDEG(self) -> int:
        """  The wind direction in degrees (0=North) at the time of minimum wind speed (windSpeedMinMPH). """
        return self.period["windDirMinDEG"]

    @property
    def windDirMin(self) -> str:
        """  Wind direction in cardinal coordinates at the time of minimum wind speed (windSpeedMinMPH). """
        return self.period["windDirMin"]

    @property
    def windGustKTS(self) -> int:
        """ Wind gust in knots. """
        return self.period["windGustKTS"]

    @property
    def windGustKPH(self) -> int:
        """ Wind gust in kilometers per hour. """
        return self.period["windGustKPH"]

    @property
    def windGustMPH(self) -> int:
        """ Wind gust in miles per hour. """
        return self.period["windGustMPH"]

    @property
    def windSpeedKTS(self) -> int:
        """ Wind speed in knots. """
        return self.period["windSpeedKTS"]

    @property
    def windSpeedKPH(self) -> int:
        """ Wind speed in kilometers per hour. """
        return self.period["windSpeedKPH"]

    @property
    def windSpeedMPH(self) -> int:
        """ Wind speed in miles per hour. """
        return self.period["windSpeedMPH"]

    @property
    def windSpeedMaxKTS(self) -> int:
        """ The max wind speed in knots. """
        return self.period["windSpeedMaxKTS"]

    @property
    def windSpeedMaxKPH(self) -> int:
        """ The max wind speed in kilometers per hour. """
        return self.period["windSpeedMaxKPH"]

    @property
    def windSpeedMaxMPH(self) -> int:
        """ The max wind speed in miles per hour. """
        return self.period["windSpeedMaxMPH"]

    @property
    def windSpeedMinKTS(self) -> int:
        """ The minimum wind speed in knots. """
        return self.period["windSpeedMinKTS"]

    @property
    def windSpeedMinKPH(self) -> int:
        """ The minimum wind speed in kilometers per hour. """
        return self.period["windSpeedMinKPH"]

    @property
    def windSpeedMinMPH(self) -> int:
        """ The minimum wind speed in miles per hour. """
        return self.period["windSpeedMinMPH"]

    @property
    def windDir80mDEG(self) -> int:
        """ The wind direction in degrees at a height of 80 meters. """
        return self.period["windDir80mDEG"]

    @property
    def windDir80m(self) -> str:
        """ Wind direction in cardinal coordinates at a height of 80 meters. """
        return self.period["windDir80m"]

    @property
    def windDirMax80mDEG(self) -> int:
        """ The wind direction in degrees (0=North) at the time of maximum wind speed at a height of 80 meters. """
        return self.period["windDirMax80mDEG"]

    @property
    def windDirMax80m(self) -> str:
        """ Wind direction in cardinal coordinates at the time of maximum wind speed at a height of 80 meters. """
        return self.period["windDirMax80m"]

    @property
    def windDirMin80mDEG(self) -> int:
        """ The wind direction in degrees (0=North) at the time of minimum wind speed at a height of 80 meters. """
        return self.period["windDirMin80mDEG"]

    @property
    def windDirMin80m(self) -> str:
        """ Wind direction in cardinal coordinates at the time of minimum wind speed at a height of 80 meters. """
        return self.period["windDirMin80m"]

    @property
    def windGust80mKTS(self) -> int:
        """ Wind gust in knots at a height of 80 meters. """
        return self.period["windGust80mKTS"]

    @property
    def windGust80mKPH(self) -> int:
        """ Wind gust in kilometers per hour at a height of 80 meters. """
        return self.period["windGust80mKPH"]

    @property
    def windGust80mMPH(self) -> int:
        """ Wind gust in miles per hour at a height of 80 meters. """
        return self.period["windGust80mMPH"]

    @property
    def windSpeed80mKTS(self) -> int:
        """ The wind speed in knots at a height of 80 meters. """
        return self.period["windSpeed80mKTS"]

    @property
    def windSpeed80mKPH(self) -> int:
        """ The wind speed in kilometers per hour at a height of 80 meters. """
        return self.period["windSpeed80mKPH"]

    @property
    def windSpeed80mMPH(self) -> int:
        """ The wind speed in miles per hour at a height of 80 meters. """
        return self.period["windSpeed80mMPH"]

    @property
    def windSpeedMax80mKTS(self) -> int:
        """ The maximum wind speed in knots at a height of 80 meters. """
        return self.period["windSpeedMax80mKTS"]

    @property
    def windSpeedMax80mKPH(self) -> int:
        """ The maximum wind speed in kilometers per hour at a height of 80 meters. """
        return self.period["windSpeedMax80mKPH"]

    @property
    def windSpeedMax80mMPH(self) -> int:
        """ The maximum wind speed in miles per hour at a height of 80 meters. """
        return self.period["windSpeedMax80mMPH"]

    @property
    def windSpeedMin80mKTS(self) -> int:
        """ The minimum wind speed in knots at a height of 80 meters. """
        return self.period["windSpeedMin80mKTS"]

    @property
    def windSpeedMin80mKPH(self) -> int:
        """ The minimum wind speed in kilometers per hour at a height of 80 meters. """
        return self.period["windSpeedMin80mKPH"]

    @property
    def windSpeedMin80mMPH(self) -> int:
        """ The minimum wind speed in miles per hour at a height of 80 meters. """
        return self.period["windSpeedMin80mMPH"]

    @property
    def weather(self) -> str:
        """ Full weather phrase that combines the weather from all periods as needed. """
        return self.period["weather"]

    @property
    def weatherCoded(self) -> List[WeatherCoded]:
        """  Array of periods containing different weather types; can be used to determine when a particular type
        of weather is expected to begin/end. Refer to the Coded Weather documentation for additional information
        on the types of weather codes.
                "weatherCoded": [
                    {
                      "timestamp": 1521568800,
                      "wx": "S:L:RW",
                      "dateTimeISO": "2018-03-20T14:00:00-04:00"
                    },
                    {
                      "timestamp": 1521576000,
                      "wx": "C:L:RW",
                      "dateTimeISO": "2018-03-20T16:00:00-04:00"
                    }
                  ],
        """
        wxcoded_list = []
        for code in self.period["weatherCoded"]:
            weathercoded = WeatherCoded(code)
            wxcoded_list.append(weathercoded)
        return wxcoded_list

    @property
    def weatherPrimary(self) -> str:
        """ Primary weather across all periods. """
        return self.period["weatherPrimary"]

    @property
    def weatherPrimaryCoded(self) -> str:
        """ Primary weather coded. Refer to the Coded Weather documentation for additional information on the types
        of weather codes. """
        return self.period["weatherPrimaryCoded"]

    @property
    def cloudsCoded(self) -> str:
        """ Code for the cloud type. Refer to the Coded Weather documentation for additional information on the types
        of cloud codes. """
        return self.period["cloudsCoded"]

    @property
    def icon(self) -> str:
        """ Weather icon representing the expected weather from the default Aeris icon set. For more custom
        implementations, icons can be determined by the weatherCoded and weatherCodedPrimary properties. """
        return self.period["icon"]

    @property
    def isDay(self) -> bool:
        """ True if the period is during the day, otherwise false. """
        if self.period["isDay"] == "false":
            return False
        else:
            return True

    @property
    def solradWM2(self) -> float:
        """ Solar radiation over the forecast period, described in watts per square meter. """
        return self.period["solradWM2"]

    @property
    def solradMinWM2(self) -> float:
        """ Minimum expected solar radiation over the forecast period, described in watts per square meter. """
        return self.period["solradMinWM2"]

    @property
    def solradMaxWM2(self) -> float:
        """ Maximum expected solar radiation over the forecast period, described in watts per square meter. """
        return self.period["solradMaxWM2"]

    @property
    def sunrise(self):
        """ Sunrise time as a UNIX timestamp. Provided when using filter=day (default) or filter=daynight.
        Not currently available for hourly forecasts. NOTE: If no sunrise (Midnight sun / polar night) a
        boolean false will be returned """
        if self.period["sunrise"] == "false":
            return None
        else:
            return self.period["sunrise"]

    @property
    def sunriseISO(self):
        """ ISO 8601 date of the sunrise for the observation location. Provided when using filter=day (default)
        or filter=daynight. Not currently available for hourly forecasts. NOTE: If no sunrise (Midnight sun / polar
        night) a boolean false will be returned """
        if self.period["sunriseISO"] == "false":
            return None
        else:
            return self.period["sunriseISO"]

    @property
    def sunset(self):
        """ sunset time as a UNIX timestamp. Provided when using filter=day (default) or filter=daynight.
        Not currently available for hourly forecasts. NOTE: If no sunset (Midnight sun / polar night) a
        boolean false will be returned """
        if self.period["sunset"] == "false":
            return None
        else:
            return self.period["sunset"]

    @property
    def sunsetISO(self):
        """ ISO 8601 date of the sunset for the observation location. Provided when using filter=day (default)
        or filter=daynight. Not currently available for hourly forecasts. NOTE: If no sunset (Midnight sun / polar
        night) a boolean false will be returned """
        if self.period["sunsetISO"] == "false":
            return None
        else:
            return self.period["sunsetISO"]
