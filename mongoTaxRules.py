from pymongo import MongoClient
import re
from helpers import parse

def mongoTaxRules():

    client = MongoClient('mongodb+srv://KalleBlomkvist:dd09d84cc1b211ec9d640242ac120002@cluster0.wxbhy.mongodb.net/')
    clcn = client['TaxationRules']['TaxationRules']
    result = dict()

    try:
        result["free_dates"] = clcn.find_one({'name': 'FreeDates'})['data']
        result["free_vehicles"] = clcn.find_one({'name': 'FreeVehicles'})['data']
        time_zones = []
        for s in clcn.find_one({'name': 'TimeZones'})['data']:
            time_zones.append(parse(s))
        result["time_zones"] = time_zones
    except:
        print("ERROR WHILE FETCHING DATA FROM MONGO")
    
    return result

