import os
import sys
sys.path.insert(0, '../geocoding')

from flask import Flask, render_template, request, json
import geocoding_functions as geo_fns

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to Python Flask!'

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
		return json.dumps({'latitude': 0, 'longtitude': 0})
	return json.dumps({'latitude': coordinates[0], 'longtitude': coordinates[1]})
	# bill = request.form['bill']
	# roof = request.form['roof']
	# return json.dumps({'address':address, 'bill':bill, 'roof':roof})

if __name__=="__main__":
    app.run()
