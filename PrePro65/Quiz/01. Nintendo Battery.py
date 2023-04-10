'''Batter'''
from math import floor

def bat(percent):
    '''battery'''
    wide = int(input())
    if wide % 2 != 0:
        wide += 1
    value = floor(wide / 100 * percent)
    print("(" + ("O" * value) + ("_" * (wide - value)) + ") {}%".format(percent))
bat(int(input()))
