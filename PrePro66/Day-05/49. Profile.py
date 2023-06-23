'''Profile'''

def prof(gender, iden, name, surname, age):
    '''Profile'''
    print("======\nID :", iden)
    print("Name : Mr." * (gender == "male") + "Name : Mrs." * (gender == "female"), name, surname)
    print("Age :", age, "years old\nOccupation :", input().upper() + "\n======")
prof(input().lower(), input()[0:6], input().capitalize(), input().capitalize(), int(input()))
