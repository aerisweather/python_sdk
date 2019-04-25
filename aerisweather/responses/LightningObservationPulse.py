
class LightningObservationPulse:
    """ Defines the object that stores the obs pulse data returned within a Lightning endpoint requests """

    def __init__(self, ob):
        self.ob_data = ob

    @property
    def type(self) -> str:
        return self.ob_data["type"]

    @property
    def peakamp(self) -> int:
        return self.ob_data["peakamp"]

    @property
    def numSensors(self) -> int:
        return self.ob_data["numSensors"]

    @property
    def icHeightM(self) -> int:
        return self.ob_data["icHeightM"]

    @property
    def icHeightFT(self) -> int:
        return self.ob_data["icHeightFT"]
