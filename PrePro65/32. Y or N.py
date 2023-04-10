'''Yes or No'''

def logic():
    '''Y/N'''
    word = input()
    if word.isalnum():
        print("Yes, it is.")
    else:
        print("No, it's not.")
logic()
