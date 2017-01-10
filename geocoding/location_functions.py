import numpy as np


def haversine_distance(x, y):
    """
    Compute the haversine distance between two points.
    :param x: a point specified as (latitude,  longitude)
    :param y: a point specified as (latitude,  longitude)
    :return: haversine distance between x and y in meters
    """
    R = 6371000
    theta1 = x[0] * np.pi / 180
    theta2 = y[0] * np.pi / 180
    delta_theta = (y[0] - x[0]) * np.pi / 180
    delta_lambda = (y[1] - x[1]) * np.pi / 180
    a = np.sin(delta_theta / 2) ** 2 + np.cos(theta1) * np.cos(theta2) * np.sin(delta_lambda / 2) ** 2
    c = 2 * np.arctan(np.sqrt(a) / np.sqrt(1 - a))
    distance = R * c

    return distance


def getDistance(point1, point2):
    """
    Compute haversine distance between point1 and point2.
    :param point1: a location point specified as (latitude, longitude)
    :param point2: a location point specified as (latitude, longitude)
    :return: haversine distance in meters
    """
    assert (point1 is not None),"point1 has invalid coordinates"
    assert (point2 is not None),"point2 has invalid coordinates"
    
    return haversine_distance(point1, point2)


def getNearestStation(house, stations):
    """
    Retrieve the closest station to house among stations.
    :param house: a tuple of (lat, lng) of the user's house
    :param stations: a list of (lat, lng) tuples of weather stations
    :return: tuple (distance, stationID)
    """
    nearest = None
    distance = None
    for idx in range(0, len(stations)):
        current_distance = getDistance(house, stations[idx])
        if(distance is None or current_distance < distance):
            distance = current_distance
            nearest = idx
    
    return (distance, nearest)


def getStationDistances(house, stations):
    """
    Retrieve stations sorted by their distances from house.
    :param house: a tuple of (lat, lng) of the user's house
    :param stations: a list of (lat, lng) tuples of weather stations
    :return: sorted list of (distance, stationID) tuples
    """
    distances = []
    for idx in range(0, len(stations)):
        current_distance = getDistance(house, stations[idx])
        distances.append((current_distance, idx))
    
    return sorted(distances)


def getStationLocations(station_df):
    """
    Retrieve coordinates of all stations.
    :param station_df: a pd.DataFrame with columns=[name, lat, lng]
    :return: list of (lat, lng) tuples
    """
    allLat = station_df['lat'].get_values()
    allLng = station_df['lng'].get_values()
    stations = list(zip(allLat, allLng))
    
    return stations


def get_k_nearest_neighbours(house, k, station_df):
    """
    Retrieve the names of the k closest stations to house.
    :param house: a tuple of (lat, lng) of the user's house
    :param k: the number of stations to pick
    :param station_df: a pd.DataFrame with columns=[name, lat, lng]
    :return: sorted pd.Series of the names of the k closest stations
    """
    stations = getStationLocations(station_df)
    sorted_stations = getStationDistances(house, stations)
    if k > len(stations):
        k = len(stations)
    indx = [y[1] for y in sorted_stations[0:k]]
    
    return station_df.name[indx]


def get_weights_for_k_nearest(house, k, station_df):
    """
    Retrieve the distance weights associated to the k closest stations to house.
    :param house: a tuple of (lat, lng) of the user's house
    :param k: the number of stations to pick
    :param station_df: a pd.DataFrame with columns=[name, lat, lng]
    :return: sorted np.Array of the importance weights of the k closest stations
    """
    stations = getStationLocations(station_df)
    sorted_stations = getStationDistances(house, stations)
    distances = np.array([y[0] for y in sorted_stations[0:k]])
    weights = (1/distances) / (np.sum(1/distances))
    
    return weights
