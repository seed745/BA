#script for evaluating the simple grid

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as p
from find_bins import find_bins
from util import geofac_data
import csv

plt.rcParams.update({
    "axes.labelsize": 16,       # X and Y axis labels
    "xtick.labelsize": 14,      # X-axis tick labels
    "ytick.labelsize": 14,      # Y-axis tick labels

})


indexlist = []
for i in range(1,21):
    indexlist.append(f"{i}")
    
data = geofac_data()

binsize , binpos = find_bins()
binpos = np.array(binpos)
binsize = np.array(binsize)

gridsize_x=360
gridsize_y=90

pixelsize_x = 1
pixelsize_y = 1


""" x_grid = np.linspace(x_min, x_max + binsize[:,:,1].max(), grid_size, endpoint=True)
y_grid = np.linspace(y_min, y_max + binsize[:,:,0].max(), grid_size, endpoint=True) """
x_grid= np.arange(-180,181,pixelsize_x)
print(x_grid)
y_grid= np.arange(0,91,pixelsize_y)
heat_grid = np.zeros((360, 90)) 

print(len(x_grid))
print(len(y_grid))
print(heat_grid.shape)

solid_angle = []
for i in range(20):
    row = []
    for j in range(20):
        solid = (np.cos(np.deg2rad(binpos[i][j][0]))-np.cos(np.deg2rad(binpos[i][j][0]+binsize[i][j][0])))*(np.deg2rad(binsize[i][j][1]))
        row.append(solid)
    solid_angle.append(row)

print(solid_angle[0][0])
print()


for x_idx in x_grid[:-1]:
    print(x_idx)
    for y_idx in y_grid[:-1]:
        #print(y_idx)
        for i in range(20):
            for j in range(20):
                y_start, x_start = binpos[i][j]
                height, width = binsize[i][j]
                heat_value = data[i][j]

                if x_idx >= x_start and y_idx >= y_start:
                    if x_idx <= x_start + width and y_idx <= y_start + height:
                         pixel_solid = np.cos(np.deg2rad(y_idx))-np.cos(np.deg2rad(y_idx+pixelsize_y))*(np.deg2rad(pixelsize_x))
                         norm = (pixel_solid/solid_angle[i][j])
                         heat_grid[x_idx][y_idx] += heat_value*norm
        heat_grid[x_idx][y_idx]  = heat_grid[x_idx][y_idx]*5.24*60*60  #quatsch

fig, ax = plt.subplots(figsize=(8, 6))
cmap = plt.cm.plasma
norm = plt.Normalize(vmin=heat_grid.min(), vmax=heat_grid.max())
heatmap_plot = ax.pcolormesh(x_grid, y_grid, np.transpose(heat_grid), cmap=cmap, norm=norm)



""" ax.set_xlim(-180,180)
ax.set_ylim(0,90) """
ax.set_aspect("auto")
#sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)  
#sm.set_array([]) 
plt.xlabel("phi in °")
plt.ylabel("theta in °")


plt.yticks(range(0,91,30))

plt.xticks(range(-180,181,45))


cbar = plt.colorbar(heatmap_plot, ax=ax)  
cbar.set_label("particle count per hour", fontsize=16)  # Label size
cbar.ax.tick_params(labelsize=14)  # Tick size

plt.show()