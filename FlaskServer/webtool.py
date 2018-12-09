import sys

# pip install Flask
from flask import Flask, render_template, request, redirect, Response
# pip install flask-cors
from flask_cors import CORS, cross_origin
import random, json

app = Flask(__name__)
cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

# Variables
y = 0
z = 0

@app.route('/')
def output():
    # serve index template
    return "Hello World!"

@app.route('/yz_json')
def api_yz():
    # serve index template
    return (y,z)


@app.route('/receiver', methods = ['POST'])
def worker():
    # read json + reply
    data = request.get_json(force=True)
    print("Data is:")
    print(data)
    
    y = data["y"]
    z = data["z"]

    print(y, ",", z)
    
    return "Data received"

if __name__ == '__main__':
    # run!
    app.run(host='0.0.0.0')
