#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cm_14.py

(i) Stretch the images according to the histgrams obtained using bm_13
(ii) Merge the bands in one multi-layered raster band
(iii) Reproject and crop the raster
(iv) merge to obtain the final image
(v) plot the map.

"""


import sys
# note that this path is  valid for linux debian
# for windows and mac you need to place a valid path
sys.path.append('/usr/lib/python3/dist-packages/osgeo/utils')


from osgeo import gdal
import gdal_merge as gm
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# get the GeoTiff driver and register it
driver  =  gdal.GetDriverByName('GTiff')
driver.Register()

def process_geotiffs():
    # (i)
    # Stretch the histograms
    # 144030

    data = gdal.Open("../../Data/map/raster/China/144030/L5144030_03020060731_B10.TIF")
    gdal.Translate(destName = "../../Data/map/raster/China/144030/B10_s.TIF", srcDS = data, scaleParams = [[30,  200,  1,  254]], exponents = [0.7])
    data = gdal.Open("../../Data/map/raster/China/144030/L5144030_03020060731_B20.TIF")
    gdal.Translate("../../Data/map/raster/China/144030/B20_s.TIF", data,  scaleParams = [[10,  120,  1,  254]], exponents = [0.7])
    data = gdal.Open("../../Data/map/raster/China/144030/L5144030_03020060731_B30.TIF")
    gdal.Translate("../../Data/map/raster/China/144030/B30_s.TIF", data,  scaleParams = [[8,  140,  1,  254]], exponents = [0.7])


    # 145030
    data = gdal.Open("../../Data/map/raster/China/145030/L5145030_03020060722_B10.TIF")
    gdal.Translate(destName = "../../Data/map/raster/China/145030/B10_s.TIF", srcDS = data, scaleParams = [[30,  200,  1,  254]], exponents = [0.7])
    data = gdal.Open("../../Data/map/raster/China/145030/L5145030_03020060722_B20.TIF")
    gdal.Translate("../../Data/map/raster/China/145030/B20_s.TIF", data,  scaleParams = [[10,  120,  1,  254]], exponents = [0.7])
    data = gdal.Open("../../Data/map/raster/China/145030/L5145030_03020060722_B30.TIF")
    gdal.Translate("../../Data/map/raster/China/145030/B30_s.TIF", data,  scaleParams = [[8,  140,  1,  254]], exponents = [0.7])

    # (ii)
    # Merge the bands
    #
    gm.main(['', '-o',  '../../Data/map/raster/China/144030/144030_rgb.tif', '-separate', '../../Data/map/raster/China/144030/B30_s.TIF',  '../../Data/map/raster/China/144030/B20_s.TIF',  '../../Data/map/raster/China/144030/B10_s.TIF'])
    gm.main(['', '-o',  '../../Data/map/raster/China/145030/145030_rgb.tif', '-separate', '../../Data/map/raster/China/145030/B30_s.TIF',  '../../Data/map/raster/China/145030/B20_s.TIF',  '../../Data/map/raster/China/145030/B10_s.TIF'])


    # (iii)
    # Crop and reproject the images
    #
    gdal.Warp("../../Data/map/raster/China/144030/144030_rgb_ll.tif", "../../Data/map/raster/China/144030/144030_rgb.tif",  dstSRS = "+proj=latlong +datum=WGS84", outputBounds = (84.25,  42.5,  86.1,  43.5)) # NB: no spaces surrounding '=' in the SRS !!!
    gdal.Warp("../../Data/map/raster/China/145030/145030_rgb_ll.tif", "../../Data/map/raster/China/145030/145030_rgb.tif",  dstSRS = "+proj=latlong +datum=WGS84", outputBounds = (82.5,  42.5,  84.5,  43.5)) # NB: no spaces surrounding '=' in the SRS !!!

    #~ # (iv)
    #~ # Merge into the final image
    #~ #
    gm.main(['', '-n', '0', '-o',  '../../Data/map/raster/China/bayan.tif',  '../../Data/map/raster/China/144030/144030_rgb_ll.tif',  '../../Data/map/raster/China/145030/145030_rgb_ll.tif'])


# if needed
process_geotiffs()

#
# Draw the map
#
ds  =  gdal.Open("../../Data/map/raster/China/bayan.tif")
data  =  ds.ReadAsArray()


fig = plt.figure(figsize = (20, 10))# because it is a raster the output size matters

# If you do not need a fancy projection use PlateCarree. It's much faster because there is no need to reproject the image pixels
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

im_extent = [82.5, 86.1, 42.5, 43.5] # [left_x, right_x, bottom_y, top_y]
ax.imshow(data[:3,:,:].transpose((1,2,0)),  extent = im_extent, origin = 'upper', transform=ccrs.PlateCarree())

# Using platecaree you can also plot your labels !
ax.gridlines(draw_labels=True, xlocs=range(82,86,1),ylocs=[42.5,43,43.5])

# Finally set the extent
ax.set_xlim(82.5,86.1)
ax.set_ylim(42.5,43.5)

plt.show()
