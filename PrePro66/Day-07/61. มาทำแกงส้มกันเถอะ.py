'''มาทำแกงส้มกันเถอะ'''

def cooking(ingredient, price=0, quantity=0, special=0):
    '''gangsom the star'''
    while ingredient != "stop":
        if ingredient == "shrimp sour soup":
            price += 80
        elif ingredient == "mixed vegetables sour soup":
            price += 60
        elif ingredient == "papaya sour soup":
            price += 55
        elif ingredient == "mixed vegetables sour soup":
            price += 60
        else:
            price += 100
        quantity += 1
        ingredient = input()
    if quantity >= 3 and price >= 200:
        special = price - price * 85 / 100
    print("Original Price %d baht\nDiscount %d baht\nTotal %d baht"\
        %(price, special, price - special))
cooking(input())
