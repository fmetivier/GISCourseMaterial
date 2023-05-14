#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: metivier

f9.py

Plot pictures from a directory on top of OSM

"""
#################
# Librairies
#################
import folium
import numpy as np
from GPSPhoto import gpsphoto
import glob

macarte = folium.Map(location=[48.48, 2.6], zoom_start=13)

flist = glob.glob(
    "/home/metivier/Nextcloud/cours/GISCourseMaterial/Data/folium/110523/*.jpg"
)

for file in flist:
    # get position info
    pos = gpsphoto.getGPSData(file)
    print(pos)

    # add marker
    file = file.split("/GISCourseMaterial")[1]
    popup = "<img src=../.." + file + " width='400px'/>"
    folium.Marker(
        [pos["Latitude"], pos["Longitude"]],
        popup=popup,
    ).add_to(macarte)


macarte.save("f_9.html")
