'''เรียงเลข'''

def astodes(txt):
    '''ascend to descend'''
    print("".join(reversed(sorted(txt))))
astodes(list(input()))
