'''money'''

def money():
    '''ผิดไรวะ'''
    pay = float(input())
    cost = float(input())
    remain = pay - cost
    if (pay - cost) == 0:
        print("จ่ายมาพอดี")
    elif pay < cost:
        print("จำนวนเงินไม่พอ")
    else:
        print("เเบงค์ 100 บาท : %d" %(remain // 100))
        remain %= 100
        print("เเบงค์ 50 บาท : %d" %(remain // 50))
        remain %= 50
        print("เเบงค์ 20 บาท : %d" %(remain // 20))
        remain %= 20
        print("เหรียญ 12 บาท : %d" %(remain // 12))
        remain %= 12
        print("เหรียญ 10 บาท : %d" %(remain // 10))
        remain %= 10
        print("เหรียญ 5 บาท : %d" %(remain // 5))
        remain %= 5
        print("เหรียญ 2 บาท : %d" %(remain // 2))
        remain %= 2
        print("เหรียญ 1 บาท : %d" %(remain // 1))
        remain %= 1
        print("เหรียญ 50 สตางค์ : %d" %(remain // 0.5))
        remain %= 0.5
        print("เหรียญ 25 สตางค์ : %d" %(remain // 0.25))
money()
