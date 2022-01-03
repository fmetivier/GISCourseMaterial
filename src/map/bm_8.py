#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_8.py

Fill polygons with colours
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.patches import Patch
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch
import numpy as np
from matplotlib import cm


# definition of the figure and axis
fig      =  plt.figure(figsize = (20, 10))
ax       =  fig.add_subplot(111)

#color map I use viridis because it is nice !
cmap = cm.get_cmap('viridis')

#map definition
map  =  Basemap()

#read shapefile and plot
map.readshapefile('../../Data/map/shapefiles/ne_50m_admin_0_countries/ne_50m_admin_0_countries', 'wc')


# filling polygons
p1, p2,  p3, p4, p5    =  [], [], [], [], []

#selects and colors the countries that have more then 100M inhabitants
for info,  shape in zip(map.wc_info,  map.wc):

	for key,val in info.items():
		print("%s: %s" % (key,val))

	print("Shape:",shape)

	if info['POP_EST'] >=  1e8:
		x, y = zip(*shape)
		p1.append( Polygon(list(zip(x, y)),  closed = True))
	elif info['POP_EST'] >=  1e7 and info['POP_EST'] < 1e8:
		x, y = zip(*shape)
		p2.append( Polygon(list(zip(x, y)),  closed = True))
	elif info['POP_EST'] >=  1e6 and info['POP_EST'] < 1e7:
		x, y = zip(*shape)
		p3.append( Polygon(list(zip(x, y)),  closed = True))
	elif info['POP_EST'] >=  0 and info['POP_EST'] < 1e6:
		x, y = zip(*shape)
		p4.append( Polygon(list(zip(x, y)),  closed = True))

#making the collections
pp1 = PatchCollection(p1,  facecolor =  cmap(0.99) , edgecolor = 'k')
ax.add_collection(pp1)

pp2 = PatchCollection(p2,  facecolor =  cmap(0.75) , edgecolor = 'k')
ax.add_collection(pp2)
pp3 = PatchCollection(p3,  facecolor =  cmap(0.5), edgecolor = 'k')
ax.add_collection(pp3)
pp4 = PatchCollection(p4,  facecolor =  cmap(0.25), edgecolor = 'k')
ax.add_collection(pp4)
pp5 = PatchCollection(p5,  facecolor =  cmap(0.1), edgecolor = 'k')
ax.add_collection(pp5)

#and the legend
colors  =  [cmap(0.99),  cmap(0.75),  cmap(0.5),  cmap(0.25), cmap(0.1)]
texts  =  ["$Pop \geq 10^8$",  "$10^7 \leq Pop < 10^8$", "$10^6 \leq Pop < 10^7$",  "$Pop < 10^6$", "Pop unknown"]
patches  =  [ Patch(color = colors[i],  label = texts[i] ) for i in range(len(texts)) ]
plt.legend(handles = patches,  loc = 'lower left',  title = 'World Population (2017)')

#scale
map.drawmeridians(range(-180, 180, 40), color = 'k', dashes = [4,  2],  labels = [0, 0, 1, 0], fontsize = 12, zorder = 1)
map.drawparallels(range(-90, 90, 20), color = 'k', dashes = [4,  2],  labels = [1, 0, 0, 0], fontsize = 12, zorder = 1)

# plt.savefig('../../figures/bm_8.svg',bbox_inches='tight')
plt.show()
