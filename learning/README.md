# Learning

This module shows how to define a regression model from weather data to produced power by a solar plant and how to use such a model to estimate the power produced at a given location.

## Description of the module

- `ELL data/`: folder containing data relative to the EPFL ELL measurements.
  - `ELL_temp_wind_df.p`: pd.DataFrame containing temperature and wind indexed by time.
  - `irradiance.csv`: CSV file containing time and irradiance measurements every minute from Jan 1, 2016 to Jul 9, 2016.
  - `power.csv`: CSV file containing time and power measurements every minute from Jan 1, 2016 to Jul 9, 2016.
- `ECS-240265M60-ALL-BLACK-1.pdf`: datasheet for a photovoltaic module from [ECSOLAR](http://www.ecsolar.com/). In French.
- `all_features.p`: pd.DataFrame containing average irradiance, temperature and wind per month for each station.
- `extractTempAndWindFromMeteoLausanne.ipynb`: iPython notebook showing how to retrieve temperature and wind information in Lausanne for the EPFL measurements. It makes use of the weather data from MeteoLausanne, which is not in the repository due to its large size.
- `groupedStations.p`: pd.DataFrame containing average irradiance and power per month for each station.
- `groupedStationsAllFeatures.p`: pd.DataFrame containing average irradiance, temperature, wind and power per month for each station.
- `irradMean.p`: TODO_DESCRIPTION. The size of this file exceeds the maximum allowed size in GitHub.
- `irrad-meanFromIdaweb.ipynb`: iPython notebook showing how to  estimate the produced power for each month at each station.
- `model.p`: most accurate regression model for produced power at ELL using only irradiance at ELL. 
- `modelWithTempAndWind.ipynb`: most accurate regression model for produced power at ELL using only irradiance, temperature and wind. Less accurate than `model.p`.
- `model_with_temp_wind.p`most accurate model for produced power at ELL using irradiance, temperature and wind.
- `regressionModels.ipynb`: iPython notebook showing different regressors for relating weather measurements to produced power at ELL.
