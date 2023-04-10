"""Thai"""

def thai_num():
    '''number'''
    thai = input()
    if thai == "N":
        country = input()
    age = int(input())
    coupon = input()
    if age <= 10 or age > 60:
        print("0.00")
    elif age > 10 and age <= 20 and thai == "Y":
        price = 20
        if coupon == "Y":
            percent = int(input())
            price = ((price * (100 - percent)) / 100)
        print("%.2f" %price)
    elif age > 20 and thai == "Y":
        price = 40
        if coupon == "Y":
            percent = int(input())
            price = ((price * (100 - percent)) / 100)
        print("%.2f" %price)
    elif age > 10 and age <= 20 and thai == "N":
        price = 100
        if country == "Vietnam" or country == "Singapore" or country == "India":
            price /= 2
        if coupon == "Y":
            percent = int(input())
            price = ((price * (100 - percent)) / 100)
        print("%.2f" %price)
    elif age > 20 and thai == "N":
        price = 200
        if country == "Vietnam" or country == "Singapore" or country == "India":
            price /= 2
        if coupon == "Y":
            percent = int(input())
            price = ((price * (100 - percent)) / 100)
        print("%.2f" %price)
thai_num()
