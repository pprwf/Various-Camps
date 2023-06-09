'''Thailand National Highway Numbering System'''

def highway(way):
    '''Thailand National Highway Numbering System'''
    if way >= 1 and way <= 4:
        print("highway connecting Bangkok to outlying regions")
    elif way == 7 or way == 9:
        print("motorway")
    elif way in (11, 12, 21, 22, 23, 24, 41, 42, 43, 44) or (way >= 31 and way <= 38):
        print("principal highway")
    elif (way >= 101 and way <= 131) or (way >= 201 and way <= 299)\
        or (way >= 301 and way <= 376) or (way >= 401 and way <= 425):
        print("regional secondary highway")
    elif (way >= 1001 and way <= 1430) or (way >= 2027 and way <= 2425)\
        or (way >= 3001 and way <= 3902) or (way >= 4001 and way <= 4373):
        print("intra-province highway")
    else:
        print("Invalid Route")
highway(int(input()))
