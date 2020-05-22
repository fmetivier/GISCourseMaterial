#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
bm_5.py

Draw points and great circle with scale
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.size']=6
#define the figure size
fig = plt.figure(figsize = (8/2.54, 4/2.54))

#define the basic map
map  =  Basemap(projection = 'moll',  lon_0  =  0)
map.drawmapboundary(fill_color = 'aqua')
map.fillcontinents(color = 'lightgray', lake_color = 'aqua')
map.drawcoastlines()


#two samples of plots using map.plot and plt.plot
xp, yp = map(2.4,  48.8)
map.plot(xp, yp, 'bo',  ms = 10)
offset = 200
# text() is only a method of plot
plt.text(xp+offset, yp+offset, "Paris")

xw, yw = map(-77.15,  38.89)
plt.plot(xw, yw, 'bo',  ms = 10)
plt.text(xw+offset, yw+offset, "Washington D.C.")

#draw a great circle linking the two cities
map.drawgreatcircle(2.4,  48.8,  -77.15,  38.89, linewidth = 2, color = 'r')

# and the scale
map.drawmeridians(range(-180, 180, 40), color = 'k', dashes = [4,  2])
map.drawparallels(range(-90, 90, 20), color = 'k', dashes = [4,  2], labels = [1, 0, 1, 0], zorder = 1)

plt.savefig('../figures/bm_5.pdf', bbox_inches='tight')
plt.show()
