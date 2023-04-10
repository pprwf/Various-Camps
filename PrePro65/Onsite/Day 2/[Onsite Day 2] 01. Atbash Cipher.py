'''Cipher'''

def cipher(txt):
    '''cipher'''
    for i in txt:
        if 65 <= ord(i) <= 122:
            print("".join(chr(187 - ord(i)).swapcase()), end="")
        else:
            print("".join(i), end="")
cipher(input())
