
""" Defines the available parameter types for each Aeris API endpoint's requests.

    For details on the use of each parameter value, see the Parameters secton of the corresponding endpoint, such
    as the Forecasts endpoint's parameters found here:
    https://www.aerisweather.com/support/docs/api/reference/endpoints/forecasts/#params.
"""
from collections import namedtuple


class ParameterType:

    parameter_type = namedtuple('PARAMETER_TYPE', ['AIR_QUALITY', 'ALERTS', 'FORECASTS', 'LIGHTNING', 'OBSERVATIONS',
                                                   'OBSERVATIONS_SUMMARY', 'PLACES'])
    # AIR QUALITY
    aqi = namedtuple('AIR_QUALITY', ['P', 'FILTER', 'QUERY', 'LIMIT', 'SKIP', 'SORT', 'FIELDS', 'FORMAT',
                                     'PLIMIT', 'PSKIP', 'PSORT', 'RADIUS', 'CALLBACK', 'MINDIST'])
    AIR_QUALITY = aqi('p', 'filter', 'query', 'limit', 'skip', 'sort', 'fields', 'format', 'plimit', 'pskip',
                      'psort', 'radius', 'callback', 'mindist')

    # ALERTS
    alerts = namedtuple('ALERTS', ['CALLBACK', 'FIELDS', 'FILTER', 'FORMAT', 'LIMIT', 'P', 'QUERY', 'RADIUS',
                                   'SKIP', 'SORT'])
    ALERTS = alerts('callback', 'fields', 'filter', 'format', 'limit', 'p', 'query', 'radius', 'skip', 'sort')

    # FORECASTS
    forecasts = namedtuple('FORECASTS', ['CALLBACK', 'FIELDS', 'FILTER', 'FROM', 'LIMIT', 'P', 'PLIMIT', 'PSKIP',
                                         'QUERY', 'SKIP', 'TO'])
    FORECASTS = forecasts('callback', 'fields', 'filter', 'from', 'limit', 'p', 'plimit', 'pskip', 'query', 'skip', 'to')

    # LIGHTNING
    lightn = namedtuple('LIGHTNING', ['CALLBACK', 'FIELDS', 'FILTER', 'FORMAT', 'FROM', 'LIMIT', 'P', 'PLIMIT', 'PSKIP',
                                      'QUERY', 'RADIUS', 'SKIP', 'SORT', 'TO'])
    LIGHTNING = lightn('callback', 'fields', 'filter', 'format', 'from', 'limit', 'p', 'plimit', 'pskip', 'query',
                       'radius', 'skip', 'sort', 'to')

    # LIGHTNING SUMMARY
    lightn_sum = namedtuple('LIGHTNING_SUMMARY', ['CALLBACK', 'FIELDS', 'FILTER', 'FORMAT', 'FROM', 'P', 'QUERY', 'RADIUS', 'TO'])
    LIGHTNING_SUMMARY = lightn_sum('callback', 'fields', 'filter', 'format', 'from', 'p', 'query', 'radius', 'to')

    # OBSERVATIONS
    observations = namedtuple('OBSERVATIONS', ['CALLBACK', 'FIELDS', 'FILTER', 'FROM', 'LIMIT', 'P', 'RADIUS',
                                               'QUERY', 'SORT', 'SKIP', 'TO'])
    OBSERVATIONS = observations('callback', 'fields', 'filter', 'from', 'limit', 'p', 'radius', 'query', 'sort',
                                'skip', 'to')

    # OBSERVATIONS_ARCHIVE
    obs_archive = namedtuple('OBSERVATIONS_ARCHIVE', ['CALLBACK', 'FIELDS', 'FILTER', 'FROM', 'LIMIT', 'P',
                                                      'PLIMIT', 'PSKIP', 'PSORT', 'QUERY', 'RADIUS', 'SORT',
                                                      'SKIP', 'TO'])
    OBSERVATIONS_ARCHIVE = obs_archive('callback', 'fields', 'filter', 'from', 'limit', 'p', 'plimit', 'pskip',
                                       'psort', 'query', 'radius', 'sort', 'skip', 'to')

    # OBSERVATIONS_SUMMARY
    obs_summary = namedtuple('OBSERVATIONS_SUMMARY', ['CALLBACK', 'FIELDS', 'FILTER', 'FROM', 'LIMIT', 'P',
                                                      'PLIMIT', 'PSKIP', 'PSORT', 'QUERY', 'RADIUS', 'SORT',
                                                      'SKIP', 'TO'])
    OBSERVATIONS_SUMMARY = obs_summary('callback', 'fields', 'filter', 'from', 'limit', 'p', 'plimit', 'pskip',
                                       'psort', 'query', 'radius', 'sort', 'skip', 'to')

    # PLACES
    places = namedtuple('PLACES', ['CALLBACK', 'FIELDS', 'FILTER', 'FORMAT', 'LIMIT', 'P', 'QUERY', 'RADIUS',
                                   'SORT', 'SKIP'])
    PLACES = places('callback', 'fields', 'filter', 'format', 'limit', 'p', 'query', 'radius', 'sort', 'skip')

    # PRECIP SUMMARY
    precipsum = namedtuple('PRECIP_SUMMARY', ['P', 'FROM', 'TO', 'FILTER', 'PLIMIT', 'PSKIP', 'PSORT'])
    PRECIP_SUMMARY = precipsum('p', 'from', 'to', 'filter', 'plimit', 'pskip', 'psort')

    # THREATS
    threats = namedtuple('THREATS', ['P', 'CALLBACK', 'RADIUS', 'FIELDS'])
    THREATS = threats('p', 'callback', 'radius', 'fields')

    # TROPICAL CYCLONES
    tropcyc = namedtuple('TROPICAL_CYCLONE', ['P', 'FIELDS', 'FILTER', 'FORMAT', 'LIMIT', 'QUERY', 'RADIUS', 'SKIP',
                                              'SORT', 'CALLBACK'])
    TROPICAL_CYCLONE = tropcyc('p', 'fields', 'filter', 'format', 'limit', 'query', 'radius', 'skip', 'sort', 'callback')
