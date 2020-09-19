#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cm_1_2.py

projection vs transform
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig  = plt.figure(figsize=(5,3))
# the great interest with cartopy is its ability to be intergrated into the pyplot environnement
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

#this becomes necessary if you plot data that is not in the same projection
ax.set_xlim(-100,30)
ax.set_ylim(0,90)

#add coastlines
ax.coastlines()

#Point 1
LON_P, LAT_P = (2.4, 48.8)
ax.plot(LON_P,LAT_P,'bo', transform=ccrs.Geodetic())

LON_NY, LAT_NY = -75, 43
ax.plot(LON_NY,LAT_NY,'ro', transform=ccrs.Geodetic())

ax.plot([LON_P,LON_NY],[LAT_P,LAT_NY],'--',transform=ccrs.PlateCarree())
ax.plot([LON_P,LON_NY],[LAT_P,LAT_NY],'-',transform=ccrs.Geodetic())

plt.savefig('../figures/OneTrajectory.pdf',bbox_inches='tight')


plt.show()
