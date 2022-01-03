#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_16.py

Draw equipotential (isopieze map) lines of the Plio-quaternary aquifer
on top of a satellite view of the Lakes of Landes south of Arcachon.

basemap version
"""

#libraries
import geopandas
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import cm
from liblabels import labelLine,  labelLines


def convert_shape():
    #read the file
    piezo = geopandas.read_file("../../Data/map/shapefiles/Aquitaine/Isopiezes_mio-plio-quaternaire.shp")


    print(piezo.head())
    print(piezo.crs)
    print(" ================ ")

    #test to get rid of null or empty values in the record (else the conversion fails)
    piezo =  piezo[piezo['geometry'].notnull()]
    #all is here the Plate carree definition
    piezo2 = piezo.to_crs({'init': 'epsg:4326'})
    print(piezo2.head())
    print(piezo.crs)
    print(" ================= ")

    #save the file
    piezo2.to_file("../../Data/map/shapefiles/Aquitaine/Isopiezes_mio-plio-quaternaire_latlon.shp",encoding='utf-8')


def map_piezo():

    # Define figure size and basemap
    fig = plt.figure(figsize = (20, 20))
    ax = fig.add_subplot(111)
    map  =  Basemap(llcrnrlat = 44.159251, llcrnrlon = -1.435541, urcrnrlat = 44.683123,  urcrnrlon = -0.696010, epsg = 4230)

    # Retrieve satellite image from ESRI
    map.arcgisimage(service = 'ESRI_Imagery_World_2D',  xpixels  =  1500,  verbose =  True)

    # Open shapefile
    map.readshapefile("../../Data/map/shapefiles/Aquitaine/Isopiezes_mio-plio-quaternaire_latlon",  "piezo", color = 'w')

    # retrieve the polylines and plot them using different colors
    cmap = cm.get_cmap('YlOrRd')
    for info,  shape in zip(map.piezo_info,  map.piezo):
            c = cmap(float(info['COTE_mNGF'])/100.)
            x, y = zip(*shape)
            ax.plot(x, y, '-', linewidth = 2, color = c, label = info['COTE_mNGF'])

    # Label the contours
    labelLines(plt.gca().get_lines(), backgroundcolor = 'DarkGreen')

    # Print some information
    x, y = map(-1.1681992, 44.48807)
    ax.text(x, y, "Etang de Cazaux", color = 'w')
    x, y = map(-1.1749838, 44.345)
    ax.text(x, y, 'Etang de Parentis', color = 'w')
    x, y = map(-1.355, 44.5)
    ax.text(x, y, u"Océan atlantique", color = 'w', rotation = 90, fontsize = 30)
    x, y = map(-1.184541, 44.668606)
    ax.text(x, y, "Bassin d'Arcachon", color = 'w')


    # Scale
    map.drawmeridians([-1.4, -1.2, -1, -0.8], color = 'r', dashes = [4,  2],  labels = [0, 0, 0, 1], fontsize = 12)
    map.drawparallels([44.2, 44.4, 44.6], color = 'r', dashes = [4,  2],  labels = [1, 0, 1, 0], fontsize = 12)


    # Show
    # plt.savefig('../figures/bm_16.pdf',bbox_inches='tight')
    plt.show()

map_piezo()
