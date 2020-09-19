#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_cm_2.py

Change basemap projection
"""
from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(15/2.54,7/2.54))

#basemap
ax = fig.add_subplot(121)
map  =  Basemap(projection = 'moll',  lon_0  =  0)
map.drawcoastlines()
ax.set_title('$lon_0 = 0$')

#cartopy
ax2 = fig.add_subplot(122, projection=ccrs.Mollweide(central_longitude=180))
ax2.coastlines()
ax2.set_title('$lon_0 = 180$')

plt.savefig('../figures/bm_cm_2.pdf',bbox_inches='tight')
plt.show()
