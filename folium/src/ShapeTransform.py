#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Library to transform shapefiles
"""
import osgeo.ogr
import json
import pandas


def shape_to_geojson(fname):
    """
    reads a shapefile and returns
        1) a geosjson object
        2) a pandas dataframe
    """

    #get the shapefile
    shapefile = osgeo.ogr.Open(fname)
    layer = shapefile.GetLayer(0)
    layerdefn = layer.GetLayerDefn()
    FieldList = []
    FieldType = []
    dfDic = {}
    for i in range(layerdefn.GetFieldCount()):
        FieldName=layerdefn.GetFieldDefn(i).GetName()
        FieldList.append(FieldName)
        dfDic[FieldName]=[]

    numFeatures = layer.GetFeatureCount()

    #initialize the Geojson dic
    data={"type": "FeatureCollection", "features": []}

    jd = json.JSONDecoder()

    #loop through the data
    for featureNum in range(numFeatures):
            feature = layer.GetFeature(featureNum)


            #first add to the Geojson dic
            fdic={}
            fdic["type"] = "Feature"
            attributes = feature.items()

            #create the properties dic
            pdic={}
            for key, val in attributes.items():
                pdic[key] = val
                fdic["properties"] = pdic

            #create the geometry dic
            geometry = feature.GetGeometryRef()
            # we must first export to json then Transform into a dic
            fdic["geometry"] = jd.decode(geometry.ExportToJson())

            #add the feature to the featurecollection dic
            data["features"].append(fdic)

            #second add to the data columns
            for Field in FieldList:
                dfDic[Field].append(attributes[Field])

            df = pandas.DataFrame(dfDic)

    return json.dumps(data), df


if __name__ == '__main__':

    data, df = shape_to_geojson('../../map/include/shapefiles/ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp')
    print(df.head())
    print(df.columns)
