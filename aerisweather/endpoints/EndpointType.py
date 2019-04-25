from enum import Enum


class EndpointType(Enum):
    """ Defines the available endpoints for Aeris API requests.

        When requesting data from an unimplemented endpoint, use the CUSTOM type and set the name of the endpoint
            using the "custom" property.

        Examples:
            # ObservationSummary
            endpoint = Endpoint(endpoint_type=EndpointType.OBSERVATIONS_SUMMARY)

            # Custom Endpoint
            EndpointType.custom = "stormreports"
            endpt = Endpoint(EndpointType.CUSTOM, location=RequestLocation(postal_code="54660"))
    """

    AIR_QUALITY = "airquality"
    ALERTS = "advisories"
    CONVECTIVE_OUTLOOK = "convective/outlook"
    FORECASTS = "forecasts"
    LIGHTNING = "lightning"
    OBSERVATIONS = "observations"
    OBSERVATIONS_SUMMARY = "observations/summary"
    PLACES = "places"
    CUSTOM = "custom"

    __custom_endpoint_type_name = ""

    @property
    def custom(self):
        """ Returns the string name of the custom/generic endpoint used when CUSTOM is the endpoint type """
        return self.__custom_endpoint_type_name

    @custom.setter
    def custom(self, endpoint_type: str):
        """ Sets the string name of the custom/generic endpoint used when CUSTOM is the endpoint type """
        self.__custom_endpoint_type_name = endpoint_type
