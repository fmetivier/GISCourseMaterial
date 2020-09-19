#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_11.py

Get information fom a georeferenced image
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


# GET PROJECTION INFORMATION
proj = ds.GetProjection()
inproj  =  osr.SpatialReference()
inproj.ImportFromWkt(proj)
print( "Projection" )
print( inproj.ExportToProj4() )



# GET MAP LIMITS
geotransform  =  ds.GetGeoTransform()
#upper left corner
originX  =  geotransform[0]
originY  =  geotransform[3]
print( "upper left corner" )
print( originX,  originY )
#pixel size
pixelWidth  =  geotransform[1]
pixelHeight  =  geotransform[5]
print( "Pixel size" )
print( pixelWidth,  pixelHeight )

#width and height of the image
w = abs(pixelWidth * ds.RasterXSize)
h = abs(pixelHeight * ds.RasterYSize)
print( "Width and height" )
print( w, h )

#coordinate of the image center
UTM_X = originX+w/2
UTM_Y = originY-h/2


#CONVERT THE COORDINATES OF THE CENTER TO LON/LAT
srcProj = pyproj.Proj(inproj.ExportToProj4()) # image projection
dstProj = pyproj.Proj(proj = "longlat", ellps = "WGS84", datum = "WGS84") # Plate Carree
Long, Lat = pyproj.transform(srcProj, dstProj, UTM_X, UTM_Y)
print( "Original Center coordinates" )
print( UTM_X,  UTM_Y )
print( "Converted Center coordinates" )
print( Long,  Lat )
