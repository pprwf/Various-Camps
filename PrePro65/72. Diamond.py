'''diamond'''

def diamond(size):
    '''diamond'''
    if size % 2 == 0:
        size -= 1
    for row in range(1, (size + 1) // 2 + 1):
        for _ in range((size + 1) // 2 - row):
            print(" ", end="")
        for _ in range(row * 2 - 1):
            print("*", end="")
        print()
    for row in range((size + 1) // 2 + 1, size + 1):
        for _ in range(row - (size + 1) // 2):
            print(" ", end="")
        for _ in range((size + 1 - row) * 2 - 1):
            print("*", end="")
        print()
diamond(int(input()))
