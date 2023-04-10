'''math'''

def math(num):
    '''math'''
    if num < 1:
        num = 1
    allnum = []
    allnum.append(num)
    while True:
        txt = input()
        if txt == "+":
            print("%.2f" %sum(allnum))
            break
        elif txt == "-":
            sub = allnum[0] - allnum[1]
            for i in range(2, len(allnum)):
                sub -= allnum[i]
            print("%.2f" %(sub))
            break
        elif txt == "*":
            mul = allnum[0] * allnum[1]
            for i in range(2, len(allnum)):
                mul *= allnum[i]
            print("%.2f" %(mul))
            break
        elif txt == "/":
            div = allnum[0] / allnum[1]
            for i in range(2, len(allnum)):
                div /= allnum[i]
            print("%.2f" %(div))
            break
        else:
            allnum.append(float(txt))
math(float(input()))
