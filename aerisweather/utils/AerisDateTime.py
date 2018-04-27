
from datetime import datetime


class AerisDateTime(object):
    """Defines methods for working with Aeris API time data"""

    @staticmethod
    def get_datetime_from_aeris_iso(str_aeris_datetime) -> datetime:
        """
        Takes an ISO string from the Aeris API and returns a valid Python DateTime object
        @parameter aerisDateTime - an Aeris API ISO DateTime string
        """
        # remove the colon in the timezone and dump into a datetime object
        ob_datetime_array = str_aeris_datetime.rpartition(':')
        ob_datetime_string = ob_datetime_array[0] + ob_datetime_array[2]
        ob_datetime = datetime.strptime(ob_datetime_string, '%Y-%m-%dT%H:%M:%S%z')

        return ob_datetime




