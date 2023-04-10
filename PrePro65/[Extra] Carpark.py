'''Carpark'''

def duration(startdate, starttime, stopdate, stoptime):
    '''ช่วงเวลาการจอดรถ'''
    timediff = (stoptime - starttime) + (stopdate - startdate) * 24
    datediff = timediff // 24
    timediff %= 24
    if startdate > stopdate or starttime >= 24 or stoptime >= 24 or \
    starttime < 0 or stoptime < 0 or startdate > 365 or stopdate > 365 or \
    startdate < 1 or stopdate < 1 or timediff < 0 or \
    datediff < 0 or datediff > 365:
        return "error"

def price(datediff, timediff):
    '''ราคา'''
    if datediff == 0:
        if timediff <= 2:
            cost = 0
        elif timediff <= 12 and timediff > 2:
            cost = timediff * 15
        else:
            cost = 200
    else:
        cost = datediff * 200
        if timediff <= 2:
            cost += 0
        elif timediff <= 12 and timediff > 2:
            cost += timediff * 15
        else:
            cost += 200
        if (datediff // 28) >= 1:
            cost -= 500
        if (datediff // 7) >= 1:
            cost -= (datediff // 7) * 300
    print("%d day %d hour" %(datediff, timediff))
    print("%d baht" %cost)

def parking():
    '''parking'''
    startdate = int(input())
    starttime = int(input())
    stopdate = int(input())
    stoptime = int(input())
    timediff = (stoptime - starttime) + (stopdate - startdate) * 24
    datediff = timediff // 24
    timediff %= 24
    durat = duration(startdate, starttime, stopdate, stoptime)
    if durat != "error":
        price(datediff, timediff)
    else:
        print("error")
parking()
