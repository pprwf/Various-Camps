'''Peterpan'''

def outer(length):
    '''outside'''
    for i in range(1, length):
        if i % 3 == 0:
            print("..◊.", end="")
        else:
            print("..♦.", end="")
    print(".\n", end="")

def inner(length):
    '''inside'''
    for i in range(1, length):
        if i % 3 == 0:
            print(".◊.◊", end="")
        else:
            print(".♦.♦", end="")
    print(".\n", end="")

def frame(txt):
    '''PeterPanFrame'''
    length = len(txt) + 1
    outer(length)
    inner(length)
    time = 0
    print("♦", end="")
    for i in txt:
        time += 1
        print(".%s." %i, end="")
        if time % 3 == 0:
            print("◊", end="")
        else:
            print("♦", end="")
    print()
    inner(length)
    outer(length)
frame(input())
