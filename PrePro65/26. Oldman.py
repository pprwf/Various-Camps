'''ผู้สูงอายุกินฟรี'''

def old():
    '''จานแรกกินฟรี'''
    age = int(input())
    dishes = int(input())
    price = 100
    if age >= 60 and dishes <= 1:
        print("Free")
    elif age >= 60 and dishes > 1:
        price -= 50
        print("Pay %d bath" %(price * dishes))
    else:
        print("Pay %d bath" %(price * dishes))
old()
