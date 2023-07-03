'''Two-Sided Pyramid'''

def pyramid(size, wide=1):
    '''Two-Sided Pyramid'''
    for layer in range(1, size + 1):
        print("  " * (size - layer), end="")
        print("* " * wide, end="")
        wide += 2
        print("")
pyramid(int(input()))
