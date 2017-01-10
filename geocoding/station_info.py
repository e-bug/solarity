import re


def degreeMin2Decimal(dm):
    """
    Convert a degree-minute coordinate to a decimal number.
    :param dm: degree-minute coordinate
    :return: decimal number corresponding to the passed degree-minute coordinate
    """
    # Whole of Switzerland is in NE.
    deg = int(dm.split('°')[0])
    minutes = int(dm.split('°')[1].split('\'')[0])

    return deg + minutes/60


def getParsedStation(string):
    """
    Retrieve name, latitude and longitude of a station from a line in Idaweb's legends.
    :string: line of Idaweb's legend file corresponding to a station information
    :return: name, lat, lng of the station in the passed string
    """
    name = string.split()[0]
    lat_lng = re.search("(\d+)°(\d+)'/(\d+)°(\d+)'", string).group(0)
    lng = lat_lng.split('/')[0]
    lat = lat_lng.split('/')[1]
    
    return name, degreeMin2Decimal(lat), degreeMin2Decimal(lng)


def getStationNamesAndLocations(stationsFile):
    """
    Retrieve Idaweb stations from passed file.
    :param stationsFile: file containing a station information per line
    :return: dictionary of {'station_name': (station_lat, station_lng)}
    """
    station_dict = {}
    with open(stationsFile) as fp:
        for line in fp:
            name, lat, lng = getParsedStation(line)
            station_dict[name] = (lat, lng)

    return station_dict
