#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_12.py

Plot a georeferenced jpeg image
Add a point location and its name
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from osgeo import gdal
from osgeo import osr
import pyproj
from numpy import linspace
from numpy import meshgrid

ds  =  gdal.Open("../include/raster/Aquitaine/LC82000292015341LGN00.jpg")
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

UTM_X = originX+w/2
UTM_Y = originY-h/2

srcProj = pyproj.Proj(proj = "utm", zone = "30", ellps = "WGS84", units = "m")
dstProj = pyproj.Proj(proj = "longlat", ellps = "WGS84", datum = "WGS84")
Long, Lat = pyproj.transform(srcProj, dstProj, UTM_X, UTM_Y)

fig = plt.figure(figsize = (20, 20))# because it is a raster the output size is important
map = Basemap(projection = 'tmerc',  lon_0 = Long, lat_0 = Lat, width = w, height = h)

map.imshow(plt.imread("../include/raster/Aquitaine/LC82000292015341LGN00.jpg"),  origin = 'upper')

#place Bordeaux to test
x, y = map(-0.568058, 44.8409391)
plt.plot(x, y, 'ro', ms = 12)
plt.text(1.01*x, 1.01*y, 'Bordeaux', fontsize = 12, color = 'w')

map.drawmeridians(range(-18, 18, 1), color = 'r', labels = [0, 0, 1, 1], fontsize = 14, zorder = 2)
map.drawparallels(range(42, 47, 1), color = 'r', labels = [1, 1, 0, 0], fontsize = 14, zorder = 2)

plt.savefig('../figures/bm_12.pdf',bbox_inches='tight')
plt.show()
