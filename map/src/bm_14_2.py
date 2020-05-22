#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
bm_14.py

(i) Stretch the images according to the histgrams obtained using bm_13
(ii) Merge the bands in one multi-layered raster band
(iii) Reproject and crop the raster
(iv) merge to obtain the final image
(v) plot the map.
"""


import sys
sys.path.append("/home/metivier/src/python/lib")
sys.path.append('/usr/bin/')


from osgeo import gdal, osr, ogr
from osgeo.gdalconst import *
import pyproj
import gdal_merge as gm
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# get the GeoTiff driver and register it
driver = gdal.GetDriverByName('GTiff')
driver.Register()

# (i)
# Stretch the histograms
# 144030

data = gdal.Open("../include/raster/China/144030/L5144030_03020060731_B10.TIF")
gdal . Translate(destName = "../include/raster/China/144030/B10_se.TIF", srcDS = data, scaleParams = [[30, 200, 1, 254]], exponents = [0.7])
data = gdal.Open("../include/raster/China/144030/L5144030_03020060731_B20.TIF")
gdal.Translate("../include/raster/China/144030/B20_se.TIF", data, scaleParams = [[10, 120, 1, 254]], exponents = [0.7])
data = gdal.Open("../include/raster/China/144030/L5144030_03020060731_B30.TIF")
gdal.Translate("../include/raster/China/144030/B30_se.TIF", data, scaleParams = [[8, 140, 1, 254]], exponents = [0.7])

gm.main(['','-o', '../include/raster/China/144030/144030_rgb_e2.tif', '-separate', './raster/China/144030/B30_se.TIF', './raster/China/144030/B20_se.TIF', './raster/China/144030/B10_se.TIF'])
