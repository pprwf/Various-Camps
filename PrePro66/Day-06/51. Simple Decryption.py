'''Simple Decryption'''

def ran(alp):
    '''decryption'''
    return 20 if alp in ("a", "f", "k", "p", "u", "z") else 21\
        if alp in ("b", "g", "q", "l", "v") else 22 if alp in ("c", "h", "m", "r", "w")\
        else 23 if alp in ("d", "i", "n", "s", "x") else 24

def decrypt(char, char2, char3, char4, char5):
    '''Simple Decryption'''
    print(ran(char) + ran(char2) + ran(char3) + ran(char4) + ran(char5))
decrypt(input(), input(), input(), input(), input())
