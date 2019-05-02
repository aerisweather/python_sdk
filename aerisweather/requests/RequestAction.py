""" Defines the available Request Actions for each Aeris API endpoint.

    For details on the use of each action value, see the Actions section of the corresponding endpoint, such
    as the Forecasts endpoint's actions found here:
    https://www.aerisweather.com/support/docs/api/reference/endpoints/forecasts/#actions.
"""
from collections import namedtuple


class RequestAction:

    request_action = namedtuple('REQUEST_ACTION', ['AIR_QUALITY',
                                                   'ALERTS',
                                                   'CONVECTIVE_OUTLOOK',
                                                   'FORECASTS',
                                                   'LIGHTNING',
                                                   'OBSERVATIONS',
                                                   'OBSERVATIONS_SUMMARY',
                                                   'PLACES',
                                                   'CUSTOM'])

    aqi = namedtuple('AIR_QUALITY', ['ID', 'CLOSEST', 'SEARCH', 'WITHIN', 'ROUTE'])
    AIR_QUALITY = aqi('id', 'closest', 'search', 'within', 'route')

    alts = namedtuple('ALERTS', ['ONE', 'TWO'])
    ALERTS = alts('one', 'two')

    conv = namedtuple('CONVECTIVE_OUTLOOK', ['AFFECTS', 'CONTAINS', 'ID', 'SEARCH'])
    CONVECTIVE_OUTLOOK = conv('affects', 'contains', 'id', 'search')

    fcasts = namedtuple('FORECASTS', ['ID', 'CLOSEST', 'ROUTE'])
    FORECASTS = fcasts('id', 'closest', 'route')

    lght = namedtuple('LIGHTNING', ['ID', 'CLOSEST', 'ROUTE', 'SEARCH'])
    LIGHTNING = lght('id', 'closest', 'route', 'search')

    lght_sum = namedtuple('LIGHTNING_SUMMARY', ['ID', 'CLOSEST', 'SEARCH', 'WITHIN'])
    LIGHTNING_SUMMARY = lght_sum('id', 'closest', 'search', 'within')

    obs = namedtuple('OBSERVATIONS', ['CLOSEST', 'ID', 'ROUTE', 'SEARCH', 'WITHIN'])
    OBSERVATIONS = obs('closest', 'id', 'route', 'search', 'within')

    obs_archive = namedtuple('OBSERVATIONS_ARCHIVE', ['ID', 'CLOSEST', 'SEARCH', 'WITHIN'])
    OBSERVATIONS_ARCHIVE = obs_archive('id', 'closest', 'search', 'within')

    obs_summary = namedtuple('OBSERVATIONS_SUMMARY', ['ID', 'CLOSEST', 'SEARCH', 'WITHIN'])
    OBSERVATIONS_SUMMARY = obs_summary('id', 'closest', 'search', 'within')

    pl = namedtuple('PLACES', ['ID', 'CLOSEST', 'SEARCH', 'WITHIN'])
    PLACES = pl('id', 'closest', 'search', 'within')

    precipsum = namedtuple('PRECIP_SUMMARY', ['ID'])
    PRECIP_SUMMARY = precipsum('id')

    threat = namedtuple('THREATS', ['ID'])
    THREATS = threat('id')

    tropcyc = namedtuple('TROPICAL_CYCLONE', ['ALL', 'CLOSEST', 'SEARCH', 'WITHIN', 'AFFECTS'])
    TROPICAL_CYCLONE = tropcyc('all', 'closest', 'search', 'within', 'affects')

    __custom_action_type_name = ""
    cust = namedtuple('CUSTOM', ['VALUE'])
    CUSTOM = cust(__custom_action_type_name)

    @property
    def custom(self):
        """ Returns the string name of the custom/generic Action used when CUSTOM is the Action type """
        return self.__custom_action_type_name

    @custom.setter
    def custom(self, action_type: str):
        """ Sets the string name of the custom/generic Action used when CUSTOM is the Action type """
        cust = namedtuple('CUSTOM', ['VALUE'])
        self.CUSTOM = cust(action_type)
        # self.__custom_action_type_name = action_type
