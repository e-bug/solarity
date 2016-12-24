#!/bin/sh

filename='idaweb_radiation_scraper.py'

# Weather parameter values:
# 	circum-global_radiation
# 	global_radiation_std_dev
# 	global_radiation_ten_min_mean
# 	longwave_incoming_radiation_ten_min_avg
# 	longwave_outgoing_radiation_ten_min_avg
# 	shortwave_reflected_radiation_ten_min_avg
# 	uvb
# 	uvb_std
# 	photosynth_std
# 	diffuss
# 	photosynth
weather_param='global_radiation_std_dev'

for y in $(seq 2014 2015)
do
   python $filename $weather_param $y
done

