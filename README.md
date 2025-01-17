# Solarity: Solar Clarity for Swiss Households
Team members: [Emanuele Bugliarello](https://github.com/e-bug), [Maaz Mohiuddin](https://github.com/maaz15), and [Wajeb Saab](https://github.com/Wajeb).

## Abstract
The massive drive towards renewable energy from Swiss electrical utilities is making domestic solar installations wide-spread all across Switzerland. To make an informed decision about the installations, households require information regarding the initial investment, overall cost, and potential savings, tailored to each person's needs. Google's [Project Sunroof](https://www.google.com/get/sunroof) is aimed at providing this information and is currently available for only a few select states in the United States. Our aim in this project is to provide a similar platform for Switzerland. We use weather data to estimate how much solar energy each area in Switzerland can generate. Additionally, based on historical weather data, we predict the solar energy production in the coming years. We couple this information with other inputs, such as roof size and average energy consumption, to provide each person with information regarding the initial investment, overall cost, break-even time, and potential savings.

## Data description
The data to be used for this project is not publicly available and its retrieval is the first challenging aspect of this project.
As a first step, we are interested in two kinds of data from the weather recordings: (1) solar irradiation, both direct and diffused, (2) cloud overcast.
We have access to weather data archives from [meteoswiss](http://www.meteoswiss.admin.ch/home.html?tab=overview) and [meteolausanne](http://meteolausanne.com/). Other sources might be useful in the future to provide more accurate estimates.

Data from meteolausanne is stored in a text file of approximately 100MB. It provides different metrics for a single point in the entire Lausanne area and it spans from July 2008 to October 2016 with a granularity of 10 minutes for the first three years and 5 minutes afterwards.

Data from meteoswiss helps us producing estimates for other areas as well. The amount of data is much larger but not easily retrievable. In fact, no API is provided and we need to use their portal to ask for specific metrics to be sent to us via e-mail as csv files. Acquiring good understanding of meteoswiss's data and portal is our first effort in this project.

Besides data on weather, we acquire data on energy tariffs, solar panel efficiency, etc.

## Feasibility and Risks
The project consists of three main parts:

1. **Data Retrieval**: Given that the data is not publicly available, one of the challenging aspects of this project is gathering the relevant data. A risk is the inability to get this relevant data for many areas in Switzerland.
2. **Data Analysis**: The analysis required for this project is not immediately within our field of expertise. We need the help of experts in order to understand and complete this challenging part. We have identified two different challenges:
    * Estimating solar potential in a given year from the weather data
    * Predict solar potential in the coming years based on the historic data
3. **Data Visualization**: Producing a platform with a clean interface and that is easily usable is one of the main challenging aspects of this project.

Using weather data allows us to provide estimates for an area rather than each specific house (as in the Google's Project Sunroof). Although less accurate, our idea uses data that is more readily and publicly available, which allows it to be reproduced in other areas.

## Deliverables
Our main goal is to deliver a platform that a user can query. The inputs of a query is the address, roof size, and average monthly/quarterly energy consumption of the user. The output is a viz that shows different options that the user can purchase, based on their initial investment, monthly/quarterly savings, and break-even time.

## Timeplan

| Deliverable | Due Date | Status |
|----------|-------------|--------|
| Retrieve & Understand weather data  |  November 20, 2016 | :white_check_mark: |
| Wrangle weather data & retrieve financial data from different solar panel providers   |    December 4, 2016   | :white_check_mark: |
| Apply model to the data to transform weather information such as cloud information, irradiation, etc. to solar energy potential for the current year   | December 11, 2016 | :white_check_mark: |
| Basic platform & basic outputs based on collected data; completed & tested |    December 18, 2016   | :white_check_mark: |
| Predict solar potential in future years based on trend in previous years |    January 8, 2017   | :white_check_mark: |
| Final platform & viz; completed & tested   |    January 15, 2017   | :white_check_mark: |


## Description of this repository

The project is splitted into several modules, each dealing with a different aspect of our system.

- `Solarity.ipynb`: iPython notebook showing the entire pipeline to estimate the solar power production according to the user's inputs. It makes use of the results obtained from the different modules of the project.
- `economicParameters/`: module introducing the costs for solar and electricity in Switzerland.
- `geocoding/`: module showing how to retrieve the closest weather stations to a given postal address.
- `learning/`: module showing how to train a regression model from weather data to produced power by a solar plant and to use it for predicting the power produced at a given location.
- `projectPresentation/`: folder containing slides and poster shown during the project presentation.
- `sampleData/`: folder containing samples of each weather parameter collected from Idaweb. 
- `scraper/`: module showing how to automate requests to MeteoSwiss's Idaweb to obtain weather data.
- `website/`: module containing the website for the project.
