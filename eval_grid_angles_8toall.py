#script for evaluating the simple grid

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as p
from find_bins import find_bins

indexlist = []
for i in range(1,21):
    indexlist.append(f"{i}")
    
file = "/home/jasper/Bachelor/sim/simple_grid/test_10M.0.hits"

df = pd.read_csv(file,skiprows=1,names=["evid","detid","x","y","z","dphi","dtheta"], sep='\s+')

area = np.pi*(83/10)**2

print(df.size)

#reading and adding the other.hits to df

for i in [1,2]:
    temp = pd.read_csv(file[:-6]+str(i)+".hits",skiprows=1,names=["evid","detid","x","y","z","dphi","dtheta"], sep='\s+')
    #print(temp.size)
    df = pd.concat([df,temp],axis=0)

#counting the coincidence events
dupli = df[df.duplicated(subset=["evid"],keep=False)]

#counts = dupli["evid"].value_counts()
#full_hits = dupli[dupli["evid"].isin(counts[counts == 4].index)]
full_hits = dupli
map = []
for i in range(1,21):
    row = []
    for j in range(21,41):
        test = pd.concat([full_hits[full_hits["detid"]==i], full_hits[full_hits["detid"]==j]])
        test = test[test.duplicated(subset=["evid"],keep=False)]
        group = test.groupby(by=["detid"]).indices
        hits = len(group[i])
        ratio = hits/10**7
        geofac = np.pi*area*ratio
        row.append(geofac)
    map.append(row)

binsize , binpos = find_bins()
binpos = np.array(binpos)
binsize = np.array(binsize)

numpixel = 400

fig, ax = plt.subplots(figsize=(8,6))

heatmap = np.array(map)
cmap = plt.cm.plasma
norm = plt.Normalize(vmin=heatmap.min(),vmax=heatmap.max())

i=7
for j in range(20):
    rect = p.Rectangle(
        (binpos[i][j][1],binpos[i][j][0]), binsize[i][j][1],binsize[i][j][0],
        linewidth = 1, edgecolor="black",
        facecolor=cmap(norm(map[i][j])),
        alpha=0.2  #transparency value
        )
    ax.add_patch(rect)

ax.set_xlim(-120,120)
ax.set_ylim(-90,90)
ax.set_aspect("auto")
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)  
sm.set_array([]) 
ax.set_xlabel("phi in °")
ax.set_ylabel("theta in °")

""" ticks = []
for i in range(0,90,10):
    ticks.append(f"{i+45}")
ax.set_xticks(range(0,89,10),ticks)
ax.set_yticks(range(0,89,10),ticks) """

cbar = plt.colorbar(sm, ax=ax, label="GF in cm²sr")  

plt.show()