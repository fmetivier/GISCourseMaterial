#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
bm_6.py

Purpose : Know what is inside a shapefile.
"""
import osgeo.ogr

# open shapefile
shapefile = osgeo.ogr.Open("../include/shapefiles/ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp")

numLayers = shapefile.GetLayerCount() # counts layers
print( "Shapefile contains %d layers" % (numLayers))

# Gets the reference system and the number of features for each layer
# In the case of GEOFLA Each layer has a spatial reference ! this complicates everything !!!
for LayerNum in range(numLayers):
    Layer = shapefile.GetLayer(LayerNum)
    numFeatures = Layer.GetFeatureCount()
    print( "Layer %d has %d features" % (LayerNum, numFeatures))
    # tests whether there is a spatial ref attached to the file
    if Layer.GetSpatialRef():
        spatialRef = Layer.GetSpatialRef().ExportToProj4()
        print( "Layer %d has spatial reference %s" % (LayerNum, spatialRef))
    else:
        print( "Layer %d has no spatial reference" % (LayerNum))

    # gets the number of attributes per feature
    for featureNum in range(numFeatures):
        feature = Layer.GetFeature(featureNum)
        fieldcount = feature.GetFieldCount()
        print( "Feature %d has %d attributes\n" % (featureNum, fieldcount))

    # prints the attributes of the last feature
    print( "Feature %d has the following attributes:" % (featureNum))
    attributes = feature.items()
    for key, value in attributes.items():
        print( "%s  = %s" % (key, value))

    # retrieve the feature geometry and print its type
    geometry = feature.GetGeometryRef()
    # geometries are stored in map units not in lat/lon this also complicates things for basemap.
    print(geometry.Centroid().ExportToWkt())
    geometryName = geometry.GetGeometryName()

print("Feature %d has a geometry of type %s" % (featureNum, geometryName))
