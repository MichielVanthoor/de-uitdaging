from app import app

from flask import render_template, request
from flask_sslify import SSLify
from werkzeug.contrib.fixers import ProxyFix

app.wsgi_app = ProxyFix(app.wsgi_app)
<<<<<<< .merge_file_p2IAAE
sslify = SSLify(app)
=======
SSLify(app)
>>>>>>> .merge_file_g628I3

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/over_ons')
def over_ons():
<<<<<<< .merge_file_p2IAAE
    return render_template('over_ons.html')
=======
    return render_template('over_ons.html')
>>>>>>> .merge_file_g628I3
