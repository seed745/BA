#scipt for finding the angular bins of the simple grid design

import numpy as np
import matplotlib.pyplot as plt

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
    for i in range(50):
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
    skip = False
    i=0
    while i < 29:
        if i < 27 and i%4 != 0 and i%2 == 0 :
            diode.append(active(p[i+4],p[i+5],p[i+8],p[i+9]))
            i+=1
        elif i<27:
            diode.append(active(p[i+4],p[i+5],p[i+8],p[i+9]))
        elif i == 27:
            diode.append(active(p[1],p[2],p[5],p[6])) #adding the upper photodiode
        elif i == 28:
            diode.append(active(p[29],p[30],p[33],p[34])) #adding the upper photodiode
        i+=1

    index = [None,19,None]
    for i in range(19):
        index.append(i)
    index.extend([None,20,None])
    
    diode = []
    for i in range(20):
        diode.append(0             )


    i= 0
    three = 0
    while i< len(index):
        if index[i] != None:
            if three != 3:
                if index[i]<19:
                    diode[i] =active(p[i+4],p[i+5],p[i+8],p[i+9])
                elif index[i]==19:
                    diode[i] = active(p[1],p[2],p[5],p[6]) #adding the upper photodiode
                elif index[i]==20:
                    diode[i] = active(p[29],p[30],p[33],p[34]) #adding the lower photodiode
                i+=1
                three += 1
            else:
                three = 0
        else:
            i+=1

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
                    theta.append(np.rad2deg(np.arctan2((b[1]-t[1]),z)))
                    phi.append(np.rad2deg(np.arctan2((b[0]-t[0]),z)))
            row.append([np.abs(min(theta)-max(theta)),np.abs(min(phi)-max(phi))])
            posrow.append([min(theta),min(phi)])
        bins.append(row)
        binpos.append(posrow)
   
    return bins, binpos, diode

size, pos, p = find_bins()

x=[]
y=[]
for i in p:
    for j in range(4):
        x.append(i[j][0])
        y.append(i[j][1])

#print(len(x))
plt.plot(x,y,"x")
plt.show()


