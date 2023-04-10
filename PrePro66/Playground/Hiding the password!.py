'''Hiding the password!'''

def password(encode, decode=""):
    '''only alnum'''
    for i in encode:
        if i.isnumeric():
            if int(i) % 2:
                decode += "#"
            else:
                decode += "*"
        else:
            decode += "_"
    print(decode)

password(input())
