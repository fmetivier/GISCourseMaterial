# -*- coding: utf-8 -*
"""
cm_5_SVZ.py

Draw map of the time variation of the Z component of the magnetic field
Courtesy of A. Fournier

"""

import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

SVZ = np.loadtxt('../include/txt/SVZ.txt')

#size of the grid over the sphere
nlon  =  61 # 61 points in longitude
nlat  =  31 # 31 points in colatitude

#coordinates of SVZ points
colat  =  np.linspace(1.,  179.,  nlat,  endpoint = True) # we exclude the poles
longi = np.linspace(-180.,  180.,  nlon,  endpoint = True)

my_crs = ccrs.PlateCarree()
fig  =  plt.figure(figsize = (20, 10))
ax = fig.add_subplot(111, projection = ccrs.Robinson(central_longitude=180))

ax.coastlines()
#~ ax.gridlines(draw_labels=True, xlocs=range(-180,181,60), ylocs=range(-90,91,30))
ax.gridlines(xlocs=range(-180,181,60), ylocs=range(-90,91,30))


#transform coordinates and reshape SVZ into a 2D grid
latit  =  90 - colat
lons,  lats  =  np.meshgrid(longi, latit)
svz2d  =   np.reshape(SVZ,  (nlat, nlon) )

#define color levels
maxsvz  =  max(np.abs(SVZ))
clevs  =  np.linspace(-maxsvz,  maxsvz,  11,  endpoint = True)

#plot SVZ
cs1  =  ax.contour(lons,  lats,  svz2d,  clevs,  colors = 'k',  linewidth = 0.5, transform = my_crs)
cs2  =  ax.contourf(lons,  lats,  svz2d,  clevs,  cmap = plt.cm.RdBu_r, transform = my_crs)

#add colorbar
axins = inset_axes(ax,
                   width="1%",  # width = 5% of parent_bbox width
                   height="100%",  # height : 50%
                   loc='lower left',
                   bbox_to_anchor=(1.05, 0., 1, 1),
                   bbox_transform=ax.transAxes,
                   borderpad=0,
                   )

cb  =  plt.colorbar(cs2, cax=axins)
cb.set_label('nT / yr')

plt.savefig('../figures/cm_5_SVZ.pdf',bbox_inches='tight')
plt.show()
