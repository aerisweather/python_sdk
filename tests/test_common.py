
from datetime import datetime
import unittest
from aerisweather.utils.AerisDateTime import AerisDateTime


class TestCommon(unittest.TestCase):
    """ Defines tests modules for common classes throughout the SDK """

    def test(self):
        assert type(AerisDateTime.get_datetime_from_aeris_iso("2018-03-12T10:53:00-05:00")) is datetime
