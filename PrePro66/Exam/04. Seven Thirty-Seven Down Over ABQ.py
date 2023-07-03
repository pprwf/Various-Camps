'''Seven Thirty-Seven Down Over ABQ'''

def plane(radius, stx, sty, ndx, ndy):
    '''Seven Thirty-Seven Down Over ABQ'''
    print("Safe" if ((ndx - stx) ** 2 + (ndy - sty) ** 2) ** 0.5 >= radius * 2 else "Dangerous")
plane(float(input()), float(input()), float(input()), float(input()), float(input()))
