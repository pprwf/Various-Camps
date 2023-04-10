'''Magic'''

def check(age, gender, height):
    '''c'''
    if 13 <= age <= 15:
        if gender == "male" and height >= 160:
            return 1
        elif gender == "female" and height >= 155:
            return 1
        else:
            return 3
    elif 16 <= age <= 18:
        if gender == "male" and height >= 170:
            return 2
        elif gender == "female" and height >= 160:
            return 2
        else:
            return 3

def magic(name):
    '''magic'''
    age = int(input())
    gender = input().lower()
    if gender == "male":
        prefix = "Mr. "
    elif gender == "female":
        prefix = "Miss "
    else:
        gender = "bug"
    height = float(input())
    print(prefix + name, "Age: %d Height: %.2f" %(age, height))
    if gender == "bug":
        print("You can not join this school.")
        return
    result = check(age, gender, height)
    if result == 1:
        print("You can study in junior high school.")
    elif result == 2:
        print("You can study in senior high school.")
    else:
        print("You can not join this school.")
magic(input())
