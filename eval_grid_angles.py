#script for evaluating the simple grid

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as p
from find_bins import find_bins
from util import geofac_data

indexlist = []
for i in range(1,21):
    indexlist.append(f"{i}")
    


data = geofac_data()

binsize , binpos = find_bins()
binpos = np.array(binpos)
binsize = np.array(binsize)

numpixel = 400

fig, ax = plt.subplots(figsize=(8,6))

heatmap = np.array(data)
cmap = plt.cm.plasma
norm = plt.Normalize(vmin=heatmap.min(),vmax=heatmap.max())

for i in range(20):
    for j in range(20):
        rect = p.Rectangle(
            (binpos[i][j][1],binpos[i][j][0]), binsize[i][j][1],binsize[i][j][0],
            linewidth = 1, edgecolor="black",
            facecolor=cmap(norm(heatmap[i][j])),
            alpha=0.2  #transparency value
            )
        ax.add_patch(rect)

ax.set_xlim(0,360)
ax.set_ylim(0,90)
ax.set_aspect("auto")
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)  
sm.set_array([]) 
ax.set_xlabel("phi in °")
ax.set_ylabel("theta in °")

""" ticks = []
for i in range(0,90,10):
    ticks.append(f"{i+45}")
ax.set_xticks(range(0,89,10),ticks)
ax.set_yticks(range(0,89,10),ticks) """

cbar = plt.colorbar(sm, ax=ax, label="GF in cm²sr")  

plt.show()