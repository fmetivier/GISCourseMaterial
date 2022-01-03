#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bm_1.py

simple first map (taken from basemap tutorial)
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#Define the map object
map  =  Basemap()

#draw the coastlines
map.drawcoastlines()

plt.show()
