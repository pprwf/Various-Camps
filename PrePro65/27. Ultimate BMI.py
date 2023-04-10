'''BMI Upgrade'''

def ultimate():
    '''Ultimate Jetray'''
    weight = float(input())
    height = float(input()) / 100
    age = int(input())
    bmi = weight / (height ** 2)
    if age < 18:
        print("Please use BMI for Children and Teens.")
    elif bmi < 16:
        print("Severe Thinness")
    elif bmi >= 16 and bmi <= 16.99:
        print("Moderate Thinness")
    elif bmi >= 17 and bmi <= 18.49:
        print("Mild Thinness")
    elif bmi >= 18.5 and bmi <= 24.99:
        print("Normal")
    elif bmi >= 25 and bmi <= 29.99:
        print("Overweight")
    elif bmi >= 30 and bmi <= 34.99:
        print("Obese Class I")
    elif bmi >= 35 and bmi <= 39.99:
        print("Obese Class II")
    else:
        print("Obese Class III")
ultimate()
