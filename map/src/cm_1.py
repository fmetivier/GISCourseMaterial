#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cm_1.py

simple first map (taken from cartopy tutorial)
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig  = plt.figure(figsize=(10/2.54,5/2.54))
# The great interest with cartopy is its ability to be intergrated into the pyplot environnement
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

#add coastlines
ax.coastlines()

plt.savefig('../figures/cm_1.pdf',bbox_inches='tight')
plt.show()
