'''4 Days Out'''

def acid(phnum):
    '''alkaline'''
    print("Acidic" if 0 <= phnum < 7 else "Neutral"\
        if phnum == 7 else "Alkaline" if 7 < phnum < 15 else "YO! Wrong number")
acid(float(input()))
