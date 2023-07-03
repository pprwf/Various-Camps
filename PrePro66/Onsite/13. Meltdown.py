'''Meltdown'''

def melt(temp, time, die="Good b...", alive="Phew!!!"):
    '''Meltdown'''
    for _ in range(time):
        temp -= int(input()) * 10
    print(die if temp >= 25 else alive)
melt(float(input()), int(input()))
