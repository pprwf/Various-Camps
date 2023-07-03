'''Binary Twist'''

def binary(bit, prefer):
    '''Binary Twist'''
    if bit.count("1") % 2 == 0:
        if prefer == "Even":
            print(bit + "0")
        else:
            print(bit + "1")
    else:
        if prefer == "Even":
            print(bit + "1")
        else:
            print(bit + "0")
binary(input(), input())
