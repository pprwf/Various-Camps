'''lost character'''
import re

def lost():
    '''character'''
    word = input()
    asc = re.search('"(.+?)"', word).group(1)
    if '"' in word:
        intasc = chr(int(asc))
        print(word.replace('"', "").replace(asc, intasc))
    else:
        print("No error")
lost()
