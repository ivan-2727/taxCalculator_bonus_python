from flask import Flask, request
from congestion_tax_calculator import get_tax
from vehicle import Vehicle
from date_time import date_time
from mongoTaxRules import mongoTaxRules
from localTaxRules import localTaxRules
import re
import json
import os
from helpers import convert

taxRules = mongoTaxRules() if os.environ['FLASK_ENV'] == "production" else localTaxRules()

app = Flask(__name__)
@app.route('/', methods=['POST'])
def result():
    data = request.get_json() 
    res = []
    for oneData in data:
        vehicle = Vehicle(oneData['vehicle'])
        dates = [convert(usualDate) for usualDate in oneData['dates']]
        tax = get_tax(vehicle, dates, taxRules)
        res.append(tax)
        
    return json.dumps(res, separators=(',', ':'))
