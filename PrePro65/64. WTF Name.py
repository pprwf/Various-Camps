'''ชื่องานอะไรครับเนี่ย'''

def abc():
    '''abc'''
    code = input()
    for _ in range(len(code) + 1):
        delete = input()
        if delete in code:
            code = code.replace(delete, "")
            if delete in code:
                code = code.replace(delete, "")
        else:
            break
    print(code)
abc()
