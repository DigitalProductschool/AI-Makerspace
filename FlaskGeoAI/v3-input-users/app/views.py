from app import app
from flask import render_template, request, redirect, jsonify, make_response, session
from datetime import datetime

import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore



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

