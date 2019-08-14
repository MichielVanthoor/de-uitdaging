import firebase_admin

from app import app

from flask import render_template, request
from flask_sslify import SSLify
from werkzeug.contrib.fixers import ProxyFix

default_app = firebase_admin.initialize_app()
app.wsgi_app = ProxyFix(app.wsgi_app)
sslify = SSLify(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/over_ons')
def over_ons():
    return render_template('over_ons.html')

@app.route('/sandbox')
def sandbox():
	return render_template('sandbox.html')
