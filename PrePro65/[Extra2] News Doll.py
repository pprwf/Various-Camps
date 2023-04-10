'''News Doll'''

def doll():
    '''extra2'''
    print(command(int(input()), (input().capitalize())))

def command(point, word):
    '''คำสั่ง'''
    if word == "North":
        if point == 3 or point == 4:
            point = 1 * (point == 3) + 2 * (point == 4)
    elif word == "East":
        if point == 1 or point == 3:
            point = 2 * (point == 1) + 4 * (point == 3)
    elif word == "West":
        if point == 2 or point == 4:
            point = 1 * (point == 2) + 3 * (point == 4)
    elif word == "South":
        if point == 1 or point == 2:
            point = 3 * (point == 1) + 4 * (point == 2)
    if word == "Stop":
        return point
    return command(point, input().capitalize())
doll()
