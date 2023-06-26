'''Temperature Converter'''

def kelvin(degree):
    '''kelvin'''
    return degree + 273.15

def fahrenheit(degree):
    '''fahrenheit'''
    return degree * 9 / 5 + 32

def rankine(degree):
    '''rankine'''
    return kelvin(degree) * 9 / 5

def convert(degree, unit):
    '''Temperature Converter'''
    if unit[0] == "F":
        degree = (degree - 32) * 5 / 9
    elif unit[0] == "K":
        degree -= 273.15
    elif unit[0] == "R":
        degree = (degree - 491.67) * 5 / 9
    if unit[-1] == "F":
        print("Fahrenheit = %.2f" %fahrenheit(degree))
    elif unit[-1] == "K":
        print("Kelvin = %.2f" %kelvin(degree))
    elif unit[-1] == "R":
        print("Rankine = %.2f" %rankine(degree))
    else:
        print("Celsius = %.2f" %degree)
convert(float(input()), input())
