'''Treasure Hunter'''

def planet(temp, grav):
    '''Treasure Hunter'''
    if temp > 100 and grav < 2:
        print("Visited the Luminous Crystal Planet.")
    elif -50 <= temp <= 100 and grav > 3:
        print("Visited the Majestic Gravity Well Planet.")
    elif temp < -50 and 0.5 <= grav <= 1.5:
        print("Visited the Enigmatic Floating Island Planet.")
    else:
        print("Visited the Mystery Planet.")
planet(int(input()), float(input()))
