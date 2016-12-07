from pygeocoder import Geocoder as geo

# returns True if the input address is valid, False otherwise
def isAddressValid(address):
	return geo.geocode(address).valid_address

# returns a tuple (latitude, longtitude) corresponding to coordinates of a valid address
# undefined behavior if address is not valid
def getCoordinates(address):
	return geo.geocode(address).coordinates