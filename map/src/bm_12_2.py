#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
bm_12-2.py


Plot a georeferenced DEM
using merging and cropping
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


def merge_dems():

    gm.main(['', '-n', '0', '-o', '../include/raster/Guadeloupe/antilles.tif', \
    '../include/raster/Guadeloupe/ASTGTM2_N16W062/ASTGTM2_N16W062_dem.tif', \
    '../include/raster/Guadeloupe/ASTGTM2_N15W062/ASTGTM2_N15W062_dem.tif'])

    gdal.Warp("../include/raster/Guadeloupe/guadeloupe.tif", "../include/raster/Guadeloupe/antilles.tif", outputBounds = (-62, 15.7, -61, 16.7))




#this one only needs to be done once
merge_dems()

ds  =  gdal.Open("../include/raster/Guadeloupe/guadeloupe.tif")
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
map = Basemap(projection = 'cyl',  llcrnrlon = lx, llcrnrlat = ly, urcrnrlon = rx, urcrnrlat = ry, resolution = 'f')

c = map.imshow(data, origin = 'upper', zorder = 1, cmap = 'terrain')
cb = map.colorbar(c)

map.drawcoastlines(color = (0.7, 0.7, 0.7), zorder = 2)

map.drawmeridians([-61, -61.5, -62], color = 'r', labels = [0, 0, 0, 1], fontsize = 14, zorder = 4)
map.drawparallels([16, 16.5], color = 'r', labels = [1, 0, 0, 0], fontsize = 14, zorder = 4)

plt.savefig("../figures/guadeloupe.pdf", bbox_inches = "tight")
plt.show()
