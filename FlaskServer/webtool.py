import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/')
def output():
    # serve index template
    return "Hello World!"

@app.route('/receiver', methods = ['POST'])
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
