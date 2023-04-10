'''sum'''

def ssum():
    '''sum'''
    total = 0
    for inp in range(10):
        inp = int(input())
        if inp < 0:
            inp = -5
        total += inp
    if total < 0:
        total = -5
    print(total)
ssum()
