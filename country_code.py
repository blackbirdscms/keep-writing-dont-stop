from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """return two digit code based on the country name"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if not found
    return None
