

class AlertDetails:
    """
    Defines an object that stores an individual alert's details data returned within an Alerts/Advisories
    endpoint request.
        ...
            "long": -94.964992878,
            "lat": 29.3940757428
          },
          "details": {
            "type": "BH.S",
            "name": "STATEMENT",
        ...
    """

    def __init__(self, alert):
        self.alert_data = alert

    @property
    def type(self) -> str:
        """ The valid-time event code (VTEC) for the advisory. Review the list of allowed Advisory Types. """
        return self.alert_data["type"]

    @property
    def name(self) -> str:
        """ The type name for the advisory. """
        return self.alert_data["name"]

    @property
    def loc(self) -> str:
        """ The weather zone for the advisory """
        return self.alert_data["loc"]

    @property
    def emergency(self) -> bool:
        """ Set to true if this is an emergency-specific advisory, such as a tornado emergency. """
        return self.alert_data["emergency"]

    @property
    def color(self) -> str:
        """ The 6 character hex color code for the advisory. Corresponds to the AMP Advisory types/colors. """
        return self.alert_data["color"]

    @property
    def cat(self) -> str:
        """ The default category of the alert type. May be null for non common alerts. """
        return self.alert_data["cat"]

    @property
    def body(self) -> str:
        """ The shortened and formatted version of the advisory body text. """
        return self.alert_data["body"]

    @property
    def bodyFull(self) -> str:
        """ The shortened and formatted version of the advisory body text. """
        return self.alert_data["bodyFull"]
