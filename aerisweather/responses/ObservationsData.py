
class ObservationsData:
    """
    Defines the object that stores the obs data returned within an Observation endpoint requests
    {
      "success": true,
      "error": null,
      "responses": {
        ...
        "ob": {
          "timestamp": 1520535180,
          "dateTimeISO": 2018-03-08T12:53:00-06:00",
          "tempC": -1.1
          ...
    """

    def __init__(self, ob):
        self.ob_data = ob

    @property
    def timestamp(self):
        return self.ob_data["timestamp"]

    @property
    def dateTimeISO(self):
        return self.ob_data["dateTimeISO"]

    @property
    def tempC(self):
        return self.ob_data["tempC"]

    @property
    def tempF(self):
        return self.ob_data["tempF"]

    @property
    def dewpointC(self):
        return self.ob_data["dewpointC"]

    @property
    def dewpointF(self):
        return self.ob_data["dewpointF"]

    @property
    def humidity(self):
        return self.ob_data["humidity"]

    @property
    def pressureMB(self):
        return self.ob_data["pressureMB"]

    @property
    def pressureIN(self):
        return self.ob_data["pressureIN"]

    @property
    def spressureMB(self):
        return self.ob_data["spressureMB"]

    @property
    def spressureIN(self):
        return self.ob_data["spressureIN"]

    @property
    def altimeterMB(self):
        return self.ob_data["altimeterMB"]

    @property
    def altimeterIN(self):
        return self.ob_data["altimeterIN"]

    @property
    def windKTS(self):
        return self.ob_data["windKTS"]

    @property
    def windKPH(self):
        return self.ob_data["windKPH"]

    @property
    def windMPH(self):
        return self.ob_data["windMPH"]

    @property
    def windSpeedKTS(self):
        return self.ob_data["windSpeedKTS"]

    @property
    def windSpeedKPH(self):
        return self.ob_data["windSpeedKPH"]

    @property
    def windSpeedMPH(self):
        return self.ob_data["windSpeedMPH"]

    @property
    def windDirDEG(self):
        return self.ob_data["windDirDEG"]

    @property
    def windDir(self):
        return self.ob_data["windDir"]

    @property
    def windGustKTS(self):
        return self.ob_data["windGustKTS"]

    @property
    def windGustKPH(self):
        return self.ob_data["windGustKPH"]

    @property
    def windGustMPH(self):
        return self.ob_data["windGustMPH"]

    @property
    def flightRule(self):
        return self.ob_data["flightRule"]

    @property
    def visibilityKM(self):
        return self.ob_data["visibilityKM"]

    @property
    def visibilityMI(self):
        return self.ob_data["visibilityMI"]

    @property
    def weather(self):
        return self.ob_data["weather"]

    @property
    def weatherShort(self):
        return self.ob_data["weatherShort"]

    @property
    def weatherCoded(self):
        return self.ob_data["weatherCoded"]

    @property
    def weatherPrimary(self):
        return self.ob_data["weatherPrimary"]

    @property
    def weatherPrimaryCoded(self):
        return self.ob_data["weatherPrimaryCoded"]

    @property
    def cloudsCoded(self):
        return self.ob_data["cloudsCoded"]

    @property
    def icon(self):
        return self.ob_data["icon"]

    @property
    def heatindexC(self):
        return self.ob_data["heatindexC"]

    @property
    def heatindexF(self):
        return self.ob_data["heatindexF"]

    @property
    def windchillC(self):
        return self.ob_data["windchillC"]

    @property
    def windchillF(self):
        return self.ob_data["windchillF"]

    @property
    def feelslikeC(self):
        return self.ob_data["feelslikeC"]

    @property
    def feelslikeF(self):
        return self.ob_data["feelslikeF"]

    @property
    def isDay(self):
        return self.ob_data["isDay"]

    @property
    def sunrise(self):
        return self.ob_data["sunrise"]

    @property
    def sunriseISO(self):
        return self.ob_data["sunriseISO"]

    @property
    def sunset(self):
        return self.ob_data["sunset"]

    @property
    def sunsetISO(self):
        return self.ob_data["sunsetISO"]

    @property
    def snowDepthCM(self):
        return self.ob_data["snowDepthCM"]

    @property
    def snowDepthIN(self):
        return self.ob_data["snowDepthIN"]

    @property
    def precipMM(self):
        return self.ob_data["precipMM"]

    @property
    def precipIN(self):
        return self.ob_data["precipIN"]

    @property
    def solradWM2(self):
        return self.ob_data["solradWM2"]

    @property
    def solradMethod(self):
        return self.ob_data["solradMethod"]

    @property
    def ceilingFT(self):
        return self.ob_data["ceilingFT"]

    @property
    def ceilingM(self):
        return self.ob_data["ceilingM"]

    @property
    def light(self):
        return self.ob_data["light"]

    @property
    def QC(self):
        return self.ob_data["QC"]

    @property
    def QCcode(self):
        return self.ob_data["QCcode"]

    @property
    def sky(self):
        return self.ob_data["sky"]
