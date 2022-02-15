from app import app
from flask import render_template, request, redirect, jsonify, make_response, session
from datetime import datetime

 
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


