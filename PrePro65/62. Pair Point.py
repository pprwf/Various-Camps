'''Pair'''

def shabu():
    '''Yak gin shabu P' Nick leang noi'''
    column, row = int(input()), int(input())
    for i in range(1, column + 1):
        for j in range(1, row + 1):
            print("(%d, %d)" %(i, j), end=" ")
        print("")
shabu()
