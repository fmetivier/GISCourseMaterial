#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cm_2_2.py

Change gridlines and labels
at present it is less customizable than basemap but we can still do things
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib import rcParams

rcParams['font.size'] = 6

fig = plt.figure(figsize=(16/2.54, 12/2.54))

myproj = ccrs.PlateCarree()

ax1 = fig.add_subplot(221, projection=myproj)

ax1.coastlines(resolution='110m') # resolutions available 50m and 10m
ax1.gridlines()
# problem with gridline ticks available in PlateCarre and Mercator only
# and tick overlaps use both xlocs and set_xticks same for y


ax2 = fig.add_subplot(222, projection=myproj)
ax2.coastlines(resolution='110m') # resolutions available 50m and 10m
ax2.gridlines(draw_labels=True, xlocs = range(-180,181,40), ylocs = range(-90,91,30)) # problems of labels to be solved ...

ax3 = fig.add_subplot(223, projection=myproj)
ax3.coastlines(resolution='110m') # resolutions available 50m and 10m
gl = ax3.gridlines(xlocs = range(-180,181,40), ylocs = range(-90,91,30)) # problems of labels to be solved ...
gl.xlabels_bottom=True
gl.ylabels_left = True


ax4 = fig.add_subplot(224, projection=myproj)
ax4.coastlines(resolution='110m') # resolutions available 50m and 10m
gl2 = ax4.gridlines(xlocs = range(-180,181,40), ylocs = range(-90,91,30), color='darkblue', linestyle='--') # problems of labels to be solved ...
ax4.set_xticks(range(-180,181,40), crs=ccrs.PlateCarree(central_longitude=0))
ax4.set_yticks(range(-90,91,30), crs=ccrs.PlateCarree(central_longitude=0))


plt.savefig('../figures/cm_2_2.pdf',bbox_inches='tight')
plt.show()
