#!/usr/bin/env python2
# -*- coding: utf-8 -*
"""
bm_5_EQ.py

Draw map of Feb 2017 Earthquakes
color = depth
size = magnitude

Original version and data  by E. Gayer
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#Figure
fig = plt.figure(figsize = (20, 10))
ax = fig.add_subplot(111)

#Basic map
map  =  Basemap(projection = 'moll',  lon_0  =  -180)
map.drawmapboundary(fill_color = 'aqua')
map.fillcontinents(color = 'lightgray', lake_color = 'aqua')
map.drawcoastlines()

EQall_month = pd.read_csv('../include/txt/EQall_month.csv')
print(EQall_month['time'])

print(min(EQall_month['mag']),  max(EQall_month['mag']))
x, y = map(EQall_month['longitude'].tolist(),  EQall_month['latitude'].tolist())
map.scatter(x, y, s = np.exp(EQall_month['mag']),  c = -EQall_month['depth'],  cmap = 'viridis',  zorder = 2)

# Scale
map.drawmeridians(range(-180, 180, 40), color = 'k', dashes = [4,  2])
map.drawparallels(range(-90, 90, 20), color = 'k', dashes = [4,  2], labels = [1, 0, 1, 0], fontsize = 12, zorder = 1)


##################################################################
# Tricky legend for magnitude AND depth
# 	1) For depth we use a simple colorbar
# 	2) For magnitude label won't work so we use a "phantom"
#	plot to build the legend of the scatter plot
##################################################################
#color bar
cbar = map.colorbar()
cbar.set_label('Depth')

#phantom plot
for i in range(7):
    plt.scatter([],  [],  s = np.exp(i+1),  edgecolor = 'k', facecolor = 'none', label = str(i+1))

#legend
h,  l  =  plt.gca().get_legend_handles_labels()
ax.legend(h,  l, title = "Magnitude", labelspacing = 2, borderpad = 2, frameon = True,  numpoints = 1,  ncol = 7,  framealpha = 0.9, bbox_to_anchor = (0.5, -0.1), loc = 'center')


# See the result
plt.show()
