'''Stair'''

def stair():
    '''alphabet stair'''
    alpha = input().upper()
    for col in range(65, ord(alpha) + 1):
        for row in range(65, col + 1):
            print(chr(row), end=" ")
        print("")
stair()
