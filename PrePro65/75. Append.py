'''append'''

def lis(num):
    '''append'''
    while not num > 0:
        num = int(input())
    appe = []
    for _ in range(num):
        appe.append(input())
    print("[", end="")
    for i in appe:
        if i != appe[len(appe) - 1]:
            print('"%s",' %i, end=" ")
        else:
            print('"%s"]' %i, end="")
    print()
lis(int(input()))
