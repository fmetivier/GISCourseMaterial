#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: metivier

folium maps

Plot Choropleth from a shapefile


"""
#################
# Librairies
#################
import folium
import numpy as np
import cartopy.io.shapereader as shpreader
import branca.colormap as cm


#################
# extract extent of a shapefile attribute
#################

def get_extent(shapefile, attribute):
    reader = shpreader.Reader(shapefile )
    features = reader.records()

    min_val = 9e19
    max_val = -9e19
    for feature in features:
        min_val = min(min_val,feature.attributes[attribute])
        max_val = max(max_val,feature.attributes[attribute])

    return min_val, max_val

#################
# transform linestring to folium polyline ada
#################
def LineString_to_folium_dat( idat ):
    odat = [(t[1], t[0]) for t in idat]
    return odat

#################
# create the map
#################

macarte = folium.Map(location=[44.5,0], zoom_start=8)

#################
# read shapefiles
#################

filename  = '../../map/include/shapefiles/Aquitaine/Isopiezes_mio-plio-quaternaire_latlon.shp'
reader = shpreader.Reader(filename)
features = reader.records()


#################
# create colormap
#################

cote_min, cote_max = get_extent(filename, 'COTE_mNGF')
print( cote_min, cote_max )
#dc = cote_max - cote_min
colormap = cm.linear.YlGnBu_05.scale(cote_min, cote_max)
colormap.caption = "Piezometric height (m above NGF)"
macarte.add_child(colormap)

#################
# loop to transform geometries into linestrings
# for folium.PolyLine then plot
#################
for feature in features:
    cote = feature.attributes["COTE_mNGF"]
    pp = "cote NGF: %f m" % cote
    col = colormap( cote )

    if feature.geometry.geom_type == 'LineString':
        dat = LineString_to_folium_dat( feature.geometry.coords )
        folium.PolyLine(dat, popup = pp, color = col).add_to(macarte)
    else:
        for line in feature.geometry:
            dat = LineString_to_folium_dat( line.coords )
            folium.PolyLine(dat, popup = pp, color = col).add_to(macarte)


#################
# finished !
#################

macarte.save('f_8.html')
