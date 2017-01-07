from pygeocoder import Geocoder as geo
import googlemaps

keyFile = 'googleMaps.key'

with open(keyFile) as fp:
    myKey = fp.readline()

gmaps = googlemaps.Client(key = myKey)


def getCoordinates(address):
    """
    Retrieve coordinates of given street address in Switzerland.
    :param address: string representing a street address. E.g., "Avenue du Temple 3, Renens, Switzerland"
    :return: a tuple (latitude, longtitude) corresponding to coordinates of a valid address, None otherwise
    """

    # Try with pygeocoder
    try:
        geocode_result = geo.geocode(address, region = 'ch')
        return geocode_result.coordinates
    except:
        # Try with Google Maps API
        geocode_result = gmaps.geocode(address, region = 'ch')
        if(len(geocode_result) > 0):
            coordinates = geocode_result[0]['geometry']['location']
            return (coordinates['lat'], coordinates['lng'])
    
        # Try with Google Maps with only the street name
        street_name = address.split(',')[0]
        geocode_result = gmaps.geocode(street_name, region = 'ch')
        if(len(geocode_result) > 0):
            coordinates = geocode_result[0]['geometry']['location']
            return (coordinates['lat'], coordinates['lng'])
        else:
            return None        
        
