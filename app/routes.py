from app import app

from flask import render_template, request
from flask_sslify import SSLify
from werkzeug.contrib.fixers import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app)
SSLify(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/over_ons')
def over_ons():
    return render_template('over_ons.html')