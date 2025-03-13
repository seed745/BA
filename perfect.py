import numpy as np
import util as u
import pandas as pd

r_source = 70 #mm
area = (r_source/10)**2*np.pi

file = "/home/jasper/OneDrive/Uni/Bachelor/sim/perfect/fit.0.hits"

df = pd.read_csv(file,skiprows=1,names=["evid","detid","x","y","z","dphi","dtheta"], sep='\s+')

#print(df.head(5))
#print(df.size)

#reading and adding the other.hits to df

for i in [1,2]:
    temp = pd.read_csv(file[:-6]+str(i)+".hits",skiprows=1,names=["evid","detid","x","y","z","dphi","dtheta"], sep='\s+')
    #print(temp.size)
    df = pd.concat([df,temp],axis=0)

#counting the coincidence events
dupli = df[df.duplicated(subset=["evid"],keep=False)]
#print(dupli.head(10))
group = dupli.groupby(by=["detid"]).indices

hits = len(group[0])
print(f"All hits: {hits}")
ratio = hits/1000000
geofac = np.pi*area*ratio

print(f"Full Geometry factor: {np.round(geofac,2)}")
print()

#GF of a cut out area of two 10x10 PDs as validation
cut = df[df["x"].between(-5,5) & df["y"].between(-5,5)]
dublicut = cut[cut.duplicated(subset=["evid"],keep=False)]

print(f"cutsize: {cut.size}")
print(dublicut.head(10))

cutgroup = dublicut.groupby(by=["detid"]).indices
print(cutgroup)
hits = len(cutgroup[0])
print(f"10x10 hits: {hits}")
ratio = hits/1000000
geofac = np.pi*area*ratio

print(f"10x10 cut GF: {np.round(geofac,5)}")