'''Game Decision'''

def homie(home):
    '''transfer gold into rune'''
    print(800 if home == "Farmer House" else 1600 if home == "Commoner House" else\
        8000 if home == "Deluxe House" else 240000 if home == "Merchant Mansion" else 560000)
homie(input())
