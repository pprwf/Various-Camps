'''ASCII Error'''

def asci(txt):
    '''ASCII Error'''
    left, right = txt.find('"'), txt.rfind('"')
    print(txt[:left] + chr(int(txt[left + 1:right])) + txt[right + 1:]\
        if left != -1 else "No error")
asci(input())
