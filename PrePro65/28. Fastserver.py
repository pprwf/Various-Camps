'''Fast Server'''

def server():
    '''Server'''
    speed_a = int(input())
    unit_a = input()
    speed_b = int(input())
    unit_b = input()
    if unit_a == "Millisecond":
        sec_a = speed_a / 1000
    elif unit_a == "Microsecond":
        sec_a = speed_a / 1000000
    elif unit_a == "Nanosecond":
        sec_a = speed_a / 1000000000
    else:
        sec_a = speed_a / 1000000000000
    if unit_b == "Millisecond":
        sec_b = speed_b / 1000
    elif unit_b == "Microsecond":
        sec_b = speed_b / 1000000
    elif unit_b == "Nanosecond":
        sec_b = speed_b / 1000000000
    else:
        sec_b = speed_b / 1000000000000
    if sec_a > sec_b:
        times = sec_a / sec_b
        print("Server B, %.6f second\nFaster than server A , %d times" %(sec_b, times))
    elif sec_b > sec_a:
        times = sec_b / sec_a
        print("Server A, %.6f second\nFaster than server B , %d times" %(sec_a, times))
    else:
        print("equal")
server()
