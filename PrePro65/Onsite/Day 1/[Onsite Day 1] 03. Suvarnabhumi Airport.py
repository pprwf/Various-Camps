'''Suvarnabhumi Airport'''

def timezone(desti, hour, minute, time):
    '''change time'''
    if hour == 12 and time == "AM":
        hour = 0
    if desti == "SYD":
        hour += 12
    elif desti == "SGN":
        hour += 1
        minute += 50
    elif desti == "ATL":
        hour += 9
        minute += 55
    elif desti == "YVR":
        hour += 2
        minute += 20
    elif desti == "KTM":
        hour += 12
        minute -= 15
    return hour, minute

def airport():
    '''time'''
    input()
    gmt = input().upper()
    time = input().upper()
    desti = gmt[-4:-1]
    print("BKK -", desti)
    hour, minute = timezone(desti, int(time[:2]), int(time[3:5]), time[-2:])
    if time[-2:] == "PM" and hour != 24:
        hour += 12
    if hour >= 24:
        hour %= 24
    if minute >= 60:
        hour += minute // 60
        minute %= 60
    if minute < 0:
        minute += 60
        hour -= 1
    if hour >= 12 or hour < 0 and time[-2:] == "PM":
        hour %= 12
        if hour <= 0:
            hour += 12
        suffix = "PM"
    else:
        if hour == 0:
            hour = 12
        suffix = "AM"
    print("%02d:%02d" %(hour, minute), suffix)
airport()
