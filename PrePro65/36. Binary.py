'''Binary'''

def onoffonoff():
    '''keshi'''
    binary = bin(int(input())).replace("0b", "")
    print(binary.replace("0", "close, ").replace("1", "open, ")[:-2])
onoffonoff()
