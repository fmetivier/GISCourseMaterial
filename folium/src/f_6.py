#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: metivier

folium maps

Plot Choropleth from a shapefile


"""

import folium
import  matplotlib.cm as cm
from matplotlib.colors import rgb2hex
import numpy as np
import pandas

from ShapeTransform import shape_to_geojson


macarte = folium.Map(location=[46.5,2.5], zoom_start=3)

data, df = shape_to_geojson( '../../map/include/shapefiles/ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp' )


# Populations extends over orders if magnitude so we need to
# prepare the data a little
df = df.fillna(value={'POP_EST': 1}) # get rid of nans
df = df.replace({'POP_EST' : 0}, 1) # replace 0 values
df['POP_EST'] = np.log10(df['POP_EST']) # go to log10 scale

#In the end plot
cp = folium.Choropleth(data,df,columns=['ISO_A3','POP_EST'],key_on='feature.properties.ISO_A3',\
    fill_color='PuRd',name='Population',legend_name='Populaton (log scale)').add_to(macarte)


folium.LayerControl().add_to(macarte)
macarte.save('f_6.html')
