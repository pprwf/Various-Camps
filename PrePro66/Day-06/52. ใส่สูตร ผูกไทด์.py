'''ใส่สูตร ผูกไทด์'''

def ffunc(num):
    '''f function'''
    return (num ** 2 + 2) * 7

def gfunc(num, num2):
    '''g function'''
    return 3 * (num + num2) * 2 + 4

def hfunc(num, num2, num3):
    '''h function'''
    return (num + num2) / num3 + num3 / num2

def ifunc(num, num2, num3, num4):
    '''i function'''
    return (num * num3 + num4 * num2) ** 2 / (num3 ** 2 * num4 ** 2 * 10)

def function(avar, bvar, cvar):
    '''ใส่สูตร ผูกไทด์'''
    print("x1 : %s\nx2 : %s\nx3 : %s\nx4 : %s" %(ffunc(avar), gfunc(ffunc(bvar), avar),\
        hfunc(ffunc(gfunc(avar + bvar, cvar)), gfunc(ffunc(cvar + bvar), cvar),\
        ffunc(bvar + cvar)), ifunc(gfunc(ffunc(gfunc(avar + bvar, cvar)), hfunc(gfunc(bvar + cvar,\
        ffunc(gfunc(bvar, cvar + avar))), cvar, avar + bvar)), gfunc(ffunc(cvar + bvar),\
        bvar * avar), ffunc(cvar), gfunc(ffunc(ffunc(avar)), cvar))))
function(float(input()), float(input()), float(input()))
