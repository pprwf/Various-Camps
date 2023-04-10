'''math'''

def math():
    '''math'''
    allnum = int(input())
    lis = []
    for _ in range(abs(allnum)):
        lis.append(int(input()))
    newlist = []
    mult = float(input())
    for i in lis:
        i *= mult
        string = "%.2f" %i
        newlist.append(string)
    print(newlist)
math()
