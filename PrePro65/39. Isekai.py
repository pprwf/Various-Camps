'''Isekai'''
import math

def isekai():
    '''2nd Dimension'''
    x_axis = float(input())
    y_axis = float(input())
    distance = float(input())
    degree = float(input())
    side_x = distance * math.sin(math.radians(degree))
    side_y = distance * math.cos(math.radians(degree))
    x_axis += side_y
    y_axis += side_x
    print("%.2f\n%.2f" %(x_axis, y_axis))
isekai()
