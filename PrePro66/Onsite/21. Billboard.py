'''Billboard'''

def politic(name):
    '''we have rule'''
    lis = []
    while name != "-1":
        lis.append(name)
        name = input()
    for i in reversed(lis):
        print(i)
politic(input())
