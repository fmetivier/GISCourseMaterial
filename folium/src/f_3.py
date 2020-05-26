#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:16:23 2020

@author: metivier

folium maps

Earthquakes of the last seven days plotted on top of three layers
ASTER GDEM Shaded Relief
Population density
Open street map tiles

"""
import folium
import requests

import matplotlib.cm as cm
from matplotlib.colors import rgb2hex
from datetime import date, timedelta, datetime



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

#get the data
time_interval = 7 #decide the time interval (in days) you wish to search in the catalogue
today = date.today() #get today's date
startday = today - timedelta(days=time_interval) # get the starting date of seach



et=today.strftime("%Y-%m-%d")
st=startday.strftime("%Y-%m-%d")
minmag='1'

turl= "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=%s&endtime=%s&minmag=%s" % (st,et,minmag)

response = requests.get(turl)

data = response.json()

cmap = cm.get_cmap('coolwarm')


#plot eartqhuakes as circles with individual popup info boxes.
for f in data['features']:
    mag =  f['properties']['mag']
    coord = f['geometry']['coordinates']
    c=cmap(1-coord[2]/500.)
    comment = "<p style = 'width:200px;'>"

    edic = f['properties']
    comment += "<b>%s</b>: %s<br>" % ('Time',datetime.fromtimestamp(edic['time']/1000).strftime('%c'))
    comment += "<b>%s</b>: %s<br>" % ('Place', edic['place'])
    comment += "<b>%s</b>: %s<br>" % ('Magnitude', edic['mag'])
    comment += "<b>%s</b>: %s<br>" % ('Depth (km)', coord[2])
    comment += "<a href=%s>More Info</a><br>" % edic['url']
    comment += "</p>"

    folium.CircleMarker(
        location=[coord[1],coord[0]],
        radius=5+2**(mag-1), #radius = f(mag)
        popup=comment ,
        color='black',
        weight=1, # circle line width !
        fill=True,
        fill_color=rgb2hex(c)# color=f(depth)
    ).add_to(macarte)


#save to html file
macarte.save('f_3.html')
