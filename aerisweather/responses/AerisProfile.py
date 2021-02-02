from typing import List

from aerisweather.responses import RiversCrests, RiversImpacts, RiversCategories


class AerisProfile:
    """Defines the base class for Aeris API profile data returned in an Aeris API responses"""

    def __init__(self, json_data):
        """ Constructor """
        self.data = json_data

    @property
    def tz(self):
        """Returns the timezone string like "America/Chicago"""
        return self.data["tz"]


class AerisProfileAlerts(AerisProfile):
    """Defines an object for the Aeris API profile data returned in an Aeris API Alerts/Advisories responses"""

    def __init__(self, json_data):
        """ Constructor """
        self.data = json_data
        super().__init__(self.data)


class AerisProfileCountries(AerisProfile):
    """
    Defines an object for the Aeris API profile data returned in an Aeris API Country responses.
    Used with the countries endpoint (https://www.aerisweather.com/support/docs/api/reference/endpoints/countries/).
    """

    def __init__(self, json_data):
        """ Constructor """
        self.data = json_data
        super().__init__(self.data)

    @property
    def population(self):
        """ Returns the population """
        return self.data["pop"]

    @property
    def capital(self):
        """Returns the capital city of the country."""
        return self.data["capital"]

    @property
    def areaMI(self):
        """Returns the approximate area in square miles"""
        return self.data["areaMI"]

    @property
    def areaKM(self):
        """Returns the approximate area in square kilometers"""
        return self.data["areaKM"]

    @property
    def neighbors(self) -> List[str]:
        """Returns an array of 2 letter abbreviations of neighboring countries"""
        neighbors = []

        for neighbor in self.data["neighbors"]:
            neighbors.append(neighbor)

            return neighbors


class AerisProfileConditions(AerisProfile):
    """Defines an object for the Aeris API profile data returned in an Aeris API Conditions responses"""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)


class AerisProfileFires(AerisProfile):
    """Defines an object for the Aeris API profile data returned in an Aeris API Fires responses"""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)


class AerisProfileForecasts(AerisProfile):
    """Defines an object for the Aeris API profile data returned in an Aeris API Forecasts responses"""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)


class AerisProfileIndices(AerisProfile):
    """Defines an object for the Aeris API profile data returned in an Aeris API Indices responses"""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)


class AerisProfileNormals(AerisProfile):
    """Defines an object for the Aeris API profile data returned in an Aeris API Normals responses"""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)


class AerisProfileObservations(AerisProfile):
    """Defines an object for the Aeris API profile data returned in an Aeris API Observation responses"""

    def __init__(self, json_data):
        """ Constructor """
        self.data = json_data
        super().__init__(self.data)

    @property
    def elevM(self):
        """Returns the elevation in Meters"""
        return self.data["elevM"]

    @property
    def elevFT(self):
        """Returns the elevation in Feet"""
        return self.data["elevFT"]


class AerisProfileObservationsArchive(AerisProfile):
    """Defines an object for the Aeris API profile data returned in an Aeris API ObservationsArchive responses."""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)


class AerisProfileObservationsSummary(AerisProfileObservations):
    """Defines an object for the Aeris API profile data returned in an Aeris API ObservationsSummary responses."""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)

    @property
    def hasPrecip(self):
        """A boolean stating if the observation summary has precipitation."""
        return self.data["hasPrecip"]


class AerisProfilePhrasesSummary(AerisProfile):
    """Defines an object for the Aeris API profile data returned in an Aeris API PhrasesSummary responses."""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)


class AerisProfilePlaces(AerisProfile):
    """Defines an object for the Aeris API profile data returned in an Aeris API Places responses."""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)

    @property
    def elevM(self):
        """Returns the elevation in Meters"""
        return self.data["elevM"]

    @property
    def elevFT(self):
        """Returns the elevation in Feet"""
        return self.data["elevFT"]

    @property
    def pop(self):
        """Returns the population of the place"""
        return self.data["pop"]

    @property
    def isDST(self):
        """ Returns whether or not the location is currently following daylight savings time"""
        if self.data["isDST"]:
            return True
        else:
            return False

    @property
    def tzName(self):
        """Returns the timezone name"""
        return self.data["tzname"]

    @property
    def tzOffset(self):
        """Returns the timezone offset"""
        return self.data["tzoffset"]

    @property
    def wxzone(self):
        """Returns an array of strings defining the weather zones associated with the place"""
        return self.data["wxzone"]

    @property
    def firezone(self):
        """Returns an array of strings defining the firezones associated with the place"""
        return self.data["firezone"]

    @property
    def fips(self):
        """Returns an array of strings defining the fips associated with the place"""
        return self.data["fips"]

    @property
    def countyid(self):
        """Returns an array of strings defining the county ids associated with the place"""
        return self.data["countyid"]


class AerisProfilePlacesAirports(AerisProfilePlaces):
    """Defines an object for the Aeris API profile data returned in an Aeris API Places Airports responses."""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)

    @property
    def id(self):
        """Returns the global airport profile id"""
        return self.data["id"]

    @property
    def local(self):
        """Returns the local facility id/code for the location"""
        return self.data["id"]

    @property
    def type(self):
        """Returns the airport facility type code"""
        return self.data["type"]

    @property
    def typeENG(self):
        """Returns the airport facility type name in English"""
        return self.data["typeENG"]

    @property
    def iata(self):
        """Returns the International Air Transport Association id"""
        return self.data["iata"]


class AerisProfilePlacesPostalCodes(AerisProfilePlaces):
    """Defines an object for the Aeris API profile data returned in an Aeris API Places Postal Codes responses."""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)

    @property
    def active(self):
        """True if the postal/zip code is still active and allowed by the postal service.
        False if the postal/zip code is no longer in use, though the Aeris API will continue to support it."""
        return self.data["active"]


class AerisProfileRecords(AerisProfile):
    """Defines an object for the Aeris API profile data returned in an Aeris API Records responses."""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)


class AerisProfileRivers(AerisProfile):
    """Defines an object for the Aeris API profile data returned in an Aeris API Rivers responses."""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)

    @property
    def waterbody(self):
        """"Returns the body of water where the gauge is located"""
        return self.data["waterbody"]

    @property
    def cats(self):
        """Returns a RiversCategories object containing the various categories for flood levels at the gauge location"""
        cats = RiversCategories.RiversCategories(self.data["cats"])
        return cats

    @property
    def hasImpacts(self):
        """Returns True if the gauge include flooding impacts, false if unavailable"""
        if self.data["hasImpacts"]:
            return True
        else:
            return False


class AerisProfileRiversGauges(AerisProfileRivers):
    """Defines an object for the Aeris API profile data returned in an Aeris API Rivers Gauges responses."""

    def __init__(self, json_data):
        """ Constructor """

        self.data = json_data
        super().__init__(self.data)

    @property
    def impacts(self):
        """Returns an array of RiverImpacts objects."""
        impacts = []

        for im in self.data["impacts"]:
            impacts.append(RiversImpacts.RiversImpacts(im))

        return impacts

    @property
    def lowWaterRecords(self):
        """"Returns the body of water where the gauge is located"""
        return self.data["lowWaterRecord"]

    @property
    def crests(self):
        """Returns an array of RiverImpacts objects."""
        crests = []

        for cr in self.data["crests"]:
            crests.append(RiversCrests.RiversCrests(cr))

        return crests
