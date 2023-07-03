'''Composite Function'''

def ffunc(num):
    '''g'''
    return (15 + num - num ** 3) / (num ** 2 / 3 + 11)

def gfunc(num):
    '''f'''
    return num ** 3 + 4 * num - 1

def comp(num, func):
    '''main func'''
    print("%.2f" %(ffunc(gfunc(num)) if func == "fog" else\
                    gfunc(ffunc(num)) if func == "gof" else None))
comp(float(input()), input().lower())
