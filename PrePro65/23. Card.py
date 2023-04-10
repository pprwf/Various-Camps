'''Card Swap'''

def card():
    '''Swap'''
    posit1 = "A"
    posit2 = "B"
    posit3 = "C"
    swap = input()
    if swap.startswith("1") and swap.endswith("2"):
        posit2 = posit1
    elif swap.startswith("2") and swap.endswith("1"):
        posit2 = posit1
    elif swap.startswith("3") and swap.endswith("2"):
        posit2 = posit3
    elif swap.startswith("2") and swap.endswith("3"):
        posit2 = posit3
    print(posit2)
card()
