# IDAWEB SCRAPERS
This module helps automating requests to MeteoSwiss's [Idaweb](https://gate.meteoswiss.ch/idaweb/login.do) to obtain data we are interested in.
It is based on the [Selenium WebDriver API](http://www.seleniumhq.org/projects/webdriver/), which emulates a user browsing.

## Installation
1. Install *pip* if not there yet: `sudo apt-get update && sudo apt-get install python-pip`
2. Add the path for the browser you want to use into `PATH` by executing: <br>
  `export PATH="$PATH:path/to/your/browser/application"`
3. Install *selenium*: `sudo pip install selenium`
4. Execute this command to make `run_*_scraper.sh` runnable for you: `chmod u+x run_*_scraper.sh`

## Run scrapers
Execute: `path/to/run_*_scraper.sh`

`run_*_scraper.sh` calls `idaweb_*_scraper.py` passing two parameters: `weather_parameter` and `year`. <br>
`idaweb_*_scraper.py` makes different requests for each year to obtain data about the given `weather_parameter` regarding all Cantons. <br>
The need of making multiple requests per year is due to Idaweb's downloading policies.

## Parameters
### Radiation scraper
`run_radiation_scraper.sh` calls `idaweb_radiation_scraper.py`, which takes two inputs:
- `weather_parameter`: 
 + circum-global_radiation: *Circum-global radiation; morning recordings*
 + global\_radiation\_std\_dev: *Global radiation; standard deviation*	
 + global\_radiation\_ten\_min\_mean: *Global radiation; ten minutes mean*
 + longwave\_incoming\_radiation\_ten\_min\_avg: *Longwave incoming radiation; ten minute average*
 + longwave\_outgoing\_radiation\_ten\_min\_avg: *Longwave outgoing radiation; ten minute average*
 + shortwave\_reflected\_radiation\_ten\_min\_avg: *Shortwave reflected radiation; ten minute average*
 + uvb: *UVB Strahlung Kipp & Zonen; Zehnminutenmittel*
 + uvb\_std: *UVB Strahlung Kipp & Zonen; Zehnminutenmittel, Standardabweichung*
 + photosynth\_std: *Photosynthetisch aktive Strahlung, Standardabweichung*
 + diffuss: *Diffusstrahlung; Zehnminutenmittel*
 + photosynth: *Photosynthetisch aktive Strahlung*
- `year`: *any positive integer value until 2016.*

### Temperature scraper
`run_radiation_scraper.sh` calls `idaweb_radiation_scraper.py`, which takes two inputs:
- `weather_parameter`:
 + temp_2_m_current_val: *Air temperature 2 m above ground; current value*
- `year`: *any positive integer value until 2016.*

### Wind scraper
`run_radiation_scraper.sh` calls `idaweb_radiation_scraper.py`, which takes two inputs:
- `weather_parameter`:
 + wind_scalar_10m_mean: *Wind speed scalar; ten minutes mean*
- `year`: *any positive integer value until 2016.*

## Outputs
For each period (different granularity for each scraper) of the requested `year`, we receive an e-mail with a text file conteining the data for the specified `weather_parameter`.

For each parameter, we have a log in order to monitor which periods have been requested.

Moreover, we also have two logs to monitor the execution of our browser.
