#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_9.py

Convert shapefile using Geopandas
"""
#libraries
import geopandas

#read the file
deps = geopandas.read_file("../../Data/map/shapefiles/DEPARTEMENTS/DEPARTEMENT.SHP")


print(deps.head())
print(deps.crs)
print("================")

#all is here the Plate carree definition
d2 = deps.to_crs({'init': 'epsg:4326'})
print(d2.head())
print(d2.crs)
print("=================")

#test
print(deps.geometry[deps['CODE_DEPT']=='01'])
print(d2.geometry[d2['CODE_DEPT']=='01'])

#save the file
d2.to_file("../../Data/map/shapefiles/DEPARTEMENTS/departement_latlon.shp")
