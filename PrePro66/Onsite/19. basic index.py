'''basic index'''

def base_index(inp):
    '''index'''
    lis = []
    while inp.lower() != "end":
        lis.append(inp)
        inp = input()
    ind = int(input())
    print("List[%d] = \"%s\"" %(ind, lis[ind]) if len(lis) - 1 >= ind else "Index Not Found")
base_index(input())
