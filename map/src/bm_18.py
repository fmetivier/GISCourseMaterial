#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
bm_18.py

Create the DEPARTEMENT Table and populate it
using the GEOFLA shapefile
and osgeo library
"""

#import libraries
import MySQLdb
import osgeo.ogr

#connect to the MySQL databse
connection  =  MySQLdb.connect(host = 'localhost', user = "root", passwd = "iznogod01")
cursor = connection.cursor()

#use the database
cursor.execute("use Parcours")
#delete the departements table if it exists
cursor.execute("DROP TABLE IF EXISTS departements")

#create the table
cursor.execute("""create table departements (
			NOM_DEPT varchar(255),
			NOM_REGION varchar(255),
			CODE_REG int,
			CODE_DEPT varchar(2) not null primary key,
			NOM_CHF varchar(255),
			CODE_CHF varchar(10),
			ID_GEOFLA int,
			X_CENTROID int,
			Y_CENTROID int,
			X_CHF_LIEU int,
			Y_CHF_LIEU int,
			GEOM geometry not null,
			spatial index (GEOM)) ENGINE = MyISAM
			""")

#import the data from the departement shapefile
shapefile = osgeo.ogr.Open("../include/shapefiles/DEPARTEMENTS/DEPARTEMENT.shp")

#get the Layer's attributes
Layer = shapefile.GetLayer(0)
spatialRef = Layer.GetSpatialRef().ExportToProj4()
numFeatures = Layer.GetFeatureCount()

#for each Feature in the layer retrieve the feature and geometry
for featureNum in range(numFeatures):
	f = Layer.GetFeature(featureNum) #get one feature
	g = f.GetGeometryRef() #get the geometry
	wkt = g.ExportToWkt() #convert it to WKT


	#execute the insert query
	cursor.execute("INSERT INTO departements values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, GeomFromText(%s, 2154))",  \
	(f.GetField("NOM_DEPT"), f.GetField("NOM_REGION"), \
	f.GetField("CODE_REG"), f.GetField("CODE_DEPT"), \
	f.GetField("NOM_CHF"), f.GetField("CODE_CHF"), f.GetField("ID_GEOFLA"), \
	f.GetField("X_CENTROID"), f.GetField("Y_CENTROID"), \
	f.GetField("X_CHF_LIEU"), f.GetField("Y_CHF_LIEU"), wkt))
	print "departement: %s loaded in Parcours database\n" % f.GetField("NOM_DEPT")


connection.commit()
connection.close()
