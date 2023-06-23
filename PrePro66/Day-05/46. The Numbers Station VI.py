'''The Numbers Station VI'''

def numstate(num):
    '''The Numbers Station VI'''
    if num < 0:
        print("Negative numbers aren't allowed.")
    elif num in range(1, 7):
        print("A" if num == 1 else "E" if num == 2 else "I" if num == 3\
        else "N" if num == 4 else "O" if num == 5 else "T")
    elif num in range(90, 100) or num == 0:
        print("Not an alphabet")
    elif num in range(70, 90):
        print(chr(num - 4) if num in range(73) else chr(num - 3)\
            if num in range(76) else chr(num - 2) if num in range(80)\
            else chr(num) if num in range(84) else chr(num + 1))
    else:
        print("Unknown")
numstate(int(input()))
