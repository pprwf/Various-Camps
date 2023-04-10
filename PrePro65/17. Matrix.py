'''Matrix'''

def matrix():
    '''ขกคิด'''
    a_1 = int(input())
    a_2 = int(input())
    a_3 = int(input())
    a_4 = int(input())
    det_a = (a_1 * a_4) - (a_2 * a_3)
    c_1 = int(input())
    c_2 = int(input())
    c_3 = int(input())
    c_4 = int(input())
    det_c = (c_1 * c_4) - (c_2 * c_3)
    b_1 = c_1 - a_1
    b_2 = c_2 - a_2
    b_3 = c_3 - a_3
    b_4 = c_4 - a_4
    detd = det_a + det_c + ((b_1 * b_4) - (b_2 * b_3))
    print("b1: %d\nb2: %d\nb3: %d\nb4: %d\nD: %.2f" %(b_1, b_2, b_3, b_4, detd))
matrix()
