#reading several .hits files with differing source sizes, giving the data as latex table and plotting

import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
from util import tabelle

#area in cm²
area = 5.76
geofacs = []
erg=[]
for i in range(5):
    run = []
    run.append(i)
    #reading the 0.hits file 
    df = pd.read_csv("/home/jasper/OneDrive/Uni/Bachelor/sim/error/eq10_error_"+str(i)+".0.hits",skiprows=1,names=["evid","detid"], sep='\s+')
    run.append(df.size)
    #reading and adding the other.hits to df
    
    for j in [1,2]:
        temp = pd.read_csv("/home/jasper/OneDrive/Uni/Bachelor/sim/error/eq10_error_"+str(i)+"."+str(j)+".hits",skiprows=1,names=["evid","detid"], sep='\s+')
        run.append(temp.size)
        df , temp = pd.concat([df,temp],axis=0) , 0


    #counting the coincidence events
    dupli = df[df.duplicated(subset=["evid"],keep=False)]
    group = dupli.groupby("detid").indices

    hits = len(group[0])
    run.append(hits)
    ratio = hits/1000000

    erg.append(run)

    #geometry factor in 1/cm²sr
    geofac = np.pi*area*ratio
    geofacs.append(geofac)

runnumber = [1,2,3,4,5]
#LATEX tabular
tabelle(runnumber,np.round(geofacs,4))
#tabelle_einfach(erg)

#error calc
error = np.round(np.std(geofacs),4)

print(error)

""" #plot generation
plt.errorbar(runnumber,geofacs,yerr=error, fmt = "o", capsize = 5, capthick = 2)
#plt.xlim(left=2)
plt.axhline(y=0.0268, linestyle ="--", linewidth= 2, color = "orange")
plt.xticks([1,2,3,4,5])
plt.ylabel("geometry factor in 1/cm²sr")
plt.xlabel("run number")
plt.legend(["Analytical", "Simulation"])
plt.show()
 """
    