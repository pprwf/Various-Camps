'''Travel'''

def travel():
    '''วิธีเดินทาง'''
    weather = input()
    imp = input()
    distance = float(input())
    if weather == "rainy" and not imp == "important":
        print("Not go")
    else:
        if distance >= 0 and distance < 1:
            print("Walk")
        elif distance >= 1 and distance < 20:
            print("Motorcycle")
        elif distance >= 20 and distance < 300:
            print("Car")
        elif distance >= 300:
            print("Private jet")
        else:
            print("Error")
travel()
