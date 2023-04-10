'''Cake'''

def chocolate():
    '''Chocolate Cake'''
    money = int(input())
    cost = int(input())
    if money >= cost:
        print("Chocolate Cake:", money // cost)
    else:
        print("Not enough money;(")
    print("Money left:", money % cost)
chocolate()
