'''The Numbers Station IV'''

def decode(fst, snd, trd, fth, fith):
    '''The Numbers Station IV'''
    print(str((fst + 6) % 10) + str((snd + 6) % 10) + str((trd + 6) % 10)
          + str((fth + 8) % 10) + str((fith + 3) % 10))
decode(int(input()), int(input()), int(input()), int(input()), int(input()))
