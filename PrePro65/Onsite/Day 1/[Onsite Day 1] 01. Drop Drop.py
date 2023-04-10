'''Drop Drop'''

def study(grade):
    '''Retire or Pro'''
    if grade < 1:
        print("I'm so sad.")
    elif grade < 2:
        print("%.2f" %float(4 - grade))
    else:
        print("I'm so happy.")
study(float(input()))
