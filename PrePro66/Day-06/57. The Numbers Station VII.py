'''The Numbers Station VII'''

def desym(sym):
    '''decode symbol'''
    if sym in range(1, 10, 2):
        return chr(63) if sym == 9 else chr(32 + range(1, 8, 2).index(sym)).replace(" ", "Space")
    elif sym in range(2661, 2670, 2) or sym in range(2681, 2688, 2):
        return chr(37 + range(2661, 2670, 2).index(sym)) if sym in range(2661, 2670, 2) else\
            chr(123 + range(2681, 2688, 2).index(sym))
    elif sym in range(2821, 2830, 2):
        return chr(42 + range(2821, 2830, 2).index(sym))
    elif sym in range(2841, 2850, 2):
        return chr(47) if sym == 2841 else chr(58 + range(2843, 2850, 2).index(sym))
    elif sym in (2861, 2865, 2867, 2869, 8881):
        return chr(62) if sym == 2861 else chr(64) if sym == 2865 else\
            chr(91) if sym == 2867 else chr(92) if sym == 2869 else "EOL"
    elif sym in range(2881, 2890, 2):
        return chr(36) if sym == 2889 else chr(93 + range(2881, 2888, 2).index(sym))
    else:
        return dealnum(sym)

def dealnum(alnum):
    '''decode alphabet & numeric'''
    if alnum in range(41, 50, 2):
        return chr(48 + range(41, 50, 2).index(alnum))
    elif alnum in range(21, 30, 2):
        return chr(53 + range(21, 30, 2).index(alnum))
    elif alnum in range(801, 890):
        return chr(65 + range(801, 810, 2).index(alnum)) if alnum in range(801, 810, 2) else\
            chr(70 + range(821, 830, 2).index(alnum)) if alnum in range(821, 830, 2) else\
            chr(75 + range(841, 850, 2).index(alnum)) if alnum in range(841, 850, 2) else\
            chr(80 + range(861, 870, 2).index(alnum)) if alnum in range(861, 870, 2) else\
            chr(85 + range(881, 890, 2).index(alnum)) if alnum in range(851, 890, 2) else\
            "Unknown"
    elif alnum in range(601, 690):
        return chr(97 + range(601, 610, 2).index(alnum)) if alnum in range(601, 610, 2) else\
            chr(102 + range(621, 630, 2).index(alnum)) if alnum in range(621, 630, 2) else\
            chr(107 + range(641, 650, 2).index(alnum)) if alnum in range(641, 650, 2) else\
            chr(112 + range(661, 670, 2).index(alnum)) if alnum in range(661, 670, 2) else\
            chr(117 + range(681, 690, 2).index(alnum)) if alnum in range(681, 690, 2) else\
            "Unknown"
    elif alnum in (421, 423):
        return "Z" if alnum == 421 else "z"
    else:
        return "Unknown"
def decode(code):
    '''The Numbers Station VII'''
    print(desym(code))
decode(int(input()))
