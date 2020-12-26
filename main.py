from flask import Flask, render_template, send_from_directory, request, session, make_response, redirect
from data_base import Data_base
from functions import user_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

user = user_db()
DB = Data_base(user[0], user[1])

# index
@app.route('/')
def index():
    user = session.get('user')
    saldo = DB.calc_balance()
    if user == None: response = make_response(redirect('/sing-in'))
    else: response = make_response(render_template('index.html',user=user,name=DB.request_name(user),saldo=saldo))
    return response

# Registros
@app.route('/registers', methods = ('GET', 'POST'))
def registers():
    user = session.get('user')
    if user == None: response = make_response(redirect('/sing-in'))
    elif request.method == 'GET':
        registers = DB.get_register()
        response = render_template('registers.html',user=user,registers=registers,type=type)
    elif request.method == 'POST':
        owner = DB.request_name(user)
        date = request.form['date']
        title = request.form['title']
        detais = request.form['detais']
        value = request.form['value']
        _type = request.form['type']
        _class = request.form['class']
        try: float(value)
        except: response = 'value deve ser um número'
        else:
            DB.regist(owner, date, title, detais, value, _type, _class)
            response = make_response(redirect('/registers'))
    return response

#deletar um registro
@app.route('/registers/d/<path:path>')
def edit_registers(path):
    user = session.get('user')
    if user == None: response = make_response(redirect('/sing-in'))
    else:
        try: DB.delete_registers(path)
        except: pass
        response = make_response(redirect('/registers'))
    return response

# em produção
@app.route('/registers/v/<path:path>', methods = ('GET', 'POST'))
def view_registers(path):
    user = session.get('user')
    if user == None: response = make_response(redirect('/sing-in'))
    elif request.method == 'GET': response = make_response(render_template('details_regist.html',user=user, data=DB.get_data_by_id(path)))
    else:
        date = request.form['date']
        title = request.form['title']
        detais = request.form['detais']
        value = request.form['value']
        _type = request.form['type']
        try: float(value)
        except: response = 'value deve ser um número'
        else: DB.update_regist(path, date, title, detais, value, _type)
        response = make_response(redirect('/registers/v/%s' %path))
    return response

# Rota do caixa
# @app.route('/box')
# def box():
#     user = session.get('user')
#     if user == None: response = make_response(redirect('/sing-in'))
#     else: response = render_template('box/main_page.html', user = user)
#     return response

# Rotas de autenticação
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

# rotas auxiliares
@app.route('/image/<path:path>')
def send_image(path):
    return send_from_directory('static/image', path)
    
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)