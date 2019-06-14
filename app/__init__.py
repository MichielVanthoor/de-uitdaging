from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
csp = {
    'default-src': '\'self\'',
    'img-src': '*',
    'media-src': '*',
    'script-src': '*'
}

talisman = Talisman(app, content_security_policy=csp)

from app import routes