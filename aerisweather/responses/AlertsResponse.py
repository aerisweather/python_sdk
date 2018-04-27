
from aerisweather.responses.AerisLocation import AerisLocation
from aerisweather.responses.AerisPlace import AerisPlace
from aerisweather.responses.AerisProfile import AerisProfileAlerts
from aerisweather.responses.AlertDetails import AlertDetails
from aerisweather.responses.AlertIncludes import AlertIncludes
from aerisweather.responses.AlertTimestamps import AlertTimestamps
from aerisweather.responses.Response import Response


class AlertsResponse(Response):
    """
    Defines the object that stores an individual alert's data returned within an Alerts/Advisories endpoint request
    {
      "success": true,
      "error": null,
      "response": [
            {
              "id": "2ac0f0296cf81497a20c826d36f50305",
              "loc": {
                "long": -94.964992878,
                "lat": 29.3940757428
              },
              "details": {
                "type": "BH.S",
                "name": "STATEMENT",
          ...
    """

    def __init__(self, json_data):
        super().__init__(json_data=json_data)
        self.alert_data = json_data

    @property
    def id(self) -> str:
        return self.alert_data["id"]

    @property
    def loc(self) -> AerisLocation:
        return AerisLocation(self.alert_data["loc"])

    @property
    def details(self) -> AlertDetails:
        return AlertDetails(self.alert_data["details"])

    @property
    def timestamps(self) -> AlertTimestamps:
        return AlertTimestamps(self.alert_data["timestamps"])

    @property
    def poly(self) -> str:
        """ A comma-delimited string of latitude, longitude coordinates defining the small polygon boundary for
        this advisory; typically used for certain advisories, such as tornado and severe thunderstorm warnings.
        NULL if the advisory does not include a small polygon boundary. """
        return self.alert_data["poly"]

    @property
    def geoPoly(self):
        """ A GeoJSON polygon defining the small polygon boundary for this advisory; typically used for certain
        advisories, such as tornado and severe thunderstorm warnings. NULL if the advisory does not include a
        small polygon boundary. """
        return self.alert_data["geoPoly"]

    @property
    def includes(self) -> AlertIncludes:
        return AlertIncludes(self.alert_data["includes"])

    @property
    def place(self) -> AerisPlace:
        return AerisPlace(self.alert_data["place"])

    @property
    def profile(self) -> AerisProfileAlerts:
        return AerisProfileAlerts(self.alert_data["profile"])

    @property
    def active(self) -> bool:
        return self.alert_data["active"]
