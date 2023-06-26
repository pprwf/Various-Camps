'''find("Min\\Max")'''

def checking(want, num, count=2):
    '''calculating'''
    new = int(input())
    if want == "MAX":
        num = new if num < new else num
    elif want == "MIN":
        num = new if num > new else num
    if count == 5:
        return want, num
    else:
        want, num = checking(want, num, count + 1)
        return want, num

def calc():
    '''find("Min\\Max")'''
    want, num = checking(input(), int(input()))
    print("MAX :" if want == "MAX" else "MIN :", num)
calc()
