import math
import numpy as np

# returns distance between two points
def getDistance(point1, point2):
	return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

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