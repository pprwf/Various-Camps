'''Atbash Cipher'''

def encode(code, decode=""):
    '''Atbash Cipher'''
    for i in code:
        decode += chr(187 - ord(i)) if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 else i
    print(decode.swapcase())
encode(input())
