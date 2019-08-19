from app import app

from flask import render_template, request
from flask_sslify import SSLify
import os
from werkzeug.contrib.fixers import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app)
SSLify(app)

@app.route('/')
@app.route('/index')
def index():
    mode = os.environ['MODE']
    print(mode)
    if mode == "development":
        return render_template('index.html', mode=mode)

    return render_template('index.html')

@app.route('/over_ons')
def over_ons():
    return render_template('over_ons.html')
