'''box'''

def box(size):
    '''box'''
    print("o " * size + "\n%s" %("o " * size) * (size - 1), end="")
box(int(input()))
