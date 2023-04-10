'''ทำไมเธออ่านไม่ตอบ'''

def unread():
    '''เรียงข้อความ'''
    word1 = input()
    word2 = input()
    word3 = input()
    if len(word1) < len(word2) and len(word1) < len(word3):
        print(word1.capitalize())
        if len(word2) < len(word3):
            print(word2.capitalize())
            print(word3.capitalize())
        else:
            print(word3.capitalize())
            print(word2.capitalize())
    elif len(word2) < len(word1) and len(word2) < len(word3):
        print(word2.capitalize())
        if len(word1) < len(word3):
            print(word1.capitalize())
            print(word3.capitalize())
        else:
            print(word3.capitalize())
            print(word1.capitalize())
    else:
        print(word3.capitalize())
        if len(word1) < len(word3):
            print(word1.capitalize())
            print(word2.capitalize())
        else:
            print(word2.capitalize())
            print(word1.capitalize())
unread()
