'''hourglass'''

def glass(size):
    '''hourglass'''
    for row in range(1, size * 2 + 4):
        for col in range(1, size * 2 + 2):
            con1 = row == 1 or row == size * 2 + 3
            con2 = row == size + 2 and col == size + 1
            con3 = row - 1 == col
            con4 = row + col == size * 2 + 3
            if con1 or con2 or con3 or con4:
                print("*", end="")
            else:
                print("", end=" ")
        print("")
glass(int(input()))
