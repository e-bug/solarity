import os
from flask import Flask, render_template, request, json

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
	bill = request.form['bill']
	roof = request.form['roof']
	return json.dumps({'address':address, 'bill':bill, 'roof':roof})

if __name__=="__main__":
    app.run()
