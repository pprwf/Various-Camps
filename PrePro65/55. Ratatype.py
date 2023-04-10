'''Ratatype'''

def typing():
    '''DocString'''
    sentence = input()
    time = 0
    word = "67YUHJNM"
    for i in sentence:
        if i in word:
            time += 1
        else:
            time += 0
    print(time)
typing()
