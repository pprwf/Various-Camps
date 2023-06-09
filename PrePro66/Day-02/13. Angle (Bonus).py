'''bonus'''

import math

def angle(vec1x, vec1y, vec2x, vec2y):
    '''bonus point'''
    dot = vec1x * vec2x + vec1y * vec2y
    mag1 = abs(math.sqrt(vec1x ** 2 + vec1y ** 2))
    mag2 = abs(math.sqrt(vec2x ** 2 + vec2y ** 2))
    print(int(math.degrees(math.acos(dot / (mag1 * mag2)))))
angle(float(input()), float(input()), float(input()), float(input()))
