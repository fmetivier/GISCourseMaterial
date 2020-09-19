#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_17.py

Purpose :
read shapefile
regrid equipotential head lines
calculate streamlines
plot

basemap version
"""
import geopandas
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.mlab import griddata # this one not the scipy one
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import cm
from liblabels import labelLine,  labelLines

# open shapefile
deps = geopandas.read_file("../include/shapefiles/Aquitaine/Isopiezes_mio-plio-quaternaire_latlon.shp")

print(deps.head())

X = []
Y = []
Z = []
for i in range(len(deps["geometry"])):

	try:
		#print deps["geometry"][i].geom_type
		if deps["geometry"][i].geom_type  ==  'LineString':
			x, y = deps["geometry"][i].coords.xy
			z = deps['COTE_mNGF'][i]*np.ones(len(x))
			X = np.hstack((X, x))
			Y = np.hstack((Y, y))
			Z = np.hstack((Z, z))

		elif deps["geometry"][i].geom_type  ==  'MultiLineString':
			for line in deps["geometry"][i]:
				x, y = line.coords.xy
				z = deps['COTE_mNGF'][i]*np.ones(len(x))
				X = np.hstack((X, x))
				Y = np.hstack((Y, y))
				Z = np.hstack((Z, z))
	except:
		print( i )
		pass



xs = np.linspace(min(X), max(X), 400)
ys = np.linspace(min(Y), max(Y), 400)
xx, yy = np.meshgrid(xs, ys)
zz = griddata(X, Y, Z, xs, ys, interp = 'linear') # grid data this method does NO EXTRAPOLATION which leads to a masked array

v, u = np.gradient(zz)# calculate gradient BEWARE lines (y-direction) first,  columns (x-direction) second


# Define figure size and basemap
fig = plt.figure(figsize = (20, 20))
ax = fig.add_subplot(111)
map  =  Basemap(llcrnrlat = 44.159251, llcrnrlon = -1.435541, urcrnrlat = 44.683123,  urcrnrlon = -0.696010, epsg = 4230)

# Retrive satellite image from ESRI
map.arcgisimage(service = 'ESRI_Imagery_World_2D',  xpixels  =  1500,  verbose =  True)

c = ax.contourf(xx, yy, zz, [10, 20, 30, 40, 50, 60, 70, 80], alpha = 0.3)
ax.contour(xx, yy, zz, [10, 20, 30, 40, 50, 60, 70, 80])
ax.streamplot(xx, yy, -u, -v, density = 1, color = 'red', arrowsize = 2.5) # streamlines $\mathbf{U}_{Darcy} \propto - \mathbf{grad}(h)$
map.colorbar(c)


# Print some information
x, y = map(-1.1681992, 44.48807)
ax.text(x, y, "Etang de Cazaux", color = 'w')
x, y = map(-1.1749838, 44.345)
ax.text(x, y, 'Etang de Parentis', color = 'w')
x, y = map(-1.355, 44.5)
ax.text(x, y, u"Océan atlantique", color = 'w', rotation = 90, fontsize = 30)
x, y = map(-1.184541, 44.668606)
ax.text(x, y, "Bassin d'Arcachon", color = 'w')


# Scale
map.drawmeridians([-1.4, -1.2, -1, -0.8], color = 'r', dashes = [4,  2],  labels = [0, 0, 0, 1], fontsize = 12)
map.drawparallels([44.2, 44.4, 44.6], color = 'r', dashes = [4,  2],  labels = [1, 0, 1, 0], fontsize = 12)


# Show
plt.savefig("../figures/shp2grid.pdf", bbox_inches = "tight")
plt.show()
