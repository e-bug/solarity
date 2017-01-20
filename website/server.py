import os
import sys
sys.path.insert(0, '../geocoding')

from flask import Flask, render_template, request, json
import threading, webbrowser

import geocoding_functions as geo_fns
import location_functions as loc_fns
import pickle

app = Flask(__name__)
port = 5000
url = "http://127.0.0.1:{0}".format(port)

k = 4 # number of nearest stations
station_df = pickle.load(open('../geocoding/station_df.p', 'rb'))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/doStuff', methods=['POST'])
def doStuff():
    #user = request.get_json().get('name', '')
    #return json.dumps({'user':user})
    address =  request.form['address']
    coordinates = geo_fns.getCoordinates(address)
    if(coordinates is None):
        return json.dumps(dict())

    neighbours_dict = loc_fns.get_k_nearest_neighbours_with_coords(coordinates, k, station_df)
    neighbours_dict['house'] = {'latitude': coordinates[0], 'longtitude': coordinates[1]}
    return json.dumps(neighbours_dict)
    # bill = request.form['bill']
    # roof = request.form['roof']
    # return json.dumps({'address':address, 'bill':bill, 'roof':roof})

if __name__=="__main__":
    threading.Timer(1, lambda: webbrowser.open(url)).start()
    app.run()
