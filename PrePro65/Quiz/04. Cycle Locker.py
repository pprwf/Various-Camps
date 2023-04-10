'''cycle'''

def cycle():
    '''cycle'''
    word = "0123456789"
    setpass = input()
    random = input()
    for i in word:
        for j in range(len(setpass)):
            if setpass[j] == i:
                print()
cycle()
