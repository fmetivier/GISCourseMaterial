#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:16:23 2020

@author: metivier

folium maps

Exemple of maps made of wms server layers


"""
import folium

#create the map
macarte = folium.Map(location=[25,2.4], zoom_start=3, tiles=None)

URL  =  'https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi'
Layer  =  'ASTER_GDEM_Greyscale_Shaded_Relief'

myLayer = folium.raster_layers.WmsTileLayer(URL,Layer,name='ASTER DEM',transparent=False,overlay=False)
myLayer.add_to(macarte)

Layer  = 'GPW_Population_Density_2020'
myLayer = folium.raster_layers.WmsTileLayer(URL,Layer,name='Pop Density',transparent=True,overlay=True, opacity=0.5)
myLayer.add_to(macarte)

mytile=folium.raster_layers.TileLayer(overlay=True, opacity=0.6)
mytile.add_to(macarte)


folium.LayerControl().add_to(macarte)

#save to html file
macarte.save('f_2.html')
