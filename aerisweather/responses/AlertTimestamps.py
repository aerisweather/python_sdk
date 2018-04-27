

class AlertTimestamps:
    """
    Defines an object that stores an individual alert's timestamp data returned within an Alerts/Advisories
    endpoint request.
        ...
           },
              "timestamps": {
                "issued": 1522696200,
                "issuedISO": "2018-04-02T14:10:00-05:00",
                "begins": 1522696200,
                "beginsISO": "2018-04-02T14:10:00-05:00",
                "expires": 1522821600,
                "expiresISO": "2018-04-04T01:00:00-05:00",
                "added": 1522696239,
                "addedISO": "2018-04-02T14:10:39-05:00"
              },
        ...
    """

    def __init__(self, alert):
        self.alert_data = alert

    @property
    def issued(self) -> int:
        """ UNIX timestamp when the advisory was issued by the NWS. """
        return self.alert_data["issued"]

    @property
    def issuedISO(self) -> str:
        """ ISO 8601 date of the time when the advisory was issued. """
        return self.alert_data["issuedISO"]

    @property
    def begins(self) -> int:
        """ UNIX timestamp when the advisory goes into effect. """
        return self.alert_data["begins"]

    @property
    def beginsISO(self) -> str:
        """ ISO 8601 date of the time when the advisory goes into effect. """
        return self.alert_data["beginsISO"]

    @property
    def expires(self) -> int:
        """ UNIX timestamp when the advisory expires. """
        return self.alert_data["expires"]

    @property
    def expiresISO(self) -> str:
        """ ISO 8601 date of the time when the advisory expires. """
        return self.alert_data["expiresISO"]

    @property
    def added(self) -> int:
        """ UNIX timestamp when the advisory was stored. """
        return self.alert_data["added"]

    @property
    def addedISO(self) -> str:
        """ ISO 8601 date of the time when the advisory was stored. """
        return self.alert_data["addedISO"]
