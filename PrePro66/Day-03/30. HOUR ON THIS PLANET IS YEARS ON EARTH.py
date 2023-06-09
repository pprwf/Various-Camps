'''HOUR ON THIS PLANET IS YEARS ON EARTH.'''

def time(minute):
    '''HOUR ON THIS PLANET IS YEARS ON EARTH.'''
    txt = str(minute) + " Minute"
    if minute > 1:
        txt += "s"
    txt += " here is "
    year, month = round(minute / 60 * 84 // 12), round(minute / 60 * 84 % 12)
    if year >= 1:
        txt += str(year) + " Years" if year > 1 else str(year) + " Year"
        if month > 0:
            txt += " and "
    if month >= 1:
        txt += str(month) + " Months" if month > 1 else str(month) + " Month"
    print(txt + " on Earth.")
time(int(input()))
