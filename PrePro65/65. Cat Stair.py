'''Cat'''

def stair():
    '''cat stair'''
    stp = int(input())
    for row in range(stp):
        for col in range(stp):
            if row > col:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        print("")
stair()
