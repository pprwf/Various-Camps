'''Machine'''

def machine():
    '''machine'''
    num1 = int(input())
    num2 = int(input())
    summation = 0
    print("Integer Pass : ", end="")
    if num1 <= num2:
        for i in range(num1, num2 + 1):
            if i % 2 == 0:
                continue
            print(i, end=" ")
            summation += i
    else:
        for i in range(num1, num2 - 1, -1):
            if i % 2 == 0:
                continue
            print(i, end=" ")
            summation += i
    print("\nSum Answer :", summation)
machine()
