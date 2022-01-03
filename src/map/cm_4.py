#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
"""
cm_4.py

Map limits
here again the limit of cartopy lies in the absence
of labels for lat and lon in this projection style
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from matplotlib.path import Path
from matplotlib import rcParams
import numpy as np

rcParams['font.size']=8


fig = plt.figure(figsize=(10/2.54,10/2.54))
# Define the projection
proj = ccrs.UTM(zone=31)

#define axis
ax = fig.add_subplot(111, projection = proj)
# everything is in this line !
ax.set_extent((-5,9,42,52))


ax.coastlines(resolution='10m') # best possible resolution
g = ax.gridlines(color = 'gray' ,linestyle = '-.', xlocs= range(-7,11,2) , ylocs = range(40,56,2), draw_labels=True)



plt.savefig('../../figures/cm_4.svg',bbox_inches='tight')

plt.show()
