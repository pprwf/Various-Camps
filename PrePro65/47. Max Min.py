'''ขอร้องเลย'''
def ismx(xx1, xx2):
    '''MAX'''
    return xx1 * (xx1 >= xx2) + xx2 * (xx2 > xx1)

def ismn(xx1, xx2):
    '''MIN'''
    return xx1 * (xx1 <= xx2) + xx2 * (xx2 < xx1)

def analyse():
    '''analysis'''
    mxmn = input().upper()
    num1, num2 = int(input()), int(input())
    if mxmn == "MAX":
        num3 = ismx(ismx(num1, num2), int(input()))
        num4 = ismx(num3, int(input()))
        num5 = ismx(num4, int(input()))
        print("MAX :", num5)
    else:
        num3 = ismn(ismn(num1, num2), int(input()))
        num4 = ismn(num3, int(input()))
        num5 = ismn(num4, int(input()))
        print("MIN :", num5)
analyse()
