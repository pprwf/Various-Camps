'''ลองสลับการ์ด แล้วตัดขาดจากใจเธอ'''

def card(swap):
    '''ลองสลับการ์ด แล้วตัดขาดจากใจเธอ'''
    if swap == "12" or swap == "21":
        print("A")
    elif swap == "13" or swap == "31":
        print("B")
    elif swap == "23" or swap == "32":
        print("C")
card(input())
