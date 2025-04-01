#script for evaluating the simple grid

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


indexlist = []
for i in range(1,21):
    indexlist.append(f"{i}")
    
#file = r"D:\OneDrive - Christian-Albrechts-Universität zu Kiel\Uni\Bachelor\sim\simple_grid\test_10M.0.hits"
file = r"/home/jasper/Bachelor/sim/simple_grid/test_10M.0.hits"

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

counts = dupli["evid"].value_counts()
full_hits = dupli[dupli["evid"].isin(counts[counts == 4].index)]
#full_hits = dupli



hits = full_hits["evid"].nunique()
ratio = hits/10**7
geofac = np.pi*area*ratio

error = np.pi*area*np.sqrt(hits)/10**7

print(f"Hits: {hits}")
print()
print(f"Geofac: {geofac}")
print()
print(f"Error: {error}")
print(f"rel. error in %: {error/geofac*100}")