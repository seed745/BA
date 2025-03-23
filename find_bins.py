#scipt for finding the angular bins of the simple grid design

import numpy as np
import matplotlib.pyplot as plt

def find_bins():

#values in mm
#grid of points matching each corner of active area


    p = [] 
    x = 0
    y = 0
    for i in range(50):
        if i%3 == 0 and i != 0:
            x = 0
            y += -14.2
            
            p.append([x,y])
            x += 27
        else:
            p.append([x,y])
            x += 27


    diode =[]
    for i in p[3:21]:  #6x3 grid
        pd = []
        pd.append(i)
        pd.append([i[0]+20,i[1]])
        pd.append([i[0],i[1]-10])
        pd.append([i[0]+20,i[1]-10])
        diode.append(pd)
    diode.append([[p[1][0],p[1][1]],[p[1][0]+20,p[1][1]],[p[1][0],p[1][1]-10],[p[1][0]+20,p[1][1]-10]])  #diode 19
    diode.append([[p[22][0],p[22][1]],[p[22][0]+20,p[22][1]],[p[22][0],p[22][1]-10],[p[22][0]+20,p[22][1]-10]])  #diode 20
    z = 60.8
    top = []
    for i in diode:
        row=[]
        for j in i:
            row.append(j+[z])
        top.append(row)

    buttom = []
    for i in diode:
        row = []
        for j in i:
            row.append(j+[0])
        buttom.append(row)
    #angles between each active corner point to each other photodiode and then min max of those values
   

    bins = []
    binpos = []
    for top in top:
        row = []
        posrow  =[]
        for bot in buttom:
            theta = []
            phi = []
            for t in top:
                for b in bot:
                    theta.append(np.rad2deg(np.arctan(np.linalg.norm([t[0]-b[0],t[1]-b[1]])/t[2])))
                    phi.append(np.rad2deg(np.arctan2((t[0]-b[0]),(t[1]-b[1]))))
            row.append([np.abs(min(theta)-max(theta)),np.abs(min(phi)-max(phi))])
            posrow.append([min(theta),min(phi)])
        bins.append(row)
        binpos.append(posrow)
    
    return bins, binpos, diode

b, p, diode = find_bins()

x=[]
y=[]
for i in diode:
    for j in i:
        x.append(j[0])
        y.append(j[1])

plt.plot(x,y,"x")
plt.show()
