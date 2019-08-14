import firebase_admin
from flask import render_template, request
from app import app

default_app = firebase_admin.initialize_app()

@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

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