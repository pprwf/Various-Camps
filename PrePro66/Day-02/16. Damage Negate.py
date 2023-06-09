'''damage negate'''

def barrier(dmg, percent):
    '''barrier'''
    print("%.2f" %(dmg - dmg * (percent / 100)))
barrier(float(input()), float(input()))
