'''Late Meeting'''

def fck(hour, minute, sec, unit):
    '''Late Meeting'''
    exmin, exsec = int(input()), int(input())
    minute, sec = (minute + exmin) + (sec + exsec) // 60, (sec + exsec) % 60
    addhour, minute = minute // 60, minute % 60
    if (hour <= 11 and addhour % 24 != 0 and (hour + addhour) % 24 > 11) or\
        (hour == 12 and addhour % 24 > 11):
        if unit == "am":
            unit = "pm"
        elif unit == "pm":
            unit = "am"
    hour += addhour
    if hour > 12:
        hour %= 12
    if hour == 0:
        hour = 12
    print("%02d:%02d:%02d %02s" %(hour, minute, sec, unit))
fck(int(input()), int(input()), int(input()), input())
