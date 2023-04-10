'''BMI Calculator'''

def display():
    '''แสดงผลลัพธ์'''
    name = input()
    weight = int(input())
    height = (int(input()))/100
    print("Name: %s" %name)
    print("Weight: %d kg." %weight)
    print("Height: %.2f m." %height)
    print("BMI: %.2f" %(weight/(height**2)))
display()
