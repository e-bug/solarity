#!/bin/sh

filename='idaweb_temperature_scraper.py'

# Weather parameter values:
# 	temp_2_m_current_val
weather_param='temp_2_m_current_val'

for y in $(seq 2015 2015)
do
   python $filename $weather_param $y
done

