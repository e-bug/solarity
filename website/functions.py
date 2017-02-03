import location_functions as loc_fns
import numpy as np
import pickle


# TIME VARIABLES
totalYears = 25
monthsInAYear = 12
hoursInADay = 24
daysInAMonth = 30

# COST VARIABLES
elecTariff = 0.20      # CHF/kWh
capacityPerPanel = 255 # Wp
costPerPanel = 500     # CHF
panelArea = 1.62       # m2

# STATIONS MONTHLY INFORMATION
means = pickle.load(open('../learning/groupedStations.p', 'rb'))



def get_average_power_potential(stations, weights, means):
    """
    Retrieve monthly average power potential for home according to weighted sum of potentials from closest stations.
    :param stations: a pd.DataFrame with columns=[name, lat, lng]
    :param weights: a sorted np.Array of distance weights associated to the k closest stations to house
    :param means: a pd.DataFrame of average montly potential for each station
    :return: monthly average power potential for home address
    """
    potential = 0
    for i in range(len(stations)):
        potential += np.sum(means.power[stations[i]].get_values()) * \
                     weights[i] / len(means.power[stations[i]].get_values())
    
    return potential


def get_new_bill(bill, power, elec_tariff):
    """
    Compute monthly electricity bill when using installation giving passed solar power.
    :param bill: monthly electricity bill of user
    :param power: monthly solar power produced with a given installation
    :param elec_tariff: electricity tariff at user's house location
    :return: new monthly average electricity bill and new monthly usage pattern for the produced solar power
    """
    avgEnergyUsed = bill / elec_tariff
    avgEnergyUsed_daytime = avgEnergyUsed / 2
    nightUsage = avgEnergyUsed / 2

    avgEnergyProduced = power * hoursInADay * daysInAMonth
    
    newBill = np.empty(len(power))
    newUsageFromUtility = np.empty(len(power))
    for i in range(len(power)):
        dayUsage = max(0, avgEnergyUsed_daytime - avgEnergyProduced[i])
        newUsageFromUtility[i] = dayUsage + nightUsage
        newBill[i] = newUsageFromUtility[i] * elec_tariff

    return newBill, newUsageFromUtility


def get_cumulative_savings(oldBill, newBill, cost):
    """
    Compute savings over 25 years earned by going solar.
    :param oldBill: average monthly electricity bill of the user before installing solar panels
    :param newBill: monthly electricity bill when installing a given number of solar panels
    :param cost: initial investment for solar installation
    :return:
    """
    months = range(1, totalYears*monthsInAYear + 1)
    savings = np.empty((len(newBill), len(months)))
    for i in range(len(newBill)):
        eachMonth = oldBill - newBill[i]
        savings[i,:] = eachMonth * months - cost[i]
    return savings


def get_break_even_time(savings):
    """
    Compute number of years until payback for each possible installation plan.
    :param savings:
    :return: array of number of years until payback
    """
    nInstalls = savings.shape[0]
    breakEven = np.empty(nInstalls)
    for i in range(nInstalls):
        breakEven[i] = np.argmax(savings[i,:] > 0)

    return breakEven


def get_results(coordinates, stations, k, bill, roof_area):
    """
    Retrieve break even, capacity, solar power, cost and savings for all possible installation options.
    :param coordinates: (lat,lng) coordinates of home address
    :param stations: a pd.DataFrame with columns=[name, lat, lng]
    :param k: number of nearest weather stations
    :param bill: average electricity bill of the user (CHF)
    :param roof_area: approximated roof area of the user (m2)
    :return: dictionary of dictionaries containing the results to be fed into JS.
    """
    neighbourNames = loc_fns.get_k_nearest_neighbours(coordinates, k, stations)
    neighbourWeights = loc_fns.get_weights_for_k_nearest(coordinates, k, stations)

    potential = get_average_power_potential(neighbourNames.get_values(), neighbourWeights, means)   # Wp

    # Get the user values
    averageElectricityBill = np.array([bill])   # CHF

    # Compute electric power and solar power for all installation options
    avgPower = averageElectricityBill / (elecTariff * hoursInADay * daysInAMonth)   # kW

    installation = np.array(range(5,101,5)) / 100
    numPanels = np.floor(roof_area / panelArea)
    capacity = installation * numPanels * capacityPerPanel / 1000   # kWp
    cost = installation * numPanels * costPerPanel  # CHF
    solarPower = capacity * potential   # kW

    # Take only installation plans with less solarPower than avgPower
    indxx = solarPower <= avgPower
    newBill, newUsage = get_new_bill(averageElectricityBill, solarPower[indxx], elecTariff)
    savings = get_cumulative_savings(averageElectricityBill, newBill, cost[indxx])
    breakEven = get_break_even_time(savings) / monthsInAYear
    finalSavings = savings[:,-1]

    results = dict()
    for i in range(0, 20):
        if(solarPower[i] <= avgPower):
            indexName = 'result_' + str((i + 1) * 5)
            results[indexName] = {'type': 'result', 'percentage': 5 * (i + 1),
                                  'breakEven': round(breakEven[i]*2)/2, 'cost': int(cost[i]), 
                                  'capacity': capacity[i], 'power': solarPower[i], 'savings': int(finalSavings[i])}

    return results
