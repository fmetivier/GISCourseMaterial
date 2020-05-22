#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
bm_13.py

Open Raster bands from a Geotiff Landsat 5 image
Extract and plot the histograms
"""

from osgeo import gdal,  osr,  ogr
from osgeo.gdalconst import *
import numpy as np
import matplotlib.pylab as pl
import pyproj

# get the GeoTiff driver and register it
driver  =  gdal.GetDriverByName('GTiff')
driver.Register()


def landsat_hist(fn):

    pl.figure(figsize = (8, 11))
    bcount = 1
    for f in fn:
        ds  =  gdal.Open(f,  GA_ReadOnly)
        if ds is None:
            print( 'Could not open ' + f )
            sys.exit(1)

        #raster size
        cols  =  ds.RasterXSize
        rows  =  ds.RasterYSize
        bands  =  ds.RasterCount

        print( bands,  rows,  cols )

        # Transform informations
        geotransform  =  ds.GetGeoTransform()
        originX  =  geotransform[0]
        originY  =  geotransform[3]
        pixelWidth  =  geotransform[1]
        pixelHeight  =  geotransform[5]

        print( originX,  originY,  pixelWidth,  pixelHeight )

        #read band and compute histogram
        band  =  ds.GetRasterBand(1)
        data  =  band.ReadAsArray(0,  0,  cols,  rows)
        h,  b  =  np.histogram(data, 255)
        pl.subplot(3, 1, bcount)
        pl.semilogy(b[2:250], h[2:250], 'r-')
        pl.ylabel('N')
        pl.title(f)
        bcount = bcount+1
    pl.xlabel('pixel value')

    pl.show()



fn = ["../include/raster/China/144030/L5144030_03020060731_B10.TIF", \
"../include/raster/China/144030/L5144030_03020060731_B20.TIF", \
"../include/raster/China/144030/L5144030_03020060731_B30.TIF"]
landsat_hist(fn)
