'''อันดับ 2'''

def second():
    '''Second Place'''
    min1 = int(input())
    min2 = int(input())
    if min1 > min2:
        min2, min1 = min1, min2
    for _ in range(8):
        num = int(input())
        if num < min1:
            min1, min2 = num, min1
        elif min1 < num < min2:
            min2 = num
    print("Almost the min :", min2)
second()
