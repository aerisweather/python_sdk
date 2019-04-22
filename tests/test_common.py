
from datetime import datetime
from aerisweather.utils.AerisDateTime import AerisDateTime
import pytest



class TestCommon:
    """ Defines tests modules for common classes throughout the SDK """

    test_times = {
        "2018-03-12T10:53:00-05:00",
        "1818-03-12T09:53:00-06:00",
        "1973-07-09T1:01:01-01:00",
        "2011-11-11T10:53:00-05:00"
    }

    @pytest.mark.parametrize("times", test_times)
    def test(self, times):
        assert type(AerisDateTime.get_datetime_from_aeris_iso(times)) is datetime
