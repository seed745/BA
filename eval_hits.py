#script for adding .hits files to one readable file

import pandas as pd 
import argparse
import numpy as np

#input of the filename filename.0.hits
parser = argparse.ArgumentParser(prog="eval_hits", description="Used for analyzing .hits files form Geant4", epilog="Many Thanks to Nicolas Rohrbeck")
parser.add_argument("file", type = str, help="inputfile of form path/to/filename.hits")
parser.add_argument("-a", "--area", default=0, type= float, help="area of source in cm²")
#parser.add_argument("-i", "--itime", action='store_true', help = "Itime is calculated and printed to filename.Itime")  # on/off flag
args = vars(parser.parse_args())

#reading the 0.hits file 
df = pd.read_csv(args["file"],skiprows=1,names=["evid","detid"], sep='\s+')

#print(df.size)

#reading and adding the other.hits to df
erg =[]
for i in [1,2,3]:
    erg.append(pd.read_csv(args["file"][:-6]+str(i)+".hits",skiprows=1,names=["evid","detid"], sep='\s+'))
    #print(erg[i-1].size)
    df = pd.concat([df,erg[i-1]],axis=0)

#counting the coincidence events
dupli = df[df.duplicated(subset=["evid"],keep=False)]
group = dupli.groupby("detid").indices

hits = len(group[0])
print("Source area in cm²: ")
print(args["area"])
print()
print("Coincidence hits:")
print(hits)
print()
#print("Hit/Sim Ratio: ")
ratio = hits/1000000
#print(ratio)
#print()




print("Geometry factor in 1/sr*cm²: ")
print(np.pi*args["area"]*ratio)