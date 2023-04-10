'''Equation'''

def equation():
    '''สมการ'''
    abcd = int(input())
    bcde = int(input())
    cdef = int(input())
    defg = int(input())
    efgh = int(input())
    fghi = int(input())
    result = (bcde / (abcd ** 2 / defg) + efgh * (bcde / abcd)) * fghi / (fghi * cdef)
    print("%.2f" %result)
equation()
