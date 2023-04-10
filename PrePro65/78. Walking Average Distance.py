'''walking'''

from math import ceil

def walk(date):
    '''DocString'''
    lis = []
    if not 0 < date <= 10000:
        date = 1
    for _ in range(date):
        step = int(input())
        if step < 0:
            step = 0
        lis.append(step)
    avg = sum(lis) / len(lis)
    for i in lis:
        if i >= avg:
            print(ceil(i - avg))
        else:
            print(ceil(avg - i))
walk(int(input()))
