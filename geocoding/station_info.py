import re

def getStationNamesAndLocations(stationsFile):
    station_dict = {}
    with open(stationsFile) as fp:
        for line in fp:
            name, lat, lng = getParsedStation(line)
            station_dict[name] = (lat, lng)
    return station_dict
        
        
def getParsedStation(string):
    name = string.split()[0]
    lat_lng = re.search("(\d+)°(\d+)'/(\d+)°(\d+)'", string).group(0)
    lng = lat_lng.split('/')[0]
    lat = lat_lng.split('/')[1]
    return name, degreeMin2Decimal(lat), degreeMin2Decimal(lng)

def degreeMin2Decimal(dm):
    # Whole of swiss is in NE.
    deg = int(dm.split('°')[0])
    minutes = int(dm.split('°')[1].split('\'')[0])
    return deg + minutes/60