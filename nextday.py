
def next_day(year, month, day):
    if month > 12 or day > 31 or year < 1500 or month <= 0 or day <= 0:     #leap years started in the year 1500 so the years before will not be taken into account
        return None
    
    thirty = [4,6,9,11]

    if month == 2:
        if year%4 == 0 and day == 28:
            day += 1
        elif year%4 == 0 and day == 29:
            month += 1
            day = 1
        elif year%4 == 0 and day > 29:
            return None
        elif day == 28:
            month += 1
            day = 1
        elif day > 28:
            return None
        else:
            day += 1

    elif month in thirty:
        if day == 30:
            month += 1
            day = 1
        elif day > 30:
            return None
        else:
            day += 1
    elif day == 31:
        if month == 12:
            year += 1
            month = 1
            day = 1
        else:
            month += 1
            day = 1
    else:
        day += 1
    date = str(year) + '-' + str(month) + '-' + str(day)
    return date

print(next_day(2021, 8, 31))