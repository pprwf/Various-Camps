'''3D Euclidean Distance'''

def dis(xx1, yy1, zz1):
    '''3D Euclidean Distance'''
    xx2, yy2, zz2 = float(input()), float(input()), float(input())
    print("%.2f" %(((xx2 - xx1) ** 2 + (yy2 - yy1) ** 2 + (zz2 - zz1) ** 2) ** 0.5))
dis(float(input()), float(input()), float((input())))
