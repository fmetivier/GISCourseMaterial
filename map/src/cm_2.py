#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cm_2.py

Change  projection and add gridlines
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as ft
from matplotlib import rcParams

rcParams['font.size']=6

fig = plt.figure(figsize=(15/2.54,10/2.54))

# a first projection
ax1 = fig.add_subplot(211, projection=ccrs.PlateCarree(
                                    central_longitude=0))

ax1.coastlines(resolution='110m') # resolutions available 50m and 10m

# problem with gridline ticks available in PlateCarre and Mercator only
# and tick overlaps use both xlocs and set_xticks same for y
ax1.gridlines(xlocs=range(-180,181,40), ylocs=range(-90,91,30)) # problems of labels to be solved ...
ax1.set_xticks(range(-180,181,40), crs=ccrs.PlateCarree(central_longitude=0))
ax1.set_yticks(range(-90,91,30), crs=ccrs.PlateCarree(central_longitude=0))


# a second projection
ax2 = fig.add_subplot(212, projection=ccrs.Mollweide(
                                    central_longitude=180))

# features can be used to include different kinds of back_grounds
ax2.coastlines(resolution='110m')
ax2.gridlines(color='k') # no labels for Mollweide.



plt.savefig('../figures/cm_2.pdf')
plt.show()
