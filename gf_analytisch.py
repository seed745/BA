import numpy as np
from numpy import arctan as at
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy import constants as sc
from util import print_sci_l
from util import print_sci_n

#geometrical factor for two Photodiodes after G.R. Thomas 1972 (13)

#all measures in mm

def gfaktor_eq(x,y,Z): #in 1/cm^2*sr
    X = x/2
    Y = y/2
    return (4*(Z**2+4*X**2)**0.5*Y*at(2*Y/(Z**2+4*X**2)**0.5)
        -4*Z*Y*at(2*Y/Z)
        +4*(Z**2+4*Y**2)**0.5*X*at(2*X/(Z**2+4*Y**2)**0.5)
        -4*Z*X*at(2*X/Z)
        +Z**2*np.log(((Z**2+4*X**2)*(Z**2+4*Y**2))/((Z**2+4*X**2+4*Y**2)*Z**2))
        )/100

def est_count_per_sec(G,j): #in 1/s
    return j*G

def est_counts(n,t): #t in h and 
    return n*t*60*60

j = 5.24 #in 
t = 3 # in h
print("20x10")
print("gfaktor_eq")
print_sci_n(gfaktor_eq(10,20,60.5))
print("est_count_per_sec")
print_sci_n(est_count_per_sec(gfaktor_eq(10,20,60.5),j))
print()
print("est_counts after 3h")
print_sci_n(est_counts(est_count_per_sec(gfaktor_eq(10,20,60.5),j),t))
print()
print("10x10")
print("gfaktor_eq")
print_sci_n(gfaktor_eq(10,10,60.5))
print()
print("est_count_per_sec")
print_sci_n(est_count_per_sec(gfaktor_eq(1,1,6.05),j))
print()
print("est_counts after 3h")
print_sci_n(est_counts(est_count_per_sec(gfaktor_eq(10,10,60.5),j),t))
print()
print("18x18")
print("gfaktor_eq")
print_sci_n(gfaktor_eq(1.8,1.8,6.05))
print()
print("est_count_per_sec")
print_sci_n(est_count_per_sec(gfaktor_eq(18,18,60.5),j))
print()
print("est_counts after 3h")
print_sci_n(est_counts(est_count_per_sec(gfaktor_eq(18,18,60.5),j),t))
print()

""" #unequals
print("0.8x9,0.8x10")
print("gfaktor_uneq")
print_sci_n(gfaktor_uneq(0.8,0.8,9,10))
print()
print("est_count_per_sec")
print_sci_n(est_count_per_sec(gfaktor_uneq(0.8,0.8,9,10),j))
print()
print("est_counts after 3h")
print_sci_n(est_counts(est_count_per_sec(gfaktor_uneq(0.8,0.8,9,10),j),t))
print() """


def gfaktor_uneq(x1,x2,y1,y2,z): #in 1/cm^2*sr
    return (2(z**2+(x1+x2)**0.5)    
            *((y1+y2)*at((y1+y2)/(z**2+(x1+x2)**2)**0.5)
            -(y2-y1)*at((y2-y1)/(z**2+(x1+x2)**2)**0.5))
            -2*(z**2+(x2-x1)**2)**0.5
            *((y1+y2)*at((y1+y2)/(z**2+(x2-x1)**2)**0.5)
            -(y2-y1)*at((y2-y1)/(z**2+(x2-x1)**2)**0.5))
            +2(z**2+(y1+y2)**2)**0.5
            *((x1+x2*at((x1+x2)/(z**2+(y1+y2)**2)**0.5))
            -(x2-x1)*at((x2-x1)/(z**2+(y2-y1)**2)**0.5))
            +z**2*np.log(((z**2+(x1+x2)**2+(y2-y1)**2)*(z**2+(x2-x1)**2+(y1+y2)**2))/((z**2+(x1+x2)**2+(y1+y2)**2)*(z**2+(x2-x1)**2+(y2-y1)**2)))
    
    
            )