#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
cm_12-2.py


Plot a georeferenced DEM
using merging and cropping

Cartopy version
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from osgeo import gdal
from osgeo import osr
import pyproj
from numpy import linspace
from numpy import meshgrid

import sys
sys.path.append('/usr/bin/')
import gdal_merge as gm


fname = ["../include/raster/Guadeloupe/ASTGTM2_N16W062/ASTGTM2_N16W062_dem.tif","../include/raster/Guadeloupe/ASTGTM2_N15W062/ASTGTM2_N15W062_dem.tif"]

fig = plt.figure(figsize = (20, 20))# because it is a raster the output size is important
ax = fig.add_subplot(111, projection = ccrs.PlateCarree())

minx=180
maxx=-180
miny=90
maxy=-90

for f in fname:

	ds  =  gdal.Open(f)
	data  =  ds.ReadAsArray()


	# map limits
	geotransform  =  ds.GetGeoTransform()
	proj=ds.GetProjection()
	print(proj)
	originX  =  geotransform[0]
	originY  =  geotransform[3]
	print( originX,  originY )
	pixelWidth  =  geotransform[1]
	pixelHeight  =  geotransform[5]
	print( pixelWidth,  pixelHeight )

	w = abs(pixelWidth * ds.RasterXSize)
	h = abs(pixelHeight * ds.RasterYSize)

	#corners
	lx = originX
	ly = originY-h
	rx = lx+w
	ry = originY

	if minx > min(lx,rx):
		minx = min(lx,rx)
	if maxx < max(lx,rx):
		maxx = max(lx,rx)
	if miny > min(ly,ry):
		miny = min(ly,ry)
	if maxy < max(ly,ry):
		maxy = max(ry,ly)

	extent = (originX, originX + abs(pixelWidth * ds.RasterXSize)  , originY - abs(pixelHeight * ds.RasterYSize) , originY)
	print(extent)

	print('lower left corner', lx, ly )
	print('upper right corner',  rx, ry )

	#get the spatial projection of the DEM

	inproj = osr.SpatialReference()
	inproj.ImportFromWkt(proj)
	projcs = inproj.GetAuthorityCode('PROJCS')
	print(projcs)
	#~ DEM_proj = ccrs.epsg(6326)


	ax.imshow(data, extent=extent, origin='upper', cmap='terrain', transform=ccrs.PlateCarree())


ax.coastlines(resolution='10m')
ax.gridlines(draw_labels=True)
ax.set_xlim(minx,maxx)
ax.set_ylim(miny,maxy)
plt.savefig("../figures/antillespdf", bbox_inches = "tight")
plt.show()
