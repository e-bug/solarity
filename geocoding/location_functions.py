import numpy as np


def haversine_distance(x, y):
    """
    Compute the haversine distance between two points.
    :param x: point specified as (latitude,  longitude)
    :param y: point specified as (latitude,  longitude)
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
    :param point1: location point specified as (latitude, longitude)
    :param point2: location point specified as (latitude, longitude)
    :return: haversine distance in meters
    """
    assert (point1 is not None),"point1 has invalid coordinates"
    assert (point2 is not None),"point2 has invalid coordinates"
    return haversine_distance(point1, point2)


# returns a tuple (distance, stationID)
def getNearestStation(house, stations):
	nearest = None
	distance = None
	for idx in range(0, len(stations)):
		current_distance = getDistance(house, stations[idx])
		if(distance is None or current_distance < distance):
			distance = current_distance
			nearest = idx
	return (distance, nearest)

# returns a sorted list of (distance, stationID) tuples
def getStationDistances(house, stations):
	distances = []
	for idx in range(0, len(stations)):
		current_distance = getDistance(house, stations[idx])
		distances.append((current_distance, idx))
	return sorted(distances)

# returns station latitude and longitudes
def getStationLocations(station_df):
	allLat = station_df['lat'].get_values()
	allLng = station_df['lng'].get_values()
	stations = list(zip(allLat, allLng))
	return stations

def get_k_nearest_neighbours(house, k, station_df):
	stations = getStationLocations(station_df)
	sorted_stations = getStationDistances(house, stations)
	indx = [y[1] for y in sorted_stations[0:k]]
	return station_df.name[indx]

def get_weights_for_k_nearest(house, k, station_df):
	stations = getStationLocations(station_df)
	sorted_stations = getStationDistances(house, stations)
	distances = np.array([y[0] for y in sorted_stations[0:k]])
	weights = (1/distances)/(np.sum(1/distances))
	return weights
