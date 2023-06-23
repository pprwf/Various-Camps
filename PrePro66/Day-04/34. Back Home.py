'''การเดินทาง'''

def travel(money):
    '''การเดินทาง'''
    if money >= 50:
        print("Taxi\nno walking")
    elif money >= 40:
        print("BTS\nwalking")
    elif money >= 25:
        print("Motorcycle\nno walking")
    elif money >= 8:
        print("Song Thaeo\nwalking")
    else:
        print("not going anywhere")
travel(float(input()))
