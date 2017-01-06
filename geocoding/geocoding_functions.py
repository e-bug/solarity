from pygeocoder import Geocoder as geo
import googlemaps

keyFile = 'googleMaps.key'

with open(keyFile) as fp:
    for line in fp:
        myKey = line

gmaps = googlemaps.Client(key = myKey)

# returns coordinates with input address is valid and returns (0,0) if input address is invalid
def getCoordinates(address):
    # Try with pygeocoder
    try:
        geocode_result = geo.geocode(address, region = 'ch')
        return geocode_result.coordinates
    except:
        pass
    
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
        return (0,0)        
        
"""
# returns a tuple (latitude, longtitude) corresponding to coordinates of a valid address
# undefined behavior if address is not valid
def getCoordinates(address):
	return geo.geocode(address).coordinates
"""