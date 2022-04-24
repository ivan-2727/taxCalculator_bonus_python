#seems to work for all years, not only 2013

#days in each month for a non-leap year
dim = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

#make prefix sum for a non-leap year
prsum_usual = []
d = 0
for i in range(12):
    d += dim[i]
    prsum_usual.append(d)

#make prefix sum for a leap year
prsum_leap = []
d = dim[0]
prsum_leap.append(d)
d += 1
for i in range(1,12):
    d += dim[i]
    prsum_leap.append(d)

def weekday_by_prsum(prsum, year, month, day) -> int:
    #2013 as reference, others shifted
    shift = 0
    if year >= 2013:
        shift = year - 2013 + (year - 2013)//4
    else:
        shift = -(2013 - year) - (2016 - year)//4
    if month == 0:
        return ((day + shift) % 7)
    return ((prsum[month-1] + day + shift) % 7) 

class date_time:  

    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
     
    def weekday(self) -> int:
        if abs(self.year - 2012)%4 == 0:
            return weekday_by_prsum(prsum_leap, self.year, self.month, self.day)
        return weekday_by_prsum(prsum_usual, self.year, self.month, self.day)

    def timestamp(self) -> int:
        #the beginning of 2013 is zero
        new_days = self.day-1
        if self.month > 0:
            if abs(self.year - 2012)%4 == 0:
                new_days += prsum_leap[self.month-1]
            else:
                new_days += prsum_usual[self.month-1]
        
        prev_days = 0
        if self.year >= 2013:
            prev_days = ((self.year - 2013)//4)*prsum_leap[11] + ((self.year - 2013) - (self.year - 2013)//4)*prsum_usual[11]
        else:
            prev_days = -((2016-self.year)//4)*prsum_leap[11] - ((2013 - self.year) - (2016-self.year)//4)*prsum_usual[11]

        return (new_days+prev_days)*24*60*60 + self.hour*60*60 + self.minute*60 + self.second

# for i in range(2005,2020):
#     print(i, date_time(i, 0, 1, 0, 0, 0).weekday())

# start 1356998400
# print(date_time(2005, 6, 13, 1, 2, 3).timestamp())
