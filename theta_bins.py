#script for evaluating the simple grid

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as p
from find_bins import find_bins
from util import geofac_data
import csv
import re

#combine the bins so for each angle interval we know which other intervals are included in that and thus which coincidences
def find_bigger_bins(dict):
    keys = dict.keys()
    big_bins = {}
    for i in keys:
        nums = re.findall(r"\d+",i)
        i_min , i_max = int(nums[0]) , int(nums[1])
        for j in keys:
            nums = re.findall(r"\d+",j)
            j_min , j_max = int(nums[0]) , int(nums[1])

            if i_min <= j_min and i_max >= j_max:
                bin = i
                if bin not in big_bins.keys():
                    big_bins[bin] = [j]
                else:
                    big_bins[bin].append(j) 
    res = {}
    for key in big_bins:
        res[key] = []
        for bin in big_bins[key]:
            res[key].extend(dict[bin])
    
    return res

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




#create dicts for positive and negative theta angles.
#the key name is the theta angle range in which the given coincidence are located
theta_min = {}
theta_plus = {}
for y_idx in y_grid[:-1]: 
    for i in range(20):
        for j in range(20):
            y_start, x_start = binpos[i][j]
            height, width = binsize[i][j]

            if x_start < 0 and y_idx >= y_start:  #in negative theta the 0° are included
                if y_idx < y_start + pixelsize_y:
                    bin = f"{int(np.round(y_start,0))}-{int(np.round(y_start+height,0))}"
                    if bin not in theta_min.keys():
                        theta_min[bin] = [[i,j]]

                    else:
                        theta_min[bin].append([i,j])  
            elif x_start >= 0 and y_idx >= y_start:
                if y_idx < y_start + pixelsize_y:
                    bin = f"{int(np.round(y_start,0))}-{int(np.round(y_start+height,0))}"
                    if bin not in theta_plus.keys():
                        theta_plus[bin] = [[i,j]]

                    else:
                        theta_plus[bin].append([i,j]) 
                    
"""     if heat_grid[x_idx][y_idx][0] >= 1:
        rect = p.Rectangle(
            (x_idx,y_idx), heat_grid[x_idx][y_idx][1],heat_grid[x_idx][y_idx][2],
            linewidth = 1, edgecolor="black",
            facecolor=cmap(norm(heat_grid[x_idx][y_idx][0])),
            alpha=0.3  #transparency value
            )
        ax.add_patch(rect)
        count += 1 """
print()
print("-----------------Count fertig-----------------")

print()


print(find_bigger_bins(theta_min))
print()
#find_bigger_bins(theta_plus)




