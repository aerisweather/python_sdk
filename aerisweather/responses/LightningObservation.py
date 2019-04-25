from aerisweather.responses.LightningObservationPulse import LightningObservationPulse


class LightningObservation:
    """ Defines the object that stores the obs data returned within a Lightning endpoint requests """

    def __init__(self, ob):
        self.ob_data = ob

    @property
    def timestamp(self) -> int:
        return self.ob_data["timestamp"]

    @property
    def dateTimeISO(self) -> str:
        return self.ob_data["dateTimeISO"]

    @property
    def age(self) -> int:
        return self.ob_data["age"]

    @property
    def pulse(self) -> LightningObservationPulse:
        return LightningObservationPulse(self.ob_data["pulse"])
