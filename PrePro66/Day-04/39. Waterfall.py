'''เลขไทยมีประโยชน์'''

def thainum(thai, price=200):
    '''เลขไทยมีประโยชน์'''
    nation, age, coupon = thai == "N" and input(), int(input()), input()
    percent = coupon == "Y" and int(input())
    price //= 2 if nation in ("Vietnam", "Singapore", "India") else 5 if thai == "Y" else 1
    price *= (100 - percent) / 100 if coupon == "Y" else 1
    price = 0 if age <= 10 or age > 60 else price // 2 if 10 < age <= 20 else price
    print("%.2f" %price)
thainum(input())
