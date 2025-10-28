#script for evaluating the simple grid

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


indexlist = []
for i in range(1,21):
    indexlist.append(f"{i}")
    
file = r"C:\Users\49176\Documents\OneDrive\OneDrive - Christian-Albrechts-Universität zu Kiel\Uni\Bachelor\sim\simple_grid\final_10M.0.hits"

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
#i are Indices for A detectors so 1 to 20
for i in range(1,21):
    row = []
    #j are Indices for E detectors so 21 to 40
    for j in range(21,41):
        test = pd.concat([full_hits[full_hits["detid"]==i], full_hits[full_hits["detid"]==j]])
        test = test[test.duplicated(subset=["evid"],keep=False)]
        group = test.groupby(by=["detid"]).indices
        hits = len(group[i])
        ratio = hits/10**7
        geofac = np.pi*area*ratio
        row.append(geofac)
    map.append(row)

#swap A19 and A20 due to unknown error
for row in map:
    swap = row[18]
    row[18] = row[19]
    row[19] = swap

filename = "grid_gf_final_3.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(map)
    
print("Done!")