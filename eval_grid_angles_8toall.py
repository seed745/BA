#script for evaluating the simple grid

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as p
from find_bins import find_bins
from util import geofac_data


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



fig, ax = plt.subplots(figsize=(8,6))

heatmap = np.array(data)
cmap = plt.cm.plasma
norm = plt.Normalize(vmin=heatmap.min(),vmax=heatmap.max())

j = 7
#[15,17,19,18]
for i in range(20):
    rect = p.Rectangle(
        (binpos[i][j][1],binpos[i][j][0]), binsize[i][j][1],binsize[i][j][0],
        linewidth = 1, edgecolor="black",
        facecolor=cmap(norm(data[i][j])),
        alpha=0.3  #transparency value
        )
    ax.add_patch(rect)

ax.set_xlim(-190,190)
ax.set_ylim(0,90)
ax.set_aspect("auto")
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)  
sm.set_array([]) 
ax.set_xlabel(r"$\varphi$ in °")
ax.set_ylabel(r"$\Theta$ in °")


ax.set_yticks(range(0,91,30))
ax.set_xticks(range(-180,181,45)) 


cbar = plt.colorbar(sm, ax=ax)
cbar.set_label("G in cm²sr", fontsize=16)  # Label size
cbar.ax.tick_params(labelsize=14)  # Tick size



plt.show()