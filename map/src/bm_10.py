#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
bm_10.py

Write data to a shapefie
"""
#import libraries
from osgeo import ogr, osr
import sys,  os

# set the spatial reference
spatialReference = osr.SpatialReference()
spatialReference.SetWellKnownGeogCS('WGS84')

# create the shapefile
driver  =  ogr.GetDriverByName('ESRI Shapefile')
dstFile  =  driver.CreateDataSource('../include/shapefiles/IPGP/IPGinfo.shp')
if dstFile is None:
	print("could not create file")
	sys.exit(1)

# create the layer with the spatial reference defined above
layer  =  dstFile.CreateLayer("IPGInfo", spatialReference)

# create the field where we will store the name of places
fieldDef  =  ogr.FieldDefn("Name", ogr.OFTString)
fieldDef.SetWidth(50)
layer.CreateField(fieldDef) # add the field definition to the layer

"""
 create the two features
"""
# the IPGP feature
featureDefn = layer.GetLayerDefn()
feature  =  ogr.Feature(featureDefn)
feature.SetField('Name', 'IPGP-Cuvier')

#create the feature's geometry
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(48.844855, 2.356685)
feature.SetGeometry(point)

#add the feature to the layer
layer.CreateFeature(feature)
# destroy a feature when finished so it is saved
feature.Destroy()

#do it again for UFR
featureDefn = layer.GetLayerDefn()
feature  =  ogr.Feature(featureDefn)
feature.SetField('Name', 'IPGP-Lamarck')
point = ogr.Geometry(ogr.wkbPoint)
point.AddPoint(48.827646, 2.380656)
feature.SetGeometry(point)
layer.CreateFeature(feature)
feature.Destroy()
#same for the file a bit like close
dstFile.Destroy()
