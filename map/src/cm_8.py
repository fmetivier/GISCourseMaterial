#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
cm_8.py

Fill polygons with colours
Note the ability of cartoy to reproject datasets
"""

import cartopy
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib import cm


# definition of the figure and axis
proj_crs = ccrs.Mollweide()
my_crs = ccrs.PlateCarree()
fig      =  plt.figure(figsize = (20, 10))
ax       =  fig.add_subplot(111, projection = proj_crs)

#color map I use viridis because it is nice !
cmap = cm.get_cmap('viridis')

reader = shpreader.Reader('../include/shapefiles/ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp')
features = reader.records()

#~ ax.gridlines(draw_labels=True)
ax.gridlines()
ax.coastlines()

for feature in features:

	if feature.attributes['POP_EST'] >=  1e8:
		ax.add_geometries([feature.geometry], facecolor = cmap(0.99), crs=my_crs)

	elif feature.attributes['POP_EST'] >=  1e7 and feature.attributes['POP_EST'] < 1e8:
		ax.add_geometries([feature.geometry], facecolor = cmap(0.75), edgecolor = 'k', crs=my_crs)

	elif feature.attributes['POP_EST'] >=  1e6 and feature.attributes['POP_EST'] < 1e7:
		ax.add_geometries([feature.geometry], facecolor = cmap(0.5), edgecolor = 'k', crs=my_crs)

	elif feature.attributes['POP_EST'] >=  0 and feature.attributes['POP_EST'] < 1e6:
		ax.add_geometries([feature.geometry], facecolor = cmap(0.25), edgecolor = 'k', crs=my_crs)

	else:
		ax.add_geometries([feature.geometry], facecolor = cmap(0.1), edgecolor = 'k', crs=my_crs)


#and the legend
colors  =  [cmap(0.99),  cmap(0.75),  cmap(0.5),  cmap(0.25), cmap(0.1)]
texts  =  ["$Pop \geq 10^8$",  "$10^7 \leq Pop < 10^8$", "$10^6 \leq Pop < 10^7$",  "$Pop < 10^6$", "Pop unknown"]
patches  =  [ Patch(color = colors[i],  label = texts[i] ) for i in range(len(texts)) ]
plt.legend(handles = patches,  loc = 'lower left',  title = 'World Population (2017)')


plt.show()
