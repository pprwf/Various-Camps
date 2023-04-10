'''Ranking'''

def rank():
    '''rank'''
    inp = [int(i) for i in input().split(",")]
    sort = sorted(inp)
    sort.reverse()
    lis = []
    for i in inp:
        lis.append(sort.index(i) + 1)
    for i in range(len(lis)):
        print(lis[i], end="")
        if i != len(lis) - 1:
            print(",", end="")
    print()
rank()
