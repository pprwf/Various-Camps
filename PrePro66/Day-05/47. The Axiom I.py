'''The Axiom 01'''

def axiom(year, passenger):
    '''The Axiom'''
    day = year * 360
    cup, tree = day * passenger * 1400 / 1914, passenger * 8
    cup = cup // 1 + 1 if cup % 1 != 0 else cup
    print("To prepare for", year, "years in space")
    print("AutoPilot will need", int(cup), "cups of Cupcake-In-A-Cups")
    print("The Axiom will need", tree, "trees on board")
axiom(int(input()), int(input()))
