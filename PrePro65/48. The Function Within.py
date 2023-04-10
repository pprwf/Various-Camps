'''The Evil Within'''
def ffunc(vari):
    '''f(x) = 2x'''
    return vari * 2

def gfunc(vari):
    '''g(x) = 3x^4 - x^3 + 2x^2 + 10'''
    return 3 * (vari ** 4) - vari ** 3 + 2 * (vari ** 2) + 10

def hfunc(vari1, vari2, vari3):
    '''h(x, y, z) = (z + x)^2 - xy + y^2'''
    return (vari3 + vari1) ** 2 - vari1 * vari2 + vari2 ** 2

def ifunc(vari1, vari2, vari3, vari4):
    '''i(a, b, c, d) = (a^2 + b^2 - c^2) / (d^2 - 2ad + 2a)'''
    return (vari1 ** 2 + vari2 ** 2 - vari3 ** 2) / (vari4 ** 2 - 2 * vari1 * vari4 + 2 * vari1)

def main():
    '''main'''
    real1, real2, real3, real4 = float(input()), float(input()), float(input()), float(input())
    print(ffunc(ffunc(real1)))
    print(gfunc(ffunc(real1 - real2)))
    print(hfunc(ffunc(real1 + real2), ffunc(real1 + real3), gfunc(ffunc(real4 ** 2))))
    print(ifunc(hfunc(ffunc(real1 + real2), ffunc(real1 - real3)\
, gfunc(ffunc(real4 ** 2))), gfunc(ffunc(real1 - real2))\
, ffunc(ffunc(ffunc(ffunc(ffunc(real3))))), real4 ** 8))
main()
