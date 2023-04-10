'''pager'''

def pager(text):
    '''pager'''
    length = len(text) // 20
    remain = len(text) % 20
    cost = length * 18.5
    length = remain // 8
    remain = remain % 8
    cost += length * 6.5
    length = remain // 3
    remain = remain % 3
    cost += length * 3
    cost += remain * 1.5
    print("Text's length is : \"%d\"" %len(text))
    print("Total price is   : %.2f Baht\\.-" %cost)
pager(input())
