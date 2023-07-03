'''Thrust'''

def pystar(planet, distance):
    '''rocket propulsion'''
    print((5.972e+24 * (planet == "earth") +\
        6.39e+23 * (planet == "mars") +\
        1.898e+27 * (planet == "jupiter")) * distance / 10000)
pystar(input(), float(input()))
