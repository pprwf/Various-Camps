'''กางอาณาเขต'''
from math import pi

def domain(jujutsu):
    '''กางอาณาเขต'''
    print("%.2f" %(pi * ((jujutsu / 1000) / 2) ** 2))
domain(float(input()))
