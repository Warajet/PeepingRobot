import sys

# pip install Flask
from flask import Flask, render_template, request, redirect, Response
# pip install flask-cors
from flask_cors import CORS, cross_origin
import random, json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def output():
    # serve index template
    return "Hello World!"

@app.route('/receiver', methods = ['POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def worker():
    # read json + reply
    data = request.get_json()
    result = ''

    for item in data:
    # loop over every row
        result += str(item['make']) + '\n'
        return result

if __name__ == '__main__':
    # run!
    app.run(host='0.0.0.0')
