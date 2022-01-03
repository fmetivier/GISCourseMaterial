#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_5_scale.py

Map limits and scales
1° gridlines
2° scale bars
"""

from mpl_toolkits.basemap import Basemap
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.size']=8

fig=plt.figure(figsize=(15/2.54,7/2.54))
#basemap
ax0=fig.add_subplot(121)
map  =  Basemap(llcrnrlon = -5, llcrnrlat = 42, urcrnrlon = 9., urcrnrlat = 52.,  projection = 'tmerc',  lat_0  =  46,  lon_0  =  2.5)
map.drawcoastlines()

map.drawmapscale(-3., 42.75, 1, 47, 200, barstyle='fancy',fontsize=6)
map.drawmapscale(6,51, 1, 47, 200)


ax1=fig.add_subplot(122)
map  =  Basemap(llcrnrlon = -5, llcrnrlat = 42, urcrnrlon = 9., urcrnrlat = 52.,  projection = 'tmerc',  lat_0  =  46,  lon_0  =  2.5)
map.drawcoastlines()
map.drawmeridians(range(-5,10,2),color='k',dashes=[4, 2], labels=[0,0,0,1])
map.drawparallels(range(40,54,2),color='k',dashes=[4, 2],labels=[1,0,1,0])



# plt.savefig('../figures/bm_5_scale.pdf',bbox_inches='tight')
plt.show()
