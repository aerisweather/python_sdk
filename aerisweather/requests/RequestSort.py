""" Defines the available sort options for each Aeris API endpoint's requests.

    For details on the use of each sort value, see the Sorting secton of the corresponding endpoint, such
    as the Observations endpoint's sorts found here:
        https://www.aerisweather.com/support/docs/api/reference/endpoints/observations/#sorting.
"""
from collections import namedtuple


class RequestSort:

    request_sort = namedtuple('REQUEST_SORT', ['AIR_QUALITY', 'ALERTS', 'OBSERVATIONS', 'PLACES'])

    # AIR QUALITY
    aqi = namedtuple('AIR_QUALITY', ['PM2P5', 'PM10', 'NO2', 'CO', 'SO2', 'O3', 'DT', 'ID', 'NAME', 'CITY',
                                     'STATE', 'COUNTRY'])
    AIR_QUALITY = aqi('pm2p5', 'pm10', 'no2', 'co', 'so2', 'o3', 'dt', 'id', 'name', 'city', 'state', 'country')

    # ALERTS
    alrt = namedtuple('ALERTS', ['COUNTRY', 'DEWPT', 'GUST', 'ID', 'NAME', 'PRESSURE', 'RH', 'STATE', 'TEMP',
                                 'WIND', 'WIN_DIR'])
    ALERTS = alrt('country', 'dewpt', 'gust', 'id', 'name', 'pressure', 'rh', 'state', 'temp', 'wind', 'winddir')

    # CONVECTIVE_OUTLOOK
    convo = namedtuple('CONVECTIVE_OUTLOOK', ['ALL', 'ALLHAIL', 'ALLTORN', 'ALLWIND', 'CAT', 'CONHAZO', 'DAY1',
                                              'DAY2', 'DAY3', 'DAY4', 'DAY5', 'DAY6', 'DAY7', 'DAY8', 'ENHANCED',
                                              'GENERAL', 'HAIL', 'HIGH', 'MARGINAL', 'MODERATE', 'PROB', 'SLIGHT',
                                              'TORN', 'WIND', 'XHAIL', 'XTORN', 'XWIND'])
    CONVECTIVE_OUTLOOK = convo('all', 'allhail', 'alltorn', 'allwind', 'cat', 'conhazo', 'day1', 'day2', 'day3',
                               'day4', 'day5', 'day6', 'day7', 'day8', 'enhanced', 'general', 'hail', 'high',
                               'marginal', 'moderate,mod', 'prob', 'slight', 'torn', 'wind', 'xhail,sighail',
                               'xtorn,sigtorn', 'xwind.sigwind')

    # LIGHTNING
    lght = namedtuple('LIGHTNING', ['TYPE', 'PEAKAMP', 'HEIGHT', 'NUMSENSORS'])
    LIGHTNING = lght('type', 'peakamp', 'height', 'numsensors')

    # LIGHTNING SUMMARY - no sort

    # OBSERVATIONS
    obs = namedtuple('OBSERVATIONS', ['CLOSEST', 'ID', 'ROUTE', 'SEARCH', 'WITHIN'])
    OBSERVATIONS = obs('closest', 'id', 'route', 'search', 'within')

    # OBSERVATIONS ARCHIVE
    obs = namedtuple('OBSERVATIONS_ARCHIVE', ['DT'])
    OBSERVATIONS_ARCHIVE = obs('dt')

    # PLACES
    plc = namedtuple('PLACES', ['COUNTRY', 'HAS_ZIP', 'POP', 'NAME', 'STATE'])
    PLACES = plc('country', 'haszip', 'pop', 'name', 'state')

    # PRECIP SUMMARY
    precipsum = namedtuple('PRECIP_SUMMARY', ['DT', 'PRECIP'])
    PRECIP_SUMMARY = precipsum('dt', 'precip')
