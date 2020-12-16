from flask import Flask, render_template, send_from_directory, request, session, make_response, redirect
from data_base import Data_base
from functions import user_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

user = user_db()
DB = Data_base(user[0], user[1])

@app.route('/')
def index():
    user = session.get('user')
    if user == None: response = make_response(redirect('/sing-in'))
    else: response = make_response(render_template('index.html', user = user, name = DB.request_name(user), saldo = '0,00'))
    return response

@app.route('/sing-up', methods = ('GET', 'POST'))
def create():
    if request.method == 'GET':
        session['user'] = None
        response = make_response(render_template('/users/new.html'))
    else:
        user = request.form['user']
        name = request.form['name']
        DB.register_user(user, name)
        session['user'] = user
        response = make_response(redirect('/'))
    return response

@app.route('/sing-in')
def choise():
    session['user'] = None
    return render_template('/users/login.html', users = DB.request_users())

@app.route('/sing-in/<path:user>')
def login(user):
    session['user'] = user
    return redirect('/')

@app.route('/image/<path:path>')
def send_image(path):
    return send_from_directory('static/image', path)
    
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)