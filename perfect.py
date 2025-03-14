import numpy as np
import util as u
import pandas as pd

run = []
run.append(["/home/jasper/OneDrive/Uni/Bachelor/sim/perfect/fit.0.hits",10**6,70])
run.append(["/home/jasper/OneDrive/Uni/Bachelor/sim/perfect/fit_10M.0.hits",10**7,70])
run.append(["/home/jasper/OneDrive/Uni/Bachelor/sim/perfect/fov.0.hits",10**6,83])



for i in range(len(run)):

    file , pn, r = run[i][0],run[i][1],run[i][2]  #pn = particle number, r = radius of source in mm

    area = (r/10)**2*np.pi


    print(f"Run number: {i+1}")
    print()
    print(f"Number of Particles: ")
    u.print_sci_n(pn)
    print(f"Source area in cm²: ")
    u.print_sci_n(area)
    print()


    df = pd.read_csv(file,skiprows=1,names=["evid","detid","x","y","z","dphi","dtheta"], sep='\s+')

    #print(df.head(5))
    #print(df.size)

    #reading and adding the other.hits to df

    for j in [1,2]:
        temp = pd.read_csv(file[:-6]+str(j)+".hits",skiprows=1,names=["evid","detid","x","y","z","dphi","dtheta"], sep='\s+')
        #print(temp.size)
        df = pd.concat([df,temp],axis=0)

    #counting the coincidence events
    dupli = df[df.duplicated(subset=["evid"],keep=False)]
    #print(dupli.head(10))
    group = dupli.groupby(by=["detid"]).indices

    hits = len(group[0])
    print(f"Coincidence hits: {hits}")
    ratio = hits/pn
    geofac = np.pi*area*ratio

    print(f"Full Geometry factor: {np.round(geofac,2)}")
    print()

    #GF of a cut out area of two 10x10 PDs as validation
    cut = df[df["x"].between(-5,5) & df["y"].between(-5,5)]
    dublicut = cut[cut.duplicated(subset=["evid"],keep=False)]

    #print(f"cutsize: {cut.size}")
    #print(dublicut.head(10))

    cutgroup = dublicut.groupby(by=["detid"]).indices
    #print(cutgroup)
    hits = len(cutgroup[0])
    print(f"10x10 hits: {hits}")
    ratio = hits/pn
    geofac = np.pi*area*ratio

    print(f"10x10 cut GF: {np.round(geofac,5)}")
    print()