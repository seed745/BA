#script for evaluating the simple grid

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

#differential flow from CHAOS
j = 5.24
heatmap = np.array(map)*j*3*60*60




plt.imshow(heatmap,cmap="plasma",interpolation="nearest", origin = "lower")
plt.xticks(range(0,20),indexlist)
plt.yticks(range(0,20),indexlist)
plt.xlabel("A detector index ")
plt.ylabel("E detector index")

cbar = plt.colorbar()
cbar.set_label("particle count after 3h")

plt.show()