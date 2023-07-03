'''One-Sided Pyramid'''

def onepy(size):
    '''One-Sided Pyramid'''
    for row in range(1, size + 1):
        print("  " * (size - row), end="")
        print("* " * row, end="")
        print("")
onepy(int(input()))
