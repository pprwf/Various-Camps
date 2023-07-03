'''Pathfinder'''

def travel(txt):
    '''Pathfinder'''
    txt = [i for i in txt if 4 <= len(i) <= 8]
    print(*[i + " " + str(len(i)) for i in sorted(txt, key=len)], sep="\n")
travel(input().split(", "))
