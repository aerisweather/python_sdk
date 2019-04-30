""" Defines the available filters for each Aeris API endpoint's requests.

        For details on the use of each filter value, see the Filters secton of the corresponding endpoint, such
            as the Forecasts endpoint's filters found here:
            https://www.aerisweather.com/support/docs/api/reference/endpoints/forecasts/#filters.
    """
from collections import namedtuple


class RequestFilter:

    request_filter = namedtuple('REQUEST_FILTER', ['AIR_QUALITY', 'ALERTS', 'CONVECTIVE_OUTLOOK', 'FORECASTS',
                                                   'OBSERVATIONS', 'OBSERVATIONS_SUMMARY', 'PLACES'])

    # AIR QUALITY
    aqi = namedtuple('AIR_QUALITY', ['PM2P5', 'PM10', 'NO2', 'CO', 'SO2', 'O3', 'CHINA', 'INDIA'])
    AIR_QUALITY = aqi('pm2p5', 'pm10', 'no2', 'co', 'so2', 'o3', 'china', 'india')

    # ALERTS
    alts = namedtuple('ALERTS', ['ADVISORY', 'ALL', 'ALL_COUNTRIES', 'BEACH', 'CANADA', 'COUNTY', 'DISTINCT',
                                 'EMERGENCY', 'FIRE', 'FLOOD', 'FORECAST', 'HAS_SMALL_POLY', 'MARINE',
                                 'NON_MARINE', 'NON_PRECIP', 'NOW', 'OUTLOOK', 'STATEMENT', 'SEVERE',
                                 'SYNOPSIS', 'TORNADO', 'TROPICAL', 'TSUNAMI', 'WARNING', 'WATCH', 'WIND',
                                 'WINTER', 'USA', 'GEO'])
    ALERTS = alts('advisory', 'all', 'allcountries', 'beach', 'canada', 'county', 'distinct', 'emergency',
                  'fire', 'flood', 'forecast', 'hassmallpoly', 'marine', 'nonmarine', 'nonprecip', 'now', 'outlook',
                  'statement', 'severe', 'synopsis', 'tornado', 'tropical', 'tsunami', 'warning', 'watch', 'wind',
                  'winter', 'usa', 'geo')

    # CONVECTIVE_OUTLOOK
    conv = namedtuple('CONVECTIVE_OUTLOOK', ['ALL', 'ALLHAIL', 'ALLTORN', 'ALLWIND', 'CAT', 'CONHAZO', 'DAY1',
                                             'DAY2', 'DAY3', 'DAY4', 'DAY5', 'DAY6', 'DAY7', 'DAY8', 'ENHANCED',
                                             'GENERAL', 'HAIL', 'HIGH', 'MARGINAL', 'MODERATE', 'PROB',
                                             'SLIGHT', 'TORN', 'WIND', 'XHAIL', 'XTORN', 'XWIND', 'GEO'])
    CONVECTIVE_OUTLOOK = conv('all', 'allhail', 'alltorn', 'allwind', 'cat', 'conhazo', 'day1', 'day2', 'day3',
                              'day4', 'day5', 'day6', 'day7', 'day8', 'enhanced', 'general', 'hail', 'high',
                              'marginal', 'moderate', 'prob', 'slight', 'torn', 'wind', 'xhail,sighail',
                              'xtorn,sigtorn', 'xwind,sigwind', 'geo')

    # FORECASTS
    fcast = namedtuple('FORECASTS', ['DAY', 'DAY_NIGHT', 'HR', 'PRECISE', 'GEO'])
    FORECASTS = fcast('day', 'daynight', '#hr', 'precise', 'geo')

    # LIGHTNING
    lght = namedtuple('LIGHTNING', ['CG', 'IC', 'ALL', 'NEGATIVE', 'POSITIVE'])
    LIGHTNING = lght('cg', 'ic', 'all', 'negative', 'positive')

    # LIGHTNING SUMMARY
    lght_sum = namedtuple('LIGHTNING_SUMMARY', ['CG', 'IC', 'ALL', 'NEGATIVE', 'POSITIVE'])
    LIGHTNING_SUMMARY = lght_sum('cg', 'ic', 'all', 'negative', 'positive')

    # OBSERVATIONS
    obs = namedtuple('OBSERVATIONS', ['ALL_STATIONS', 'ALLOW_NO_SKY', 'HAS_PRECIP', 'METAR', 'MESONET', 'PWS', 'GEO'])
    OBSERVATIONS = obs('allstations', 'allownosky', 'hasprecip', 'metar', 'mesonet', 'pws', 'geo')

    # OBSERVATIONS_ARCHIVE
    obs_archive = namedtuple('OBSERVATIONS_ARCHIVE', ['ALL_STATIONS', 'CENTROID', 'HAS_PRECIP', 'HAS_SKY', 'MESONET',
                                                      'OFFICAL', 'PWS', 'GEO'])
    OBSERVATIONS_ARCHIVE = obs_archive('allstations', 'centroid', 'hasprecip', 'hassky', 'mesonet', 'official', 'pws',
                                       'geo')

    # OBSERVATIONS_SUMMARY
    obs_summary = namedtuple('OBSERVATIONS_SUMMARY', ['ALL_STATIONS', 'HAS_PRECIP', 'MESONET', 'METAR', 'OFFICAL',
                                                      'PWS', 'GEO'])
    OBSERVATIONS_SUMMARY = obs_summary('allstations', 'hasprecip', 'mesonet', 'metar', 'official', 'pws', 'geo')

    # PLACES
    pl = namedtuple('PLACES', ['AIRPORT', 'AMUSEMENT', 'BRIDGE', 'CAMP', 'CHURCH', 'COUNTY', 'DIVISIONS',
                               'FEATURE', 'FORT', 'GOLF', 'LAKE', 'NEIGHBORHOOD', 'PARISH', 'PARK',
                               'POINTS_OF_INTEREST', 'PORT', 'POPULATED_PLACES', 'RESERVE', 'SCHOOL',
                               'STADIUM', 'TEMPLE', 'TRAIL', 'TUNNEL', 'UNIVERSITY', 'WORSHIP', 'GEO'])
    PLACES = pl("airport", "amusement", "bridge", "camp", "church", "county", "divisions", "feature", "fort", "golf",
                "lake", "neighborhood", "parish", "park", "poi", "port", "ppl", "reserve", "school", "stadium",
                "temple", "trail", "tunnel", "university", "worship", "geo")

    precipsum = namedtuple('PRECIP_SUMMARY', ['MDNT2MDNT', 'HR', 'FULL_RANGE'])
    PRECIP_SUMMARY = precipsum('mdnt2mdnt', 'hr', 'fullrange')
