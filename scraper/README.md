# IDAWEB SCRAPER
This module helps automating the request to MeteoSwiss's [Idaweb](https://gate.meteoswiss.ch/idaweb/login.do) to obtain data we are interested in.
It is based on the [Selenium WebDriver API](http://www.seleniumhq.org/projects/webdriver/), which emulates a user browsing.

## Installation
1. Install *pip* if not there yet: `sudo apt_get update && sudo apt_get install python-pip`
2. Add the path for the browser you want to use into `PATH` by executing: <br>
  `export PATH="$PATH:path/to/your/browser/application"`
3. Install *selenium*: `sudo pip install selenium`
4. Execute this command to make `run_scraper.sh` runnable for you: `chmod u+x run_scraper.sh`

## Run the scraper
Execute: `path/to/run_scraper.sh`

`run_scraper.sh` calls `idaweb_scraper.py` passing two parameters: `weather_parameter` and `year`. <br>
`idaweb_scraper.py` makes three requests (one per quarter) to obtain data about the given `weather_parameter` regarding all Cantons. <br>
The need of making three requests per year is due to Idaweb's downloading policies.

## Parameters
`run_scraper.sh` calls `idaweb_scraper.py`, which takes two inputs:
- `weather_parameter`: any parameter related to radiation measures available on Idaweb.
 + circum-global_radiation
 + global\_radiation\_std\_dev
 + global\_radiation\_ten\_min\_mean
 + longwave\_incoming\_radiation\_ten\_min\_avg
 + longwave\_outgoing\_radiation\_ten\_min\_avg
 + shortwave\_reflected\_radiation\_ten\_min\_avg
 + uvb
 + uvb\_std
 + photosynth\_std
 + diffuss
 + photosynth
- `year`: any positive integer value until 2016.

## Outputs
For each quarter of the requested `year`, we receive an e-mail with a text file conteining the data for the specified `weather_parameter`.

For each parameter, we have a log in order to monitor which quarters have been requested.

Moreover, we also have two logs to monitor the execution of our browser.
