'''Itim Cone'''

from math import pi

def icecream(height, radius):
    '''icecream'''
    print("Cone area is %.4f" %(pi * radius * height + pi * radius ** 2))
icecream(float(input()), float(input()))
