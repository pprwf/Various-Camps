'''จันทร์อังคารพุธพฤหัสศุกร์เสาร์อาทิตย์'''

def everyday():
    '''ได้คุยไม่ได้คบนี่ใครเอ่ย อ่อ เราเอง'''
    sec = int(input())
    day = sec // 86400
    hour = (sec % 86400) // 3600
    minute = ((sec % 86400) % 3600) // 60
    second = ((sec % 86400) % 3600) % 60
    print("%02d:%02d:%02d:%02d" %(day, hour, minute, second))
everyday()
