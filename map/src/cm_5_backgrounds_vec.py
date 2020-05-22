# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import rcParams
import cartopy.crs as ccrs
import cartopy.feature as ft


rcParams['font.size']=6

fig=plt.figure(figsize=(15/2.54,15/2.54))


ax=fig.add_subplot(211,projection=ccrs.PlateCarree())
#in the case of world maps you can use the predefined datasets of NaturalEarth
ax.add_feature(ft.LAND)
ax.add_feature(ft.OCEAN)
ax.add_feature(ft.LAKES)
ax.add_feature(ft.RIVERS)
ax.add_feature(ft.BORDERS, linestyle='--', edgecolor='gray', linewidth=0.5)

ax.set_title('Natural Earth 110m')

ax2=fig.add_subplot(212,projection=ccrs.PlateCarree())
ax2.set_xlim(-10,50)
ax2.set_ylim(30,60)

# in the case of 50 and 10m datasets you have to define the features from the NaturalEarthFeature
land_50m = ft.NaturalEarthFeature('physical', 'land', '50m', edgecolor='k', facecolor=ft.COLORS['land'])
ocean_50m = ft.NaturalEarthFeature('physical', 'ocean', '50m', edgecolor='face', facecolor=ft.COLORS['water'])
lakes_50m = ft.NaturalEarthFeature('physical', 'lakes', '50m', edgecolor='face', facecolor=ft.COLORS['water'])
rivers_50m = ft.NaturalEarthFeature('physical', 'rivers_lake_centerlines', '50m', edgecolor=ft.COLORS['water'], facecolor='none')

ax2.add_feature(land_50m)
ax2.add_feature(ocean_50m)
ax2.add_feature(lakes_50m)
ax2.add_feature(rivers_50m)

ax2.set_title('Natural Earth 50m')


plt.savefig('../figures/cm5_backgrounds_vec.pdf', bbox_inches='tight')
plt.show()
