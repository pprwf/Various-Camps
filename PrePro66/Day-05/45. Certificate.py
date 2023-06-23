'''Certificate'''

def cert(name, surname):
    '''Certificate'''
    print("Print certificate success.\n%s-%s" %(name, surname) if name.isalpha()\
        and surname.isalpha() and name == name.capitalize() and surname == surname.capitalize()\
        else "Cannot print certificate.")
cert(input(), input())
