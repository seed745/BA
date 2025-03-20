#scipt for finding the angular bins of the simple grid design

import numpy as np

def find_bins():
#function for calculating the active area corners from corners of the casing of a photodiode
    def active(a,b,c,d):
        a = [a[0]+2,a[1]-2.1]
        b = [b[0]-5,b[1]-2.1]
        c = [c[0]+2,c[1]+2.1]
        d = [d[0]-5,d[1]+2.1]
        return [a, b, c, d]

#values in mm
#grid of points matching each corner of photodiode


    p = [] 
    x = 0
    y = 0
    for i in range(35):
        if i%4 == 0 and i != 0:
            x = 0
            y += -14.2
            
            p.append([x,y])
            x += 27
        else:
            p.append([x,y])
            x += 27

    #photodiode and point combination
    diode = []
    for i in range(20):
        if i < 18:
            diode.append(active(p[i+4],p[i+5],p[i+8],p[i+9]))
        elif i == 18:
            diode.append(active(p[1],p[2],p[5],p[6])) #adding the upper photodiode
        elif i == 19:
            diode.append(active(p[29],p[30],p[33],p[34])) #adding the upper photodiode

    print(len(diode))
    #angles between each active corner point to each other photodiode and then min max of those values
    z = 60.5
    bins = []
    binpos = []
    for top in diode:
        row = []
        posrow  =[]
        for bot in diode:
            theta = []
            phi = []
            for t in top:
                for b in bot:
                    theta.append(np.rad2deg(np.arctan(np.abs(t[1]-b[1])/z)))
                    phi.append(np.rad2deg(np.arctan(np.abs(t[0]-b[0])/z)))
            row.append([np.abs(min(theta)-max(theta)),np.abs(min(phi)-max(phi))])
            posrow.append([min(theta),min(phi)])
        bins.append(row)
        binpos.append(posrow)
    return bins, binpos


size, pos = find_bins()

print(pos)
print(len(pos[0]))