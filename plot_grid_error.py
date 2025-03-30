import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as p
from util import geofac_error
from util import geofac_data

indexlist = []
for i in range(1,21):
    indexlist.append(f"{i}")

error = np.array(geofac_error())
data = np.array(geofac_data())

pro = error/data * 100


plt.imshow(pro,cmap="plasma",interpolation="nearest", origin = "lower")
plt.xticks(range(0,20),indexlist,fontsize=14)
plt.yticks(range(0,20),indexlist,fontsize=14)
plt.xlabel(r"A detector index",fontsize=16)
plt.ylabel(r"E detector index",fontsize=16)

cbar = plt.colorbar()
cbar.set_label(r"$\frac{\Delta G}{G}$ GF error in %",fontsize=16)
cbar.set_ticklabels(range(0,11),fontsize=16)

plt.show()