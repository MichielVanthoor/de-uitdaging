from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
talisman = Talisman( app, force_https_permanent='true', force_https='true')

from app import routes