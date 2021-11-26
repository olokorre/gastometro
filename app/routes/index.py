from flask.templating import render_template
from app import app
from flask import send_from_directory, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image/<path:path>')
def send_image(path):
    return send_from_directory('static/image', path)
    
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)


@app.route('/favicon.ico')
def icon():
    return send_from_directory('static/image/', 'favicon.ico')