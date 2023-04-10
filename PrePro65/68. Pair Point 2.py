'''Pair'''

def pair():
    '''point'''
    num = int(input())
    for col in range(num, -num - 1, -1):
        for row in range(num, -num - 1, -1):
            print("(%02d, %02d)" %(abs(col), abs(row)), end=" ")
        print("")
pair()
