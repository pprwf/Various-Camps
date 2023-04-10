'''Mookrob'''

def hungry():
    '''หิวข้าว'''
    money = float(input())
    price_check = 99999999999
    for i in range(1, 11):
        for _ in range(1, 6):
            price = float(input())
            if money >= price:
                paid = price
                store = i
                break
            elif price <= price_check:
                price_check = price
                that_store = i
        if money >= price:
            print("%.2f\n%d" %(paid, store))
            break
        if i == 10:
            print("%.2f\n%d" %(price_check, that_store))
hungry()
