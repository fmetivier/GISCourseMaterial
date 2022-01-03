# -*- coding: utf-8 -*
"""
bm_5_SVZ.py

Draw map of the time variation of the Z component of the magnetic field
Courtesy of A. Fournier

pb with map.contour in python3
"""

import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

SVZ = np.loadtxt('../../Data/map/txt/SVZ.txt')

#size of the grid over the sphere
nlon  =  61 # 61 points in longitude
nlat  =  31 # 31 points in colatitude

#coordinates of SVZ points
colat  =  np.linspace(1.,  179.,  nlat,  endpoint = True) # we exclude the poles
#~ longi  =  np.linspace(0.,  360.,  nlon,  endpoint = True)
longi = np.linspace(-180.,  180.,  nlon,  endpoint = True)

plt.rc('legend',  fontsize = 30)
plt.rc('axes',  labelsize = 30, facecolor = 'None')
plt.rc('savefig',  facecolor = 'None',  edgecolor = 'None')

fig  =  plt.figure(figsize = (20, 10))
map  =  Basemap(projection='moll',lon_0=0)
map.drawcoastlines(linewidth  =  1.5)
#   draw lat/lon grid lines every 30 degrees.
map.drawmeridians(np.arange(0,  360,  30))
map.drawparallels(np.arange(-90,  90,  30))

#transform coordinates and reshape SVZ into a 2D grid
latit  =  90 - colat
lons,  lats  =  np.meshgrid(longi, latit)
x,  y  =  map(lons,  lats)
svz2d  =   np.reshape(SVZ,  (nlat, nlon) )

#define color levels
maxsvz  =  max(np.abs(SVZ))
clevs  =  np.linspace(-maxsvz,  maxsvz,  11,  endpoint = True)

#plot SVZ
cs1  =  map.contour(x,  y,  svz2d,  clevs,  colors = 'k',  linewidth = 0.5)
cs2  =  map.contourf(x,  y,  svz2d,  clevs,  cmap = plt.cm.RdBu_r)

#add colorbar
cb  =  map.colorbar(cs2, "bottom",  size = "5%",  pad = "2%")
font_size  =  24 # Adjust as appropriate.
cb.ax.tick_params(labelsize = font_size)
cb.set_label('nT / yr')

# plt.savefig("../../figures/bm_5_SVZ.svg",bbox_inches='tight')
plt.show()
