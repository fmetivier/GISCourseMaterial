#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
bm_3.py

Coordinate transormations using pyproj
"""
#libray
import pyproj

#
# Calculate distance between two points on earth
#

wgs84_geod  =  pyproj.Geod(ellps = 'WGS84')
lat1,  lon1  =  (27.23150120120691,  -91.522575364888709) # somewhere in the gulf of mexico
lat2,  lon2  =  (27.239416154284083,  -91.520817319790083) # near lat1,  lon1
az12, az21, dist  =  wgs84_geod.inv(lon1, lat1, lon2, lat2)
print("Azimuths from point 1 to point 2 (and vice versa): %f°, %f°\nDistance between points: %f km" % (az12, az21, dist))

#
# Change projection
#

# Define  original coordinates
UTM_X = 565718.
UTM_Y = 3980998.

# Define source and destination projections
srcProj = pyproj.Proj(proj = "utm", zone = "11", ellps = "clrk66", units = "m")
dstProj = pyproj.Proj(proj = "longlat", ellps = "WGS84", datum = "WGS84")

# Do the  corrdinate transformation
Long, Lat = pyproj.transform(srcProj, dstProj, UTM_X, UTM_Y)
print("Coordinate transformation from UTM 11 zone \n\t %0.4f, %0.4f  = > %0.4f E, %0.4f N" % (UTM_X, UTM_Y, Long, Lat))

#
# Some calculations
#

#
# Add ten kilometers to one UTM coordinate
#
UTM_Y += 10000
Long2, Lat2 = pyproj.transform(srcProj, dstProj, UTM_X, UTM_Y)
print("Coordinate transformation from UTM 11 zone\n\t %0.4f, %0.4f  = > %0.4f E, %0.4f N"	% (UTM_X, UTM_Y, Long2, Lat2))

#
# Find de position of a point located 10km north of the original point
#
azimuth = 360
distance = 10000

geod = pyproj.Geod(ellps = "WGS84") # instantiate the Geod class to do the calculation
Long3, Lat3, invangle = geod.fwd(Long, Lat, azimuth, distance)
print("The point located 10km to the North of  %0.4f E, %0.4f N has  longitude  %0.4f E and latitude %0.4f N"	% (Long, Lat, Long3, Lat3))
