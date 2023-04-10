'''Profile'''

def instagram():
    '''ig: _pprwf'''
    gender = input().lower()
    input_id = input()
    fname = input()
    lname = input()
    age = int(input())
    occupation = input()
    print("======")
    print("ID :", input_id[0:6])
    print("Name :", (gender.replace("female", "Mrs.").replace("male", "Mr."))\
, fname.capitalize(), lname.capitalize())
    print("Age :", age, "years old")
    print("Occupation :", occupation.upper())
    print("======")
instagram()
