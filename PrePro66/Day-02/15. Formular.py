'''Changon's Formular'''

def new(avar, bvar, cvar):
    '''new formular'''
    print("x1 : " + str((- avar * bvar + avar) / (2 * cvar) + avar ** 2))
    print("x2 : " + str((avar * bvar + avar) / (2 * cvar) - avar ** 2))
new(float(input()), float(input()), float(input()))
