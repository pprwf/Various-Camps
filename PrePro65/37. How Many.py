'''37'''

def many():
    '''how many'''
    sentence = input().lower()
    number = input().lower()
    if len(number) == 1 and number in sentence:
        print("Character :", sentence.count(number))
    elif len(number) > 1 and number in sentence:
        print("Word :", sentence.count(number))
    else:
        print("No word and character.")
many()
