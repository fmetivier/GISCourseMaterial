#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
bm_12-1.py

Plot a georeferenced DEM
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from osgeo import gdal
from osgeo import osr
import pyproj
from numpy import linspace
from numpy import meshgrid

import sys
sys.path.append('/usr/bin/')
import gdal_merge as gm

ds  =  gdal.Open("../include/raster/Guadeloupe/ASTGTM2_N16W062/ASTGTM2_N16W062_dem.tif")
data  =  ds.ReadAsArray()


# map limits
geotransform  =  ds.GetGeoTransform()
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

print( lx, ly )
print( rx, ry )

#center
Long = lx+w/2
Lat = ly+h/2
print( Long, Lat )

fig = plt.figure(figsize = (20, 20))# because it is a raster the output size is important
ax = fig.add_subplot(111)
map = Basemap(projection = 'cyl',  llcrnrlon = lx, llcrnrlat = ly, urcrnrlon = rx, urcrnrlat = ry)


c = map.imshow(data, origin = 'upper', zorder = 2, cmap = 'terrain')
cb = map.colorbar(c)


map.drawmeridians([-61, -61.5, -62], color = 'r', labels = [0, 0, 0, 1], fontsize = 14, zorder = 4)
map.drawparallels([15, 15.5, 16], color = 'r', labels = [1, 0, 0, 0], fontsize = 14, zorder = 4)

plt.show()
