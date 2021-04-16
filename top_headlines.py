import json
import numpy as np 
import pandas as pd 
from flask import Flask, render_template
from secrets import API_KEY
import requests

app = Flask(__name__)

@app.route('/')
def index():     
    return '<h1>Welcome!</h1>'

@app.route('/name/<nm>')
def hello_name(nm):
    return render_template('name.html',name=nm)

@app.route('/headlines/<nm>')
def headlines(nm):
    results = []
    headlines_json = requests.get('https://api.nytimes.com/svc/topstories/v2/technology.json?api-key='+API_KEY).json()
    for i in range(5):
        results.append(headlines_json['results'][i]['title'])
    return render_template('headlines.html',name=nm,headlines=results)

@app.route('/links/<nm>')
def links(nm):
    results = []
    urls = []
    headlines_json = requests.get('https://api.nytimes.com/svc/topstories/v2/technology.json?api-key='+API_KEY).json()
    for i in range(5):
        results.append(headlines_json['results'][i]['title'])
        urls.append(headlines_json['results'][i]['url'])
    return render_template('links.html',name=nm,headlines=results,urls = urls)

@app.route('/images/<nm>')
def images(nm):
    results = []
    urls = []
    images = []
    headlines_json = requests.get('https://api.nytimes.com/svc/topstories/v2/technology.json?api-key='+API_KEY).json()
    for i in range(5):
        results.append(headlines_json['results'][i]['title'])
        urls.append(headlines_json['results'][i]['url'])
        images.append(headlines_json['results'][i]['multimedia'][0]['url'])
    return render_template('images.html',name=nm,headlines=results,urls = urls,images = images)

if __name__ == '__main__':  
    print('starting Flask app', app.name)
    app.run(debug=True)
