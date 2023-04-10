'''Geometric'''

def geometric():
    '''arithmetic'''
    first = float(input())
    member = int(input())
    samediff = float(input())
    for _ in range(member):
        print("%.2f" %first, end=" ")
        first *= samediff
geometric()
