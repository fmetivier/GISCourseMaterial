#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cm_1_2.py

projection vs transform
"""

import cartopy.crs as ccrs
import matplotlib.pyplot as plt

fig  = plt.figure(figsize=(5,3))
# the great interest with cartopy is its ability to be
# intergrated into the pyplot environnement
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

#this becomes necessary if you plot data that is not
# in the same projection
ax.set_xlim(-180,50)
ax.set_ylim(0,90)

#add coastlines
ax.coastlines()

#Point 1
UTM_X = 565718.
UTM_Y = 3980998.
ax.plot(UTM_X, UTM_Y, 'ro', transform = ccrs.UTM(11))

#Point 2
LON_X, LAT_X = (2.4, 48.8)
ax.plot(LON_X,LAT_X,'bo', transform=ccrs.Geodetic())


# plt.savefig('../../figures/OnePoint.svg',bbox_inches='tight')


plt.show()
