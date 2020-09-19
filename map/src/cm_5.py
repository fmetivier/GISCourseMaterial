#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_5.py

Draw points and great circle with scale
"""


import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as ft
from matplotlib import rcParams

rcParams['font.size']=8
#define the figure size
fig = plt.figure(figsize = (15/2.54, 8/2.54))

ax=fig.add_subplot(111,projection=ccrs.Mollweide())
ax.set_global()
ax.coastlines(resolution='110m')
ax.add_feature(ft.LAND)
ax.add_feature(ft.OCEAN)




#two samples of plots using map.plot and plt.plot
xp, yp = (2.4,  48.8)
ax.plot(xp, yp, 'bo',  ms = 10, transform=ccrs.Geodetic())
offset = 0.5
# text() is only a method of plot
ax.text(xp+offset, yp+offset, "Paris", transform=ccrs.Geodetic())

xw, yw = (-77.15,  38.89)
ax.plot(xw, yw, 'bo',  ms = 10, transform=ccrs.Geodetic())
ax.text(xw+offset, yw - 10*offset, "Washington D.C.", transform=ccrs.Geodetic())

#draw a great circle linking the two cities
ax.plot([xp,xw],[yp,yw], linewidth = 2, color = 'r', transform=ccrs.Geodetic())

# and the scale

ax.gridlines(xlocs=range(-180,181,60),ylocs=range(-90,91,30),color='k')

plt.savefig('../figures/cm_5.pdf', bbox_inches='tight')
plt.show()
