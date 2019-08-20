from app import app

from firebase_admin import credentials
from firebase_admin import firestore
from flask import render_template, request
from flask_sslify import SSLify
import os
from werkzeug.contrib.fixers import ProxyFix

# Configure HTTPS redirect
app.wsgi_app = ProxyFix(app.wsgi_app)
SSLify(app)

# Use the application default credentials and connect db
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
  'projectId': '',
})

db = firestore.client()

# Overview of all the routes
@app.route('/')
@app.route('/index')
def index():
    mode = os.environ['MODE']
    print(mode)
    return render_template('index.html')

@app.route('/over_ons')
def about_us():
    return render_template('about_us.html')

@app.route('/projects')
def projects():
    projects = db.collection(u'projects')
    docs = users_ref.stream()

    for doc in docs:
        print(u'Cause was {}'.format(doc.cause)

    return render_template('projects.html')