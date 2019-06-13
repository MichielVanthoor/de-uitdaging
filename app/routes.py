from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/over_ons')
def over_ons():
    return render_template('over_ons.html')