'''choose a book'''
from math import factorial as fact

def book():
    '''Book'''
    num = int(input())
    rnd = int(input())
    print("%d" %(fact(num) / (fact(rnd) * fact(num - rnd))))
book()
