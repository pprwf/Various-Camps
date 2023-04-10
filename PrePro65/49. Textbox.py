'''รักพี่ๆจังเลย <3'''

def box(num):
    '''กล่อง'''
    print("-------------------------")
    txtbox = """|                       |
|                       |
|                       |
|   Pre-Progamming 65   |
|                       |
|                       |
|                       |
-------------------------"""
    if num == 1:
        print(txtbox)
    else:
        print(txtbox + ("\n%s" %txtbox) * (num - 1))

def go_to_hell():
    '''รักพี่ๆจริงๆนะ'''
    box(int(input()))
go_to_hell()
