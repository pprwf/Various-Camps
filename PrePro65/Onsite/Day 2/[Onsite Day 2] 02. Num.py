'''ตัวเลขที่มีอยู่'''

def number(length):
    '''num'''
    if length == 0:
        print("No Tape Measure")
        return
    num = []
    add = 0
    while True:
        txt = input()
        if txt == "No more!":
            break
        if txt.isnumeric():
            if int(txt) > length:
                continue
            num.append(txt)
    for i in num:
        add += int(i)
    if add == 0:
        print("Not Found Number")
    else:
        print("Sum of Found Number =", add)
number(int(input()))
