#script for evaluating the simple grid

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from util import geofac_data

data = geofac_data()
plt.rcParams.update({
    "axes.labelsize": 16,       # X and Y axis labels
    "xtick.labelsize": 13,      # X-axis tick labels
    "ytick.labelsize": 13,      # Y-axis tick labels

})


indexlist = []
for i in range(1,21):
    indexlist.append(f"{i}")
    

#differential flow from CHAOS
j = 5.24
heatmap = np.array(data)*j*60*60




plt.imshow(heatmap,cmap="plasma", origin = "lower")
plt.xticks(range(0,20),indexlist)
plt.yticks(range(0,20),indexlist)
plt.xlabel("A detector index ")
plt.ylabel("E detector index")

cbar = plt.colorbar()
cbar.set_label(r"$C$ particle count per hour", fontsize=16)  # Label size
cbar.ax.tick_params(labelsize=14)  # Tick size

plt.show()