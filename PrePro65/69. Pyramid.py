'''Pyramid'''

def pyramid():
    '''pyramid stair'''
    num = int(input())
    for i in range(1, num + 1):
        for col in range(1, (num - 1) + (i + 1)):
            if col + i <= num:
                print(end="  ")
            else:
                print("*", end=" ")
        print("")
pyramid()
