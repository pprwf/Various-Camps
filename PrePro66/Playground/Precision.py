'''Precision'''

def precision(divider, divisor, pre):
    '''pre'''
    if divisor == 0 and pre < 0:
        print("ZeroDivisionError and Floating point precision can't be lower than 0!")
    elif pre < 0:
        print("Floating point precision can't be lower than 0!")
    elif divisor == 0:
        print("ZeroDivisionError")
    else:
        print("%.*f" %(pre, divider / divisor))

precision(float(input()), float(input()), int(input()))
