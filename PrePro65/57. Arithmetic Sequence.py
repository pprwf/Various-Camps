'''Arithmetic'''

def arithmetic():
    '''arithmetic'''
    first = int(input())
    member = int(input())
    samediff = int(input())
    for _ in range(member):
        print(first, end=" ")
        first += samediff
arithmetic()
