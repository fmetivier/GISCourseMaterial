#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
cm_12.py

Plot a georeferenced jpeg image
Add a point location and its name
we use gdal to get the image info and
cartopy to plot
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from osgeo import gdal
from osgeo import osr
import pyproj

import numpy as np


ds  =  gdal.Open("../include/raster/Aquitaine/LC82000292015341LGN00.jpg")
data  =  ds.ReadAsArray()

# map limits

geotransform  =  ds.GetGeoTransform()

#upper left corner
originX  =  geotransform[0]
originY  =  geotransform[3]

print( originX,  originY )

#image width and height
pixelWidth  =  geotransform[1]
pixelHeight  =  geotransform[5]
print( pixelWidth,  pixelHeight )
W = abs(pixelWidth * ds.RasterXSize)
H = abs(pixelHeight * ds.RasterYSize)

# get the lower right corner
CornerX= originX + W
CornerY= originY - H

#Image extent
extent = [originX, CornerX, CornerY, originY]



#figure
fig = plt.figure(figsize = (20, 20)) # because it is a raster the output size is important
ax=fig.add_subplot(111, projection=ccrs.UTM(30))

ax.imshow(data[:3,:,:].transpose((1,2,0)),  origin = 'upper', extent=extent, transform=ccrs.UTM(30))

#place Bordeaux to test
(x, y) = (-0.568058, 44.8409391)
ax.plot(x, y, 'ro', ms = 12, transform=ccrs.Geodetic())
ax.text(1.01*x, 1.01*y, 'Bordeaux', fontsize = 12, color = 'w')

ax.plot(originX,originY, 'bo', ms = 12, transform=ccrs.UTM(30))
ax.plot(CornerX,CornerY, 'bo', ms = 12, transform=ccrs.UTM(30))
ax.coastlines(resolution='10m')
ax.gridlines()

plt.show()
