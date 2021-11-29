from app import app
from flask import render_template, request
from ..controllers import balance

@app.route('/registers', methods=['GET', 'POST'])
def registers():
    if request.method == 'GET': return render_template('registers.html')
    return balance.createRegister()

@app.route('/registers/data')
def registersData():
    return balance.getRegisters()

@app.route('/balance')
def getBalance():
    return balance.getBalance()