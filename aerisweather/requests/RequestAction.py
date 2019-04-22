
from collections import namedtuple

request_action = namedtuple('REQUEST_ACTION', ['AIR_QUALITY',
                                               'ALERTS',
                                               'CONVECTIVE_OUTLOOK',
                                               'FORECASTS',
                                               'OBSERVATIONS',
                                               'OBSERVATIONS_SUMMARY',
                                               'PLACES'])

aqi = namedtuple('AIR_QUALITY', ['ID', 'CLOSEST', 'SEARCH', 'WITHIN', 'ROUTE'])
AIR_QUALITY = aqi('id', 'closest', 'search', 'within', 'route')

alerts = namedtuple('ALERTS', ['ONE', 'TWO'])
ALERTS = alerts('one', 'two')

conv = namedtuple('CONVECTIVE_OUTLOOK', ['AFFECTS', 'CONTAINS', 'ID', 'SEARCH'])
CONVECTIVE_OUTLOOK = conv('affects', 'contains', 'id', 'search')

forecasts = namedtuple('FORECASTS', ['ID', 'CLOSEST', 'ROUTE'])
FORECASTS = forecasts('id', 'closest', 'route')

observations = namedtuple('OBSERVATIONS', ['CLOSEST', 'ID', 'ROUTE', 'SEARCH', 'WITHIN'])
OBSERVATIONS = observations('closest', 'id', 'route', 'search', 'within')

observations_summary = namedtuple('OBSERVATIONS_SUMMARY', ['ID', 'CLOSEST', 'SEARCH', 'WITHIN'])
OBSERVATIONS_SUMMARY = observations_summary('id', 'closest', 'search', 'within')

places = namedtuple('PLACES', ['ID', 'CLOSEST', 'SEARCH', 'WITHIN'])
PLACES = places('id', 'closest', 'search', 'within')
