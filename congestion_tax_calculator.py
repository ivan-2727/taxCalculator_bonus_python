from date_time import date_time
from vehicle import Vehicle
from functools import cmp_to_key as ctk
from helpers import comp

def get_tax(vehicle: Vehicle, dates: list, taxRules):

    time_zones = taxRules["time_zones"]
    free_vehicles = taxRules["free_vehicles"]
    free_dates = taxRules["free_dates"]

    if vehicle.get_vehicle_type().upper() in free_vehicles:
        return 0
    
    dates.sort(key=ctk(comp))

    dates = [date for date in dates if not is_toll_free_date(date, free_dates)]

    #start of 60min interval
    start_index = 0
    start_time = dates[0].timestamp()

    start_day_time = start_time
    daily_fee = 0

    total_fee = 0

    for i in range(len(dates)):

        time = dates[i].timestamp()

        if time - start_time > 3600:
            interval_fee = 0
            for j in range(start_index, i):
                interval_fee = max(get_toll_fee(dates[j], time_zones), interval_fee)
            if daily_fee + interval_fee <= 60:
                total_fee += interval_fee
                daily_fee += interval_fee
            else:
                total_fee += 60 - daily_fee
                daily_fee = 60
                
            start_time = time
            start_index = i 

        if time - start_day_time > 86400:
            daily_fee = 0 
            start_day_time = time
        
    
    interval_fee = 0
    for j in range(start_index, len(dates)):
        interval_fee = max(get_toll_fee(dates[j], time_zones), interval_fee)
    if daily_fee + interval_fee <= 60:
        total_fee += interval_fee
        daily_fee += interval_fee
    else:
        total_fee += 60 - daily_fee
        daily_fee = 60

    return total_fee

def get_toll_fee(date: date_time, time_zones : list) -> int:

    t = date.hour*3600 + date.minute*60 + date.second

    for zone in time_zones:
        if zone['start'] <= zone['end']:
            if t >= zone["start"] and t <= zone["end"]:
                return zone["price"]
        else:
            if t >= zone["start"] or t <= zone["end"]:
                return zone["price"]
    
    return 0

def is_toll_free_date(date: date_time, free_dates):
    year = date.year
    month = date.month
    day = date.day

    if date.weekday() == 5 or date.weekday() == 6:
        return True

    if str(year) in free_dates:
        if day in free_dates[str(year)][month-1]:
            return True
        if len(free_dates[str(year)][month-1]) > 0:
            if free_dates[str(year)][month-1][0] == -1:
                return True
    
    return False



 
