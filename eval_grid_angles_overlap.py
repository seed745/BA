#script for evaluating the simple grid

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as p
from find_bins import find_bins

indexlist = []
for i in range(1,21):
    indexlist.append(f"{i}")
    
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
        ratio = hits/10**7
        geofac = np.pi*area*ratio
        row.append(geofac)
    map.append(row)

binsize , binpos = find_bins()
binpos = np.array(binpos)
binsize = np.array(binsize)



grid_size = 500 
x_min, x_max = binpos[:,:,0].min(), binpos[:,:,0].max()
y_min, y_max = binpos[:,:,1].min(), binpos[:,:,1].max()
""" x_grid = np.linspace(x_min, x_max + binsize[:,:,1].max(), grid_size, endpoint=True)
y_grid = np.linspace(y_min, y_max + binsize[:,:,0].max(), grid_size, endpoint=True) """
x_grid= np.linspace(0,90,grid_size)
y_grid= np.linspace(0,90,grid_size)
heat_grid = np.zeros((grid_size, grid_size)) 

for i in range(20):
    for j in range(20):
        y_start, x_start = binpos[i][j]
        height, width = binsize[i][j]
        heat_value = map[i][j]

        # Find grid indices that overlap with this rectangle
        x_indices = np.where((x_grid >= x_start) & (x_grid <= x_start + width))[0]
        y_indices = np.where((y_grid >= y_start) & (y_grid <= y_start + height))[0]

        # Add the heat value to all overlapping grid cells
        for x_idx in x_indices:
            for y_idx in y_indices:
                heat_grid[x_idx, y_idx] += heat_value  # Accumulate heat

#heat_grid = gaussian_filter(heat_grid, sigma=1.5)

fig, ax = plt.subplots(figsize=(8, 6))
cmap = plt.cm.plasma
norm = plt.Normalize(vmin=heat_grid.min(), vmax=heat_grid.max())
heatmap_plot = ax.pcolormesh(x_grid, y_grid, heat_grid, cmap=cmap, norm=norm, shading="nearest")



ax.set_xlim(0,90)
ax.set_ylim(0,90)
ax.set_aspect("auto")
#sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)  
#sm.set_array([]) 
plt.xlabel("phi in °")
plt.ylabel("theta in °")

""" ticks = []
for i in range(0,90,10):
    ticks.append(f"{i+45}")
plt.xticks(range(0,89,10),ticks)
plt.yticks(range(0,89,10),ticks) """

plt.colorbar(heatmap_plot, ax=ax, label="GF in 1/(cm²sr)")  

plt.show()