from aerisweather.endpoints.Endpoint import EndpointType
from aerisweather.responses.AirQualityResponse import AirQualityResponse
from aerisweather.responses.Response import Response
from aerisweather.responses.AlertsResponse import AlertsResponse
from aerisweather.responses.CustomResponse import CustomResponse
from aerisweather.responses.ForecastsResponse import ForecastsResponse
from aerisweather.responses.Geometry import Geometry
from aerisweather.responses.ObservationsResponse import ObservationsResponse
from aerisweather.responses.ObservationsSummaryResponse import ObservationsSummaryResponse
from aerisweather.responses.PlacesResponse import PlacesResponse


class GeoJsonResponse(Response):
    """ Defines the base Response object for the data returned from the Aeris API. """

    data = {}

    def __init__(self, geo_json_data, endpoint_type: EndpointType):
        """
        Constructor

        Takes a geojson string that represents the features array of a geojson response from the AerisWeather API.

            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                    "type": "Polygon",
                    "coordinates": [ ]
                },
                "properties": {
                ...
        """

        super().__init__(json_data=geo_json_data)
        self.data = geo_json_data
        self.endpoint_type = endpoint_type

    @property
    def type(self) -> str:
        return self.data["type"]

    @property
    def id(self) -> None:
        if "id" in self.data:
            return self.data["id"]
        else:
            return None

    @property
    def geometry(self) -> Geometry:
        return Geometry(self.data["geometry"])

    @property
    def properties(self):
        if self.endpoint_type == EndpointType.AIR_QUALITY:
            return AirQualityResponse(self.data["properties"])
        elif self.endpoint_type == EndpointType.ALERTS:
            return AlertsResponse(self.data["properties"])
        elif self.endpoint_type == EndpointType.FORECASTS:
            return ForecastsResponse(self.data["properties"])
        elif self.endpoint_type == EndpointType.OBSERVATIONS:
            return ObservationsResponse(self.data["properties"])
        elif self.endpoint_type == EndpointType.OBSERVATIONS_SUMMARY:
            return ObservationsSummaryResponse(self.data["properties"])
        elif self.endpoint_type == EndpointType.PLACES:
            return PlacesResponse(self.data["properties"])
        else:
            return CustomResponse(self.data["properties"])
