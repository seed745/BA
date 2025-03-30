#script for evaluating the simple grid

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


indexlist = []
for i in range(1,21):
    indexlist.append(f"{i}")
    
#file = r"D:\OneDrive - Christian-Albrechts-Universität zu Kiel\Uni\Bachelor\sim\simple_grid\test_10M.0.hits"
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
        ratio = np.sqrt(hits)/10**7
        geofac = np.pi*area*ratio
        row.append(geofac)
    map.append(row)

filename = "grid_error.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(map)
    
print("Done!")