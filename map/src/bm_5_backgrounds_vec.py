# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import rcParams

rcParams['font.size']=6

fig=plt.figure(figsize=(20/2.54,10/2.54))

ax0=fig.add_subplot(221)
maCarte=Basemap(ax=ax0)
maCarte.drawmapboundary(fill_color = 'aqua')
maCarte.fillcontinents(color = 'lightgray', lake_color = 'aqua')
maCarte.drawcoastlines()
ax0.set_title('Résolution par défaut')


ax1=fig.add_subplot(222)
maCarte=Basemap(ax=ax1,llcrnrlon = -5, llcrnrlat = 42, urcrnrlon = 9., urcrnrlat = 52.,  projection = 'tmerc',  lat_0  =  46,  lon_0  =  2.5)
maCarte.drawmapboundary(fill_color = 'aqua')
maCarte.fillcontinents(color = 'w', lake_color = 'aqua')
maCarte.drawcoastlines()
maCarte.drawrivers(color='aqua')
maCarte.drawcountries(color='r',linestyle='--')
ax1.set_title('Résolution par défaut')


ax2=fig.add_subplot(223)
maCarte=Basemap(ax=ax2,llcrnrlon = -5, llcrnrlat = 42, urcrnrlon = 9., urcrnrlat = 52., resolution = 'i',  projection = 'tmerc',  lat_0  =  46,  lon_0  =  2.5)
maCarte.drawmapboundary(fill_color = 'aqua')
maCarte.fillcontinents(color = 'w', lake_color = 'aqua')
maCarte.drawcoastlines()
maCarte.drawrivers(color='aqua')
maCarte.drawcountries(color='r',linestyle='--')
ax2.set_title('Résolution intermédiaire')

ax3=fig.add_subplot(224)
maCarte=Basemap(ax=ax3,llcrnrlon = -5, llcrnrlat = 42, urcrnrlon = 9., urcrnrlat = 52., resolution = 'f',  projection = 'tmerc',  lat_0  =  46,  lon_0  =  2.5)
maCarte.drawmapboundary(fill_color = 'aqua')
maCarte.fillcontinents(color = 'w', lake_color = 'aqua')
maCarte.drawcoastlines()
maCarte.drawrivers(color='aqua')
maCarte.drawcountries(color='r',linestyle='--')

ax3.set_title('Résolution maximum')

plt.savefig('../figures/bm5_backgrounds_vec.pdf', bbox_inches='tight')

plt.show()
