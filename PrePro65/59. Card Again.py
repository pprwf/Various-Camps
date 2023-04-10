'''Card Again'''

def card():
    '''card again'''
    time = int(input())
    left = "A"
    mid = "B"
    right = "C"
    for _ in range(time):
        swap = int(input())
        if swap == 12 or swap == 21:
            left, mid = mid, left
        elif swap == 13 or swap == 31:
            left, right = right, left
        elif swap == 23 or swap == 32:
            mid, right = right, mid
    print(left + "\n" + mid + "\n" + right)
card()
