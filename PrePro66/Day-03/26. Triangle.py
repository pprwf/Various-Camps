'''สามเหลี่ยมคือรูปเรขาคณิต แล้วถ้าอยากได้เธอมาอยู่ด้วยทั้งชีวิตต้องทำยังไง'''

def tri(len1, len2, len3):
    '''สามเหลี่ยมคือรูปเรขาคณิต แล้วถ้าอยากได้เธอมาอยู่ด้วยทั้งชีวิตต้องทำยังไง'''
    if len1 == len2 & len2 == len3:
        print("Equilateral triangle")
    elif len1 == len2 | len2 == len3 | len1 == len3:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
tri(int(input()), int(input()), int(input()))
