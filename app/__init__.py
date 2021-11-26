from flask import Flask
from decouple import config
import mysql.connector

app = Flask(__name__)
app.secret_key = config('SECRET_KEY')
db = mysql.connector.connect(
    user=config('USER_DB'),
    passwd=config('PASSWD_DB'),
    db=config('DB'),
    host='dados.com'
)
cursor = db.cursor()


from .routes import index, balance
from .controllers import controller, balance
from .databases import balance