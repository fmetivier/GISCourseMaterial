#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
"""
cm_4_1.py

Map limits: add personalized labels
Depending on the projection used, sometimes standard labels do not plot correctly
in cartopy. In such cases we need to do it manually
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.path import Path
from matplotlib import rcParams
import numpy as np

rcParams['font.size']=8


fig = plt.figure(figsize=(10/2.54,10/2.54))
# Define the projection
proj = ccrs.LambertConformal(central_longitude=7.5, central_latitude=46.0, standard_parallels = (43,49))

#define axis
ax = fig.add_subplot(111, projection = proj)
# everything is in this line !
ax.set_extent((-5,9,42,52))


ax.coastlines(resolution='10m') # best possible resolution
ax.gridlines(color = 'gray' ,linestyle = '-.', xlocs= range(-7,11,2) , ylocs = range(40,56,2))


# a work around for labels not really nice but it works
ax.text(-4.1,42.1, '42N', ha='center', transform = ccrs.Geodetic())
ax.text(-4.3,44.1, '44N', ha='center', transform = ccrs.Geodetic())
ax.text(-4.8,46.1, '46N', ha='center', transform = ccrs.Geodetic())
ax.text(-5.3,48.1, '48N', ha='center', transform = ccrs.Geodetic())
ax.text(-5.6,50.1, '50N', ha='center', transform = ccrs.Geodetic())

ax.text(-3,41.7, '3W', ha='center', transform = ccrs.Geodetic())
ax.text(-1,41.85, '1W', ha='center', transform = ccrs.Geodetic())
ax.text(1,42, '1E', ha='center', transform = ccrs.Geodetic())
ax.text(3,42.1, '3E', ha='center', transform = ccrs.Geodetic())
ax.text(5,42.2, '5E', ha='center', transform = ccrs.Geodetic())
ax.text(7,42.2, '7E', ha='center', transform = ccrs.Geodetic())

#more simple draw a scale bar!
x1,y1 = (5,50)
deglat=1.65*60*np.cos(y1*np.pi/180)
x2=x1+100/deglat # pout the second point 100k apart from the first one

ax.plot([x1,x2],[y1,y1],'r-|',linewidth=2, transform=ccrs.PlateCarree())
ax.text(0.5*(x1+x2),y1+0.2,"100 km", color='r', ha='center', transform=ccrs.PlateCarree())



plt.savefig('../../figures/cm_4.svg',bbox_inches='tight')

plt.show()
