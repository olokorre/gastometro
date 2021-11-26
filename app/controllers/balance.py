from app import app
from flask import request
from ..controllers import controller
from ..databases import balance

def createRegister():
    date = request.form['date']
    title = request.form['title']
    description = request.form['description']
    type = request.form['type']
    _class = request.form['class']
    value = request.form['value']
    balance.createRegister(date, title, description, type, _class, value)
    return controller.success('Nice')