#script for adding .hits files to one readable file

import pandas as pd 

df = pd.read_csv("/home/jasper/OneDrive/Uni/Bachelor/sim/verif/eq10_1M.0.hits",skiprows=1,names=["evid","detid"], sep='\s+')
print(df.head())
df[df.duplicated(subset=["evid"],keep=False)]

#event = df["evid"]
#print(event.head())