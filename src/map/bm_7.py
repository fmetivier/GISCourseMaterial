#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_7.py

Read a shapefile
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#map definition
map  =  Basemap()

#read shapefile and plot
map.readshapefile('../../Data/map/shapefiles/ne_50m_admin_0_countries/ne_50m_admin_0_countries', 'wc'
)

#scale
map.drawmeridians(range(-180, 180, 40), color = 'k', dashes = [4,  2], labels = [0, 0, 1, 0], fontsize = 12, zorder = 1)
map.drawparallels(range(-90, 90, 20), color = 'k', dashes = [4,  2], labels = [1, 0, 0, 0], fontsize = 12, zorder = 1)

# attributes stored in
print(" =========== ATTRIBUTE =========== ")
print(map.wc_info[0])

#geometry stored in
print(" =========== GEOMETRY ============ ")
print(map.wc[0])

#put them together in a tuple
print(" =========== TUPLE =============== ")
tu = zip(map.wc_info, map.wc)
print(list(tu)[0])

# loop into the dictionnaries
print(tu)
for a,b in zip(map.wc_info, map.wc):
	print(a,b)

# plt.savefig('../../figures/bm_7.svg',bbox_inches='tight')
plt.show()
