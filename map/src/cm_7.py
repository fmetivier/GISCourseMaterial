#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
cm_7.py

Read a shapefile with cartopy
"""
import cartopy.io.shapereader as shpreader
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


reader = shpreader.Reader('../include/shapefiles/ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp')
features= reader.records()

my_crs = ccrs.PlateCarree()

fig = plt.figure(figsize=(15/2.54,10/2.54))
ax = fig.add_subplot(111, projection = my_crs)


poly = []
# print the dictionnary
for feature in features:
	print('=================================================')
	for key, val in feature.attributes.items():
		print(key,val)

#print the last geometry
print(feature.geometry)


#plot the geometries
ax.add_geometries(reader.geometries(), crs=my_crs, facecolor='gray')
ax.coastlines()
ax.gridlines(draw_labels=True,xlocs=range(-180,181,60), ylocs=range(-90,91,30))

plt.savefig('../figures/cm_7.pdf',bbox_inches='tight')
plt.show()
