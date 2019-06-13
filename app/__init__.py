from flask import Flask
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

from app import routes