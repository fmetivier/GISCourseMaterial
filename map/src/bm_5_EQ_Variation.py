#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
bm_5_EQ_Variation.py 2019

simple first map (taken from basemap tutorial)
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

engine = create_engine('mysql://root:iznogod01@localhost/quakes')



#Define the map object
map  =  Basemap()


#Fill the globe with a blue color
map.drawmapboundary(fill_color = 'aqua')

#Fill the continents with the land color
map.fillcontinents(color = 'lightgray', lake_color = 'aqua')

#draw the coastlines
map.drawcoastlines()

map.drawmeridians(range(-180,181,40),color='k',dashes=[4,2],labels=[0,0,0,1],fontsize=10)
map.drawparallels(range(-90,91,30),color='k',dashes=[4,2],labels=[1,0,0,0],fontsize=10)

df = pd.read_csv("/home/metivier/Latex/cours/sig/2019-2020/sql/bases/quakes/quakes4plus.csv")

df[100001:].to_sql('catalogue',con=engine, if_exists='append', index=False)

x,y=map(df['longitude'][df['mag']>=7].tolist(),df['latitude'][df['mag']>=7].tolist())
map.plot(x,y,'ro',markersize=6,label='M>=7')
x,y=map(df['longitude'][df['mag']>=8].tolist(),df['latitude'][df['mag']>=8].tolist())
map.plot(x,y,'bo',markersize=10,label='M>=8')
x,y=map(df['longitude'][df['mag']>=9].tolist(),df['latitude'][df['mag']>=9].tolist())
map.plot(x,y,'go',markersize=14,label='M>=9')

plt.legend()


plt.show()
