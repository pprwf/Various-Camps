'''While_Sum'''

def nonega(num, add=0):
    '''no negative'''
    while num >= 0:
        add += num
        num = int(input())
    print(add)
nonega(int(input()))
