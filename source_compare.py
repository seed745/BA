#reading several .hits files with differing source sizes, giving the data as latex table and plotting

import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
from util import tabelle2

source_length = [2,4,6,8,9,9.5,10,12,14] #in mm
source_area = []
geofacs = []
for i in range(9):
    #reading the 0.hits file 
    df = pd.read_csv("/home/jasper/OneDrive/Uni/Bachelor/sim/source/eq10_source_"+str(i)+".0.hits",skiprows=1,names=["evid","detid"], sep='\s+')

    #reading and adding the other.hits to df
    erg =[]
    for j in [1,2]:
        erg.append(pd.read_csv("/home/jasper/OneDrive/Uni/Bachelor/sim/source/eq10_source_"+str(i)+"."+str(j)+".hits",skiprows=1,names=["evid","detid"], sep='\s+'))
        #print(erg[i-1].size)
        df = pd.concat([df,erg[j-1]],axis=0)


    #counting the coincidence events
    dupli = df[df.duplicated(subset=["evid"],keep=False)]
    group = dupli.groupby("detid").indices

    hits = len(group[0])

    ratio = hits/1000000

    #area in cm²
    area = (source_length[i]/10)**2*np.pi 
    source_area.append(area)

    #geometry factor in 1/cm²sr
    geofac = np.pi*area*ratio
    geofacs.append(geofac)

#LATEX tabular
tabelle2(np.round(source_area,2),np.round(geofacs,4))

#plot generation
plt.errorbar(source_area,geofacs,yerr= 0.0004,capsize = 5, capthick = 2)
#plt.xlim(left=2)
plt.axhline(y=0.0268, linestyle ="--", linewidth= 2, color = "orange")
plt.axvline(x=2.13, linestyle="--", linewidth= 2, color = "green")
plt.ylabel("geometry factor in 1/cm²sr")
plt.xlabel("source area in cm²")
plt.legend(["Simulation","Analytical","FOV projection"])
plt.show()

    