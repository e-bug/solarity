# Geocoding
From [Wikipedia](https://en.wikipedia.org/wiki/Geocoding):
>Geocoding is the computational process of transforming a postal address description to a location on the Earth's surface (spatial representation in numerical coordinates). Reverse geocoding, on the other hand, converts the inputted geographic coordinates to a description of a location, usually the name of a place or a postal address. Geocoding relies on a computer representation of the street network. Geocoding is sometimes used for conversion from ZIP codes or postal codes to coordinates, occasionally for the conversion of parcel identifiers to centroid coordinates.

This module shows how to retrieve the closest stations to a given postal address. <br>
Distances between coordinates are computed using the [haversince formula](https://en.wikipedia.org/wiki/Haversine_formula): 
an equation giving great-circle distances between two points on a sphere from their longitudes and latitudes.

## Installation
We rely on `pygeocoder`: a Python interface for Google Geocoding API V3. <br>
To install it, just execute the following command:
```bash
pip install pygeocoder
```
