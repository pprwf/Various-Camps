'''list index'''

def index():
    '''index'''
    lis = []
    while True:
        txt = input()
        if txt.lower() == "end":
            break
        else:
            lis.append(txt)
    posit = int(input())
    if posit < len(lis):
        print('List[%d] = "%s"' %(posit, lis[posit]))
    else:
        print("Index Not Found")
index()
