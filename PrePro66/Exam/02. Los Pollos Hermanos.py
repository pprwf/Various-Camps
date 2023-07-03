'''Los Pollos Hermanos'''

def fry(food, price=0):
    '''Los Pollos Hermanos'''
    lis, menu = [],\
        ["Chicken S", "Chicken M", "Chicken L", "Chicken XL", "Chicken XXL", "French Fries", "Coke"]
    while food != "stop":
        lis.append(food)
        food = input()
    for i in lis:
        price += 20 if i == menu[0] else 45 if i == menu[1] else 85 if i == menu[2]\
        else 150 if i == menu[3] else 250 if i == menu[4]\
        else 20 if i == menu[5] else 10 if i == menu[6] else 0
    price -= 0 if price < 299 else price * 30 / 100 if price >= 599 else price * 10 / 100
    print("Cost : %d Baht" %price)
    for i in lis:
        print(i if i in menu else "Error: %s not found" %i)
fry(input())
