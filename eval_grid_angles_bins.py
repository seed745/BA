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

y_grid= np.arange(0,91,pixelsize_y)
heat_grid = np.zeros((360, 90, 3)) 




max = 20
#plotting the rectangles
fig, ax = plt.subplots(figsize=(8,6))


cmap = plt.cm.plasma
norm = plt.Normalize(vmin=0,vmax=max)

count= 0
for x_idx in x_grid[:-1]:
    print(x_idx)
    for y_idx in y_grid[:-1]: 
        for i in range(20):
            for j in range(20):
                y_start, x_start = binpos[i][j]
                height, width = binsize[i][j]

                if x_idx >= x_start and y_idx >= y_start:
                    if x_idx < x_start + pixelsize_x and y_idx < y_start + pixelsize_y:
                        if heat_grid[x_idx][y_idx][0] == 0:
                            heat_grid[x_idx][y_idx][0] += 1
                            heat_grid[x_idx][y_idx][1] = width
                            heat_grid[x_idx][y_idx][2] = height
    
                        else:
                            heat_grid[x_idx][y_idx][0] += 1

                        
        if heat_grid[x_idx][y_idx][0] >= 1:
            rect = p.Rectangle(
                (x_idx,y_idx), heat_grid[x_idx][y_idx][1],heat_grid[x_idx][y_idx][2],
                linewidth = 1, edgecolor="black",
                facecolor=cmap(norm(heat_grid[x_idx][y_idx][0])),
                alpha=0.3  #transparency value
                )
            ax.add_patch(rect)
            count += 1
print()
print("-----------------Count fertig-----------------")
print(count)








ax.set_aspect("auto")
#sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)  
#sm.set_array([]) 
plt.xlabel(r"$\varphi$ in °")
plt.ylabel(r"$\Theta$ in °")


plt.yticks(range(0,91,30))

plt.xticks(range(-180,181,45))

sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)  
sm.set_array([]) 

cbar = plt.colorbar(sm, ax=ax)  
cbar.set_label("Coincidence Count", fontsize=16)  # Label size
cbar.ax.tick_params(labelsize=14)  # Tick size
cbar.set_ticks(ticks=range(21))

plt.show()