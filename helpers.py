from date_time import date_time
import re

def comp(dateA: date_time, dateB: date_time) -> bool:
    if dateA.year != dateB.year:
        return dateA.year - dateB.year
    if dateA.month != dateB.month:
        return dateA.month - dateB.month
    if dateA.day != dateB.day:
        return dateA.day - dateB.day
    if dateA.hour != dateB.hour:
        return dateA.hour - dateB.hour
    if dateA.minute != dateB.minute:
        return dateA.minute - dateB.minute
    if dateA.second != dateB.second:
        return dateA.second - dateB.second
    return True

def parse(s : str):
    # '–' in Mongo different from the usual '-'
    lst = s.replace('–', ' ').replace('-', ' ').split(' ')
    l = lst[0].split(':')
    r = lst[1].split(':')
    start = 3600*int(l[0])+60*int(l[1])
    end = 3600*int(r[0])+60*int(r[1])+59   
    print([start, end, int(lst[2])])
    return {"start": start, "end": end, "price": int(lst[2])}

def convert(usualDate : str) -> date_time:
    arr = re.split(r'[-\s:]', usualDate)
    return date_time(*[int(x) for x in arr])
