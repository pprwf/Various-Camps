'''xbox'''

def xbox(size):
    '''xbox'''
    for row in range(1, size + 1):
        for col in range(1, size + 1):
            con1 = row == col
            con2 = (col == size and row == 1) or (row == size and col == 1)
            con3 = row + col == size + 1
            con4 = row == 1 or row == size or col == 1 or col == size
            if con1 or con2 or con3 or con4:
                print("*", end=" ")
            else:
                print("", end="  ")
        print()
xbox(int(input()))
