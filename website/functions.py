import geocoding_functions as geo_fns
import location_functions as loc_fns
import numpy as np
import pickle

totalYears = 25
monthsInAYear = 12
hoursInADay = 24
daysInAMonth = 30

def get_monthly_power_potential(stations, weights, means):
    potential = 0
    for i in range(len(stations)):
    	print(len(means.power[stations[i]].get_values()))
    	potential = potential + means.power[stations[i]].get_values() * weights[i]
    
    return potential

def get_new_bill(bill, power, elecTarrif):
    avgEnergyUsed = bill / elecTarrif
    avgEnergyUsed_daytime = avgEnergyUsed / 2
    nightUsage = avgEnergyUsed / 2

    avgEnergyProduced = power * hoursInADay * daysInAMonth
    
    newBill = np.empty(len(power))
    newUsageFromUtility = np.empty(len(power))
    for i in range(len(power)):
        dayUsage = max(0, avgEnergyUsed_daytime - avgEnergyProduced[i])
        newUsageFromUtility[i] = dayUsage + nightUsage
        newBill[i] = newUsageFromUtility[i] * elecTarrif

    return newBill, newUsageFromUtility

def get_cummulative_savings(oldBill, newBill, cost):
    months = range(1, totalYears*monthsInAYear + 1)
    savings = np.empty((len(newBill), len(months)))
    for i in range(len(newBill)):
        eachMonth = oldBill - newBill[i]
        savings[i,:] = eachMonth * months - cost[i]
    return savings

def get_break_even_time(savings):
    nInstalls = savings.shape[0]
    breakEven = np.empty(nInstalls)
    for i in range(nInstalls):
        breakEven[i] = np.argmax(savings[i,:] > 0)

    return breakEven

def getResults(coordinates, stations, k, bill, roofArea):
	neighbourNames = loc_fns.get_k_nearest_neighbours(coordinates, k, stations)	
	neighbourWeights = loc_fns.get_weights_for_k_nearest(coordinates, k, stations)

	means = pickle.load(open('../learning/groupedStations.p', 'rb'))
	# means = pickle.load(open('../learning/groupedStationsAllFeatures.p', 'rb'))

	monthly_potential = get_monthly_power_potential(neighbourNames.get_values(), neighbourWeights, means)
	potential = np.mean(np.array(monthly_potential)) ## in Wp

	# Get the user values
	averageElectricityBill = np.array([bill]) ## CHF

	elecTarrif = 0.20 ##CHF/Kwh

	capacityPerPanel = 255 ## Wp
	costPerPanel = 500 ## CHF
	panelArea = 1.62 ## m2

	avgPower = averageElectricityBill / (elecTarrif * hoursInADay * daysInAMonth) # kW

	installation = np.array(range(5,101,5)) / 100
	numPanels = np.floor(roofArea / panelArea)
	capacity = installation * numPanels * capacityPerPanel / 1000 # kWp
	cost = installation * numPanels * costPerPanel # CHF
	solarPower = capacity * potential # kW

	# take index as only those with less solarPower than avgPower
	indxx = solarPower <= avgPower
	newBill, newUsage = get_new_bill(averageElectricityBill, solarPower[indxx], elecTarrif)
	savings = get_cummulative_savings(averageElectricityBill, newBill, cost[indxx])
	breakEven = get_break_even_time(savings) / monthsInAYear

	results = dict()
	for i in range(0, 20):
		if(solarPower[i] <= avgPower):
			indexName = 'result_' + str((i + 1) * 5)
			results[indexName] = {'type': 'result', 'percentage': 5 * (i + 1), 'breakEven': breakEven[i], 'cost': cost[i]}

	return results