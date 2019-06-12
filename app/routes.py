from flask import render_template
from app import app


@app.before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/over_ons')
def over_ons():
    return render_template('over_ons.html')