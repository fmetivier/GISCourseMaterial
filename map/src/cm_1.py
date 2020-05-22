#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
cm_1.py

simple first map (taken from cartopy tutorial)
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig  = plt.figure(figsize=(10/2.54,5/2.54))
# the great interest with cartopy is its ability to be intergrated into the pyplot environnement
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

#add coastlines
ax.coastlines()


plt.show()
