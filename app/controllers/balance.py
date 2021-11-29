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

def getRegisters():
    select = balance.getRegisters()
    columns = ['id', 'name', 'description', 'type', 'class', 'value', 'date']
    result = controller.loadJson(columns, select)
    return controller.success('nice', result)

def getBalance():
    result = balance.getBalance()
    return controller.success('cu', {
        'balance': '%s' %result[0][0]
    })