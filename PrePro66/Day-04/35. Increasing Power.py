'''Increasing Power'''

def dragon_ball(origin, power, timer):
    '''super saiyan'''
    new_power = origin + power * timer
    if power > 100000:
        print("I can FEEL it...")
    if new_power > 100000000:
        print("NOW I'M MAD!!!!")
    elif new_power < 0:
        print("Where am I..?")
    elif new_power < 10000:
        print("Sorry... dad...")
    else:
        print(new_power)
dragon_ball(int(input()), int(input()), int(input()))
