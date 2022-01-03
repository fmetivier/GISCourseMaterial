#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_cm_4.py

Map limits
"""

from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


fig=plt.figure(figsize=(15/2.54,7/2.54))
#basemap
ax0=fig.add_subplot(121)
map  =  Basemap(llcrnrlon = -5, llcrnrlat = 42, urcrnrlon = 9., urcrnrlat = 52.,  projection = 'tmerc',  lat_0  =  46,  lon_0  =  2.5)

map.drawcoastlines()

#cartopy
ax1=fig.add_subplot(122, projection = ccrs.TransverseMercator(central_longitude=2.5, central_latitude=46))
ax1.set_extent((-5,9,42,52))
ax1.coastlines()
ax1.gridlines()

# plt.savefig('../../figures/bm_cm_4.svg',bbox_inches='tight')
plt.show()
