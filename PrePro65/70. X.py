'''x'''

def xnum():
    '''x'''
    odd = int(input())
    if odd % 2 == 0:
        odd -= 1
    for row in range(1, odd + 1):
        for col in range(1, odd + 1):
            con1 = row == col
            con2 = (col == odd and row == 1) or (row == odd and col == 1)
            con3 = row + col == odd + 1
            if con1 or con2 or con3:
                print("*", end=" ")
            else:
                print("", end="  ")
        print()
xnum()
