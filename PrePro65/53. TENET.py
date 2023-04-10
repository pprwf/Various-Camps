'''tenet'''

def nolan():
    '''Christopher Nolan'''
    num = int(input())
    for _ in range(num):
        word = input()
        if word == word[::-1]:
            print(word)
nolan()
