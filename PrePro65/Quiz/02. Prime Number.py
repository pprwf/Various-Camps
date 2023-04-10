'''Prime'''

def prime(prim):
    '''prime number'''
    count = 0
    if prim > 1:
        for i in range(1, prim + 1):
            if prim % i == 0:
                count += 1
        if count == 2:
            print("Prime Number")
        else:
            print("Not Prime Number")
    else:
        print("Not Prime Number")
prime(int(input()))
