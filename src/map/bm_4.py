#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_4.py

Map limits
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# everything is in this line !
map  =  Basemap(llcrnrlon = -5, llcrnrlat = 42, urcrnrlon = 9., urcrnrlat = 52.,
             resolution = 'i',  projection = 'tmerc',  lat_0  =  46,  lon_0  =  2.5)

map.drawmapboundary(fill_color = 'aqua')
map.fillcontinents(color = 'lightgray', lake_color = 'aqua')
map.drawcoastlines()

plt.show()
