'''Icecream'''

def ice(floor):
    '''ice'''
    if floor < 3:
        floor = 3
    prefer = input().lower()
    if not prefer in "mscbr":
        print("Hey!,buy another shop.")
        return
    for cream in range(1, floor + 1):
        for _ in range(floor - cream):
            print(" ", end="")
        for _ in range(cream * 2 - 1):
            print(prefer, end="")
        print()
    for cone in range(1, floor):
        for _ in range(cone):
            print(" ", end="")
        for _ in range((floor - cone) * 2 - 1):
            print("_", end="")
        print()
ice(int(input()))
