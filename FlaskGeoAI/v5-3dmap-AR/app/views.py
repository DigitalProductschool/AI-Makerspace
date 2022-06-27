from app import app
from flask import render_template, request, redirect, jsonify, make_response, session
from datetime import datetime

import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


import os
import json
import certifi
from datetime import datetime
import geopandas as gpd
import pandas as pd
import pandas as pd
from pymongo import MongoClient, cursor


'''
Firebase Login
'''
 
config = {  #everything will be different in your credentials
  "apiKey": "yourapikey",
  "authDomain": "buildai-hamburg.firebaseapp.com",
  "databaseURL": "https://buildai-hamburg.firebaseio.com",
  "projectId": "buildai-hamburg",
  "storageBucket": "buildai-hamburg.appspot.com",
  "messagingSenderId": "yourid",
  "appId": "yourid",
  "measurementId": "yourid"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()

cred = credentials.Certificate('firebase_certificate.json')
firebase_admin.initialize_app(cred)

db2 = firestore.client()





 
@app.route('/')
def index():
    return render_template('public/index.html')

@app.route('/feedback')
def feedback():
    return render_template('public/feedback.html')

@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/design')
def design():
    return render_template('public/design.html')

@app.route('/input', methods=['GET','POST'])
def input():
    if request.method == 'POST':
        if request.form['submit'] == 'add':
            name = request.form['name']
            p_id = 685759
            count = 1
            doc_ref = db2.collection(u'Comments_Hamburg')
            count = db2.collection(u'Comments_Hamburg').stream()
            docx_count = []
            for xc in count:
                docx_count.append(xc.to_dict())
            maxx = []
            for xf in docx_count:
                maxx.append(xf['counter'])
            if len(maxx) > 0:
                max_count = max(maxx)
            else:
                max_count = 0            
            count = max_count + 1
            doc_ref.add({u'comment':name,u'projectcode':p_id,u'counter':count})
            docs = db2.collection(u'Comments_Hamburg').stream()
            docx = []
            for xx in docs:
                docx.append(xx.to_dict())
            #print(docx)
            docxxx = sorted(docx, key = lambda i: i['counter'],reverse=True)
            return render_template('public/input.html', t=docxxx)
        #elif request.form['submit'] == 'delete':
            #db.child("comment").remove()
            #db.child("p_id").remove()
        #return render_template('public/project1.html')
        elif request.form['submit'] == 'mongo':
            print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    docs = db2.collection(u'Comments_Hamburg').stream()
    docx = []
    for xx in docs:
        docx.append(xx.to_dict())
    #print(docx)
    docxxx = sorted(docx, key = lambda i: i['counter'],reverse=True)
    return render_template('public/input.html', t=docxxx)

# dump traffic geojson data route
@app.route('/data', methods=['GET','POST'])
def data():
    PREFIX = "mongodb+srv://"
    USERNAME = "amartya:"
    PASSWORD2 = "your password"
    SUFFIX = "@skkroly.kankd.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(PREFIX + USERNAME + PASSWORD + SUFFIX, tlsCAFile=certifi.where())
    db = client.get_database('skkrolydb')
    collection = db.traffic_signal
    t_signal = pd.DataFrame(list(collection.find({})))
    data = t_signal['features'][0]
    return make_response(jsonify(data), 201)

# dump hotspot geojson data route
@app.route('/data2', methods=['GET','POST'])
def data2():
    PREFIX2 = "mongodb+srv://"
    USERNAME2 = "amartya:"
    PASSWORD2 = "your password"
    SUFFIX2 = "@skkroly.kankd.mongodb.net/test?retryWrites=true&w=majority"
    client2 = MongoClient(PREFIX2 + USERNAME2 + PASSWORD2 + SUFFIX2, tlsCAFile=certifi.where())
    db2 = client2.get_database('skkrolydb')
    collection2 = db2.its_data
    t_signal2 = pd.DataFrame(list(collection2.find({})))
    data2 = t_signal2['features'][0]
    return make_response(jsonify(data2), 201)

@app.route('/map')
def map():
    return render_template('public/map.html')

@app.route('/map3d')
def map3d():
    return render_template('public/map3d.html')