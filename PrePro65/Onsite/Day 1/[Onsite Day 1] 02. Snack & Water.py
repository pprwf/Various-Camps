'''เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ'''

def snack():
    '''อยากเป็นแฟนเธอ ไม่ได้อยากเป็นชู้'''
    money = float(input())
    if money < 0:
        money = 0
    water = float(input())
    if water < 0:
        water = 0
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    remain = money - water
    mod = remain % 3
    for i in range(0, 4):
        price = [10, 15, 20]
        if mod == i:
            snack1 = price[i] * val1
            mod = remain - snack1
            break
    for i in range(0, 4):
        price = [12, 15, 18]
        if mod % 3 == i:
            snack2 = price[i] * val2
            mod -= snack2
            break
    for i in range(0, 4):
        price = [5, 7, 9]
        if mod % 3 == i:
            snack3 = price[i] * val3
            break
    remain -= snack1 + snack2 + snack3
    if remain < 0:
        print("Now you have %d left.\nYou don't have enough money!" %money)
    else:
        print("Now you have %d left.\nHere's your order!\nWater: %d baht\n\
Snack number 1: %d baht\nSnack number 2: %d baht\nSnack number 3: %d baht" \
%(remain, water, snack1, snack2, snack3))
snack()
