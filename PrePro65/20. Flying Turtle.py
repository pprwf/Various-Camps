'''Tao Bin'''
from math import ceil

def milk_tea():
    '''อยากกินชานม'''
    paid = float(input())
    price = float(input())
    change = paid - price
    maximum = change / 0.25
    minimum = (change // 10) + ((change % 10) // 5) + ceil((change % 10) / 2)
    minimum += ((change % 10) % 0.5) + ((change % 10) % 0.25)
    print("%d\n%d\n%.1f" %(maximum, minimum, change))
milk_tea()
