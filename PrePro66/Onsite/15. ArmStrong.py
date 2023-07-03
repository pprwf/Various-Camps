'''armstrong'''

def arm(num, narcis=0):
    '''armstrong'''
    for i in str(num):
        narcis += int(i) ** len(str(num))
    print("%d is a ArmStrong number" %num if narcis == num else "%d is not a ArmStrong number" %num)
arm(int(input()))
