import math

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