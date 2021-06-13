#!/usr/bin/env python3
# -*- coding utf-8 -*-
"""
cm_2.py

Change  projection and add gridlines
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
from matplotlib import rcParams

rcParams['font.size']=6

fig = plt.figure(figsize=(15/2.54,10/2.54))

# a first projection
ax1 = fig.add_subplot(211, projection=ccrs.Mercator(
                                    central_longitude=0))

ax1.coastlines(resolution='110m') # resolutions available 50m and 10m

gl = ax1.gridlines(draw_labels=True)




#a second projection
ax2 = fig.add_subplot(212, projection=ccrs.Mollweide(
                                    central_longitude=180))

# features can be used to include different kinds of back_grounds
ax2.coastlines(resolution='110m')
ax2.gridlines()



plt.savefig('../figures/cm_2.pdf')
plt.show()
