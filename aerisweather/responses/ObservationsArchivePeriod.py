from aerisweather.responses.ObservationsArchiveData import ObservationsArchiveData


class ObservationsArchivePeriod:

    period = {}

    def __init__(self, period_json):
        """ Constructor """

        self.period = period_json

    @property
    def ob(self) -> ObservationsArchiveData:
        return ObservationsArchiveData(self.period["ob"])

    @property
    def raw(self) -> str:
        return self.period["raw"]
