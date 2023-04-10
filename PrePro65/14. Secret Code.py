'''Secret Code'''

def spy():
    '''246810'''
    code = int(input())
    first = str((code // 100000000) % 10)
    second = str((code // 1000000) % 10)
    third = str((code // 10000) % 10)
    fourth = str((code // 100) % 10)
    five = str((code // 1) % 10)
    print(first + second + third + fourth + five)
spy()
