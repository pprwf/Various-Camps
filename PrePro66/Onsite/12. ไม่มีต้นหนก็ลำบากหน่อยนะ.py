'''ไม่มีต้นหนก็ลำบากหน่อยนะ'''

def onepiece(allfish, crew):
    '''วันพีซน่ะ มีอยู่จริง!!!'''
    fish = allfish.count("<^))))><")
    if fish > crew:
        print("We have many fish ahoyy!!!")
    elif fish == crew:
        print("We have enough fish for everyone.")
    else:
        if crew - fish * 2 == 0:
            print("We can share the fish together Yahoooo!!!")
        else:
            print("No one will eat them because the fish cannot be divided.")
onepiece(input(), int(input()))
