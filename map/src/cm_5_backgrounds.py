# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import rcParams
import cartopy.crs as ccrs
import cartopy.feature as ft


rcParams['font.size']=6

fig=plt.figure(figsize=(15/2.54,15/2.54))
ax=fig.add_subplot(311, projection=ccrs.Mollweide())
ax.stock_img()
ax.set_title("Shaded Relief")

ax2=fig.add_subplot(312,projection=ccrs.PlateCarree())
ax2.add_feature(ft.LAND)
ax2.add_feature(ft.OCEAN)
ax2.add_feature(ft.LAKES)
ax2.add_feature(ft.RIVERS)
ax2.add_feature(ft.BORDERS)
ax2.set_xlim(-2,15)
ax2.set_ylim(40,60)

ax2.set_title('Natural Earth')

ax3=fig.add_subplot(313,projection=ccrs.Mollweide())
ax3.stock_img()
ax3.add_feature(ft.LAND,zorder=4)
ax3.add_feature(ft.LAKES,zorder=4)
ax3.add_feature(ft.RIVERS,zorder=4)

ax3.set_title('Mixed background')

plt.savefig('../figures/cm5_backgrounds.pdf', bbox_inches='tight')
plt.show()
