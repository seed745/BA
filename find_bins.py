#scipt for finding the angular bins of the simple grid design

import numpy as np
import matplotlib.pyplot as plt

def find_bins():

#values in mm
#grid of points matching each corner of active area
#IMPORTANT: Indexes of the PDs are implemented with an offset of 1. So the 4th PD is labeled here as 3.
#ALSO: the output of find_bins() contains two array with a structure where the first index stands for the A detector index and the second for E.
# The bin array includes the binsize of the coincidence. The pos array includes the position or the starting point of an angular coverage rectangle.
#BE AWARE: the current visualization scripts dont work because I've included the second special case see line 79. There I created another nested list so that the 
# indexes still match with the structure but there are two angular coverage rectangles that have to be plotted.

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
   
    left = np.array([1,4,7,10,13,16])-1
    mid = np.array([2,5,8,11,14,17])-1
    right = np.array([3,6,9,12,15,18])-1

    bins = []
    binpos = []
    row_id = 0
    #iterate through all A diodes
    for tops in range(len(top)):
        row = []
        posrow  =[]
        #iterate through all E diodes
        for bot in range(len(buttom)):
            theta = []
            phi = []
            #calculate the angles between all corners
            for t in top[tops]:
                for b in buttom[bot]:
                    theta.append(np.rad2deg(np.arccos(t[2]/np.linalg.norm([t[0]-b[0],t[1]-b[1],t[2]]))))
                    phi.append(np.rad2deg(np.arctan2((t[1]-b[1]),(t[0]-b[0]))))
            #special case: diodes on top of each other
            if tops == bot:
                row.append([np.abs(min(theta)-max(theta)),360])
                posrow.append([min(theta),-180])
            #special case 2: due to the implementation of np.arctan2, we need to include this case to separate the coincidence into two. 
            # Explantion see page 27 of bachelor_mess_2025.pdf in the Thesis folder in the cloud
            elif (tops == left[row_id] and bot == mid[row_id]) or (tops == mid[row_id] and bot == right[row_id]):
                theta_l = theta[:8]
                theta_r = theta[8:]
                phi_l = phi[:8]
                phi_r = phi[8:]

                for i in range(len(phi_r)):
                    if phi_r[i] == 180:
                        phi_r[i] = -180

                row.append([[np.abs(min(theta_l)-max(theta_l)),np.abs(min(phi_l)-max(phi_l))], [np.abs(min(theta_r)-max(theta_r)),np.abs(min(phi_r)-max(phi_r))]])
                posrow.append([[min(theta_l),min(phi_l)],[min(theta_r),min(phi_r)]])
              
            elif row_id+1 <= len(left)-1 and (tops == right[row_id] and bot == left[row_id+1]):
                row.append([np.abs(min(theta)-max(theta)),np.abs(min(phi)-max(phi))])
                posrow.append([min(theta),min(phi)])
                row_id += 1
            else:
                row.append([np.abs(min(theta)-max(theta)),np.abs(min(phi)-max(phi))])
                posrow.append([min(theta),min(phi)])

        bins.append(row)
        binpos.append(posrow)
    
    return bins, binpos

bin,pos = find_bins()
print(bin[0][1])
print(pos[0][1])
print(pos[0][0])
print(pos[0][0])