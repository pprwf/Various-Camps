'''Matrix'''

def matrix():
    '''matrix'''
    row = int(input())
    col = int(input())
    for i in range(1, row + 1):
        for j in range(i, (col * i) + 1, i):
            print(j, end=" ")
        print("")
matrix()
