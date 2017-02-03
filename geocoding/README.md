# Geocoding
From [Wikipedia](https://en.wikipedia.org/wiki/Geocoding):
>Geocoding is the computational process of transforming a postal address description to a location on the Earth's surface (spatial representation in numerical coordinates). Reverse geocoding, on the other hand, converts the inputted geographic coordinates to a description of a location, usually the name of a place or a postal address. Geocoding relies on a computer representation of the street network. Geocoding is sometimes used for conversion from ZIP codes or postal codes to coordinates, occasionally for the conversion of parcel identifiers to centroid coordinates.

This module shows how to retrieve the closest stations to a given postal address.

Distances between coordinates are computed using the [haversine formula](https://en.wikipedia.org/wiki/Haversine_formula): 
an equation giving great-circle distances between two points on a sphere from their longitudes and latitudes.

## Installation
We rely on:
- *pygeocoder*: a Python interface for Google Geocoding API V3. <br> To install it, just execute the following command: 
```bash
pip install pygeocoder
```
- *Google Maps Geocoding API*: when *pygeocoder* cannot find an address. Make sure you have your key in `googleMaps.key`.

## Description of the module

- `ch-cantons.topojson.json`: TopoJSON file with the geo-coordinates of each Swiss canton.
- `closestStations.ipynb`:iPython notebook showing the retrieval of the k closest weather stations to the address given by the user.
- `geocoding_functions.py`: Python module for transforming a postal address to coordinates.
- `get_stations_codename.py`: Python script generating `stations_codename.p`.
- `googleMaps.key`: file containing your key for the Google Maps Geocoding API.
- `location_functions.py`: Python module providing all the functions related to distances with respect to the user's address. E.g., retrieving the k nearest weather stations and their coordinates.
- `parseStations.ipynb`: iPython notebook generating pd.DataFrame of all the weather stations (`station_df.p`) and visualizing their locations in an interactive map (`stations_map.html`).
- `station_df.p`: pickle file of a pd.DataFrame of weather stations with columns=[name, lat, lng].
- `station_info.py`: Python module containing functions to extrapolate information about stations from `stations_legend.txt`.
- `stations_codename.p`: pickle file of a dictionary of stations codes and their names: {'code_station': 'name_station'}.
- `stations_legend.txt`: file containing information about all the Idaweb's weather stations. Each order on Idaweb includes information about the stations taking part in the order's measurements.
- `stations_map.html`: interactive map illustrating all the Idaweb's weather stations in Switzerland.
