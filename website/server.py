import sys
sys.path.insert(0, '../geocoding')

from flask import Flask, render_template, request, json
import threading, webbrowser

import geocoding_functions as geo_fns
import location_functions as loc_fns
import functions as fns
import pickle


app = Flask(__name__)
port = 5000
url = "http://127.0.0.1:{0}".format(port)

k = 4   # number of nearest stations
station_df = pickle.load(open('../geocoding/station_df.p', 'rb'))


@app.route('/')
@app.route('/index')
def index():
    """
    Start website.
    :return: homepage: index.html
    """
    return render_template('index.html')


@app.route('/getMap', methods=['POST'])
def getMap():
    """
    Update website map according to entered address.
    :return: coordinates of home and k nearest weather stations to update website map
    """
    address =  request.form['address']
    coordinates = geo_fns.getCoordinates(address)
    if(coordinates is None):
        return json.dumps(dict())

    results_dict = loc_fns.get_k_nearest_neighbours_with_coords(coordinates, k, station_df)
    results_dict['house'] = {'latitude': coordinates[0], 'longitude': coordinates[1]}

    return json.dumps(results_dict)


@app.route('/doStuff', methods=['POST'])
def doStuff():
    """
    Compute statistics for the address, roof area and electricity bill provided by the user, and show chart and barplot.
    :return:
    """
    address = request.form['address']
    coordinates = geo_fns.getCoordinates(address)
    if(coordinates is None):
        return json.dumps(dict())

    results_dict = loc_fns.get_k_nearest_neighbours_with_coords(coordinates, k, station_df)
    results_dict['house'] = {'latitude': coordinates[0], 'longitude': coordinates[1]}

    results_dict['bill'] = int(request.form['bill'])
    results_dict['roof'] = int(request.form['roof'])

    if(int(results_dict['bill']) != 0):
        results = fns.get_results(coordinates, station_df, k, int(results_dict['bill']), int(results_dict['roof']))
        results_dict.update(results)

    return json.dumps(results_dict)



if __name__=="__main__":
    threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    app.run()
