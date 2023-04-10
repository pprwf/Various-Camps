'''Soft Drink'''

def invalid(prefer, drinkings):
    '''invalid'''
    if len(prefer) == 0:
        return 0
    else:
        con2, con3 = prefer[-1] != "ice", prefer[0] == "ice"
        for i in range(len(prefer)):
            if con2 or con3 or prefer[i] not in drinkings:
                return 0

def drinks():
    '''hard'''
    drinkings = ["orange", 17, "banana", 13, "strawberry", 10, "cherrie", 15, \
    "watermelon", 12, "lemon", 19, "mango", 21, "grape", 11, "coke", 15, "pepsi", 15, \
    "sprite", 15, "fanta", 15, "ice", 5]
    soft_drinks = ["coke", 15, "pepsi", 15, "sprite", 15, "fanta", 15]
    prefer = []
    inp = input().lower()
    soft = ""
    total = 5
    if inp != "cup" or inp == "end":
        pass
    else:
        while inp != "end":
            inp = input().lower()
            prefer.append(inp)
            if inp in soft_drinks:
                soft = inp
        prefer.pop()
    inv = invalid(prefer, drinkings)
    if inv == 0:
        print("Invalid order!")
        return
    if soft in soft_drinks:
        print("Here's your soft drink!")
    else:
        print("Here's your juice!")
    for i in range(len(prefer)):
        for j in range(len(drinkings)):
            if prefer[i] == drinkings[j]:
                total += int(drinkings[j + 1])
    print("Cost %d baht." %total)
drinks()
