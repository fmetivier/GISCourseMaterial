#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: metivier

folium maps

Transform plot GeoJson polygons
and add information un Popups

"""

import folium
import numpy as np
import pandas

from ShapeTransform import shape_to_geojson

def big_style(x):
    """
    samples tyle function
    """
    if x['properties']['POP_EST'] <= 1e6 :
        stdic = {'fillColor': 'darkgreen', "color":'black', "opacity":0.4}
    elif x['properties']['POP_EST'] <= 1e7 and x['properties']['POP_EST'] > 1e6:
        stdic = {'fillColor': 'green', "color":'black', "opacity":0.4}
    elif x['properties']['POP_EST'] <= 1e8 and x['properties']['POP_EST'] > 1e7:
        stdic = {'fillColor': 'yellow', "color":'black', "opacity":0.4}
    elif x['properties']['POP_EST'] <= 1e9 and x['properties']['POP_EST'] > 1e8:
        stdic = {'fillColor': 'orange', "color":'black', "opacity":0.4}
    elif x['properties']['POP_EST'] > 1e9:
        stdic = {'fillColor': 'red', "color":'black', "opacity":0.4}
    return stdic

macarte = folium.Map(location=[46.5,2.5], zoom_start=3)

data, df = shape_to_geojson( '../../map/include/shapefiles/ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp' )

#add some information because it's  a mess to get the legend
JsonLayer = folium.GeoJson(data,style_function=big_style,name='Population')
JsonPop = folium.features.GeoJsonPopup(fields=['NAME','POP_EST'],aliases = ["Country","Population"]).add_to(JsonLayer)
JsonLayer.add_to(macarte)


folium.LayerControl().add_to(macarte)
macarte.save('f_5.html')
