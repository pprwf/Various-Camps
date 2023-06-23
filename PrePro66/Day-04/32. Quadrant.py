'''Quadrant'''

def quadrant(pointx, pointy):
    '''Quadrant'''
    if pointx == 0 or pointy == 0:
        print("on the axis")
    elif pointx > 0 and pointy > 0:
        print("1")
    elif pointx < 0 and pointy < 0:
        print("3")
    elif pointx > 0 and pointy < 0:
        print("4")
    else:
        print("2")
quadrant(float(input()), float(input()))
