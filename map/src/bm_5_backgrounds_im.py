# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import rcParams
import cartopy.crs as ccrs

rcParams['font.size']=6


fig = plt.figure(figsize=(20,10))
ax1=fig.add_subplot(221)
maCarte=Basemap(ax=ax1)
maCarte.bluemarble(scale=0.5)
ax1.set_title('Basemap Bluemarble')

ax2=fig.add_subplot(222)
maCarte=Basemap(ax=ax2)
maCarte.etopo(scale=0.5)
ax2.set_title('Basemap Etopo 5')

ax3=fig.add_subplot(223)
maCarte=Basemap(ax=ax3)
maCarte.shadedrelief(scale=0.5)
ax3.set_title('Basemap Shaded relief')

ax4=fig.add_subplot(224, projection=ccrs.PlateCarree())
ax4.stock_img()
ax4.set_title('Cartopy Shaded Relief')

plt.savefig('../figures/bm5_backgrounds_im.pdf', bbox_inches='tight')

plt.show()
