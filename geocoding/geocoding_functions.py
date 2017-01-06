from pygeocoder import Geocoder as geo

def is_address_valid(address):
    """
    Check if the passed address is valid.
    :param address: string representing a street address. E.g., "Avenue du Temple 3, Renens, Switzerland"
    :return: True if the address is valid, False otherwise
    """
    result = False
    try:
        result = geo.geocode(address).valid_address
    except:
        pass
    return result


def get_coordinates(address):
    """
    Retrieve coordinates of given street address.
    :param address: string representing a street address. E.g., "Avenue du Temple 3, Renens, Switzerland"
    :return: a tuple (latitude, longtitude) corresponding to coordinates of a valid address, None otherwise
    """
    if is_address_valid(address):
        return geo.geocode(address).coordinates
    else:
        return None