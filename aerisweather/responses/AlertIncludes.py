

class AlertIncludes:
    """
    Defines an object that stores an alert's county, fips zipcode and wxzone data returned within an Alerts/Advisories
    endpoint request.
        ...
           },
              "includes": {
                    "counties": [

                    ],
                    "fips": [
                      "27003",
                      "27009"
                    ],
                    "wxzones": [
                      "MNZ041",
                      "MNZ042"
                    ],
                    "zipcodes": [
                      54001,
                      54002
                    ]
        ...
    """

    def __init__(self, alert):
        self.alert_data = alert

    @property
    def counties(self) -> [str]:
        """  If a US alert will be a list of US counties in the XXC### format, where XX is the state abbreviation
        and ### is the 3 digit county fips number. If a Canadian alert will be null. """
        return self.alert_data["counties"]

    @property
    def fips(self) -> [str]:
        """  If a US alert will be a list of US counties in the XX### format, where XX is the state two digit fips
        number and ### is the 3 digit county fips number. If a Canadian alert will be null. """
        return self.alert_data["fips"]

    @property
    def wxzones(self) -> [int]:
        """  If a US alert will be a list of US public weather zones in the NOAA XXZ### format, where XX is the
        state abbreviation and ### is the 3 digit public zone id. If a Canadian alert will be a list of Canadian
        location codes (CLCs) """
        return self.alert_data["wxzones"]

    @property
    def zipcodes(self) -> [str]:
        """ List of US zip codes that are affected by the advisory. """
        return self.alert_data["zipcodes"]
