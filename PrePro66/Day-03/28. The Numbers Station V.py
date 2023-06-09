'''The Numbers Station V'''

def code(num):
    '''The Numbers Station V'''
    fst = (1, 2, 3, 4, 5, 6)
    snd = (70, 71, 72, 73, 74, 75, 76, 77, 78, 79)
    trd = (80, 81, 82, 83, 84, 85, 86, 87, 88, 89)
    fth = (90, 91, 92, 93, 94, 95, 96, 97, 98)
    if abs(num) in fst:
        print("A E I N O T")
    elif abs(num) in snd:
        print("B C D F G H J K L")
    elif abs(num) in trd:
        print("P Q R S U V W X Y Z")
    elif abs(num) in fth:
        print(". : ' ( ) + - =")
    elif abs(num) == 99:
        print("Spacebar")
    else:
        print("Unknown")
    if num < 0:
        print("Negative numbers aren't allowed.")
code(int(input()))
