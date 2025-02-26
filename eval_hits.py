#script for adding .hits files to one readable file

import pandas as pd 
import argparse

parser = argparse.ArgumentParser(prog="eval_hits", description="Used for analyzing .hits files form Geant4", epilog="Many Thanks to Nicolas Rohrbeck")
parser.add_argument("file", type = str, help="inputfile of form path/to/filename.hits")
#parser.add_argument("-i", "--itime", action='store_true', help = "Itime is calculated and printed to filename.Itime")  # on/off flag
args = vars(parser.parse_args())


df = pd.read_csv(args["file"],skiprows=1,names=["evid","detid"], sep='\s+')

print(df.size)

erg =[]
for i in [1,2,3]:
    erg.append(pd.read_csv(args["file"][:-6]+str(i)+".hits",skiprows=1,names=["evid","detid"], sep='\s+'))
    df = pd.concat([df,erg[i-1]],axis=0)

print(df.size)

dupli = df[df.duplicated(subset=["evid"],keep=False)]
print(dupli.groupby("detid").size())
