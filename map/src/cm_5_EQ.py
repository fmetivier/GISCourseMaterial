#!/usr/bin/env python3
# -*- coding: utf-8 -*
"""
cm_5_EQ.py

Draw map of Feb 2017 Earthquakes
color = depth
size = magnitude

Original Idea borrowed from E. Gayer
"""

import cartopy
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

#Figure
fig = plt.figure(figsize = (20, 10))
ax = fig.add_subplot(111, projection=ccrs.EckertI(central_longitude=180))


ax.add_feature(cartopy.feature.OCEAN, zorder=0)
ax.add_feature(cartopy.feature.LAND, zorder=0, edgecolor='black')
ax.add_feature(cartopy.feature.BORDERS, zorder=0)

#~ ax.set_global()
#~ ax.gridlines(draw_labels=True, zorder=4, color='k', linestyle='--', ylocs=range(-90,91,30), xlocs=range(-180,181,40))
ax.gridlines(zorder=4, color='k', linestyle='--', ylocs=range(-90,91,30), xlocs=range(-180,181,40))




EQall_month = pd.read_csv('../include/txt/EQall_month.csv')
print(EQall_month['time'])

print(min(EQall_month['mag']),  max(EQall_month['mag']))
x, y = EQall_month['longitude'].tolist(),  EQall_month['latitude'].tolist()
sc = ax.scatter(x, y, s = np.exp(EQall_month['mag']),  c = -EQall_month['depth'],  cmap = 'viridis',  zorder = 2, transform=ccrs.PlateCarree())

##################################################################
# Tricky legend for magnitude AND depth
# 	1) For depth we use a simple colorbar
# 	2) For magnitude label won't work so we use a "phantom"
#	plot to build the legend of the scatter plot
##################################################################
#color bar
axins = inset_axes(ax,
                   width="2%",  # width = 5% of parent_bbox width
                   height="100%",  # height : 50%
                   loc='lower left',
                   bbox_to_anchor=(1.05, 0., 1, 1),
                   bbox_transform=ax.transAxes,
                   borderpad=0,
                   )

cbar = plt.colorbar(sc, cax=axins)
cbar.set_label('Depth')

#phantom plot
for i in range(7):
    plt.scatter([],  [],  s = np.exp(i+1),  edgecolor = 'k', facecolor = 'none', label = str(i+1))

#legend
h,  l  =  plt.gca().get_legend_handles_labels()
ax.legend(h,  l, title = "Magnitude", labelspacing = 2, borderpad = 2, frameon = True,  numpoints = 1,  ncol = 7,  framealpha = 0.9, bbox_to_anchor = (0.5, -0.15), loc = 'center')

plt.savefig('../figures/cm_5_EQ.pdf',bbox_inches='tight')
# See the result
plt.show()
