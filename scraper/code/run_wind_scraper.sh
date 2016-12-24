#!/bin/sh

filename='idaweb_wind_scraper.py'

# Weather parameter values:
# 	wind_scalar_10m_mean
weather_param='wind_scalar_10m_mean'

for y in $(seq 2011 2015)
do
   python $filename $weather_param $y
done

