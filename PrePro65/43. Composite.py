'''Composite'''

def compo(comp, value):
    '''compo'''
    ffunc = (15 + value - value ** 3) / (value ** 2 / 3 + 11)
    gfunc = value ** 3 + (4 * value) - 1
    if comp == "gof":
        print("%.2f" %(ffunc ** 3 + (4 * ffunc) - 1))
    else:
        print("%.2f" %((15 + gfunc - gfunc ** 3) / (gfunc ** 2 / 3 + 11)))

def func():
    '''fuction'''
    val = float(input())
    ans = input().lower()
    compo(ans, val)
func()
