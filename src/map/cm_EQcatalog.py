"""
Download the earthquake catalogue of USGS
get the M>=5 earthquakes of the last 30 days
and plot them
"""

import requests
import json
import cartopy.crs as ccrs
import numpy as np
import matplotlib.pyplot as plt
from datetime import date, timedelta
from mpl_toolkits.axes_grid1.inset_locator import inset_axes




time_interval = 30 #decide the time interval (in days) you wish to search in the catalogue
today = date.today() #get today's date
startday = today - timedelta(days=time_interval) # get the starting date of seach



et=today.strftime("%Y-%m-%d")
st=startday.strftime("%Y-%m-%d")
minmag='5'

turl= "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=%s&endtime=%s&minmag=%s" % (st,et,minmag)

response = requests.get(turl)

data = response.json()

lat=[]
lon=[]
depth=[]
mag=[]

for f in data['features']:
	mag.append( f['properties']['mag'] )
	coord = f['geometry']['coordinates']
	lon.append(coord[0])
	lat.append(coord[1])
	depth.append(coord[2])


fig = plt.figure(figsize = (15, 7))
ax = fig.add_subplot(111, projection = ccrs.PlateCarree(central_longitude=180))
ax.coastlines()
ax.gridlines(xlocs=range(-180,181,60),ylocs=range(-90,91,30))
ax.set_xticks(range(-180,181,60))
ax.set_yticks(range(-90,91,30))
ax.set_extent((-180,180,-90,90))

sc = ax.scatter(x = lon, y = lat, s = np.exp(np.array(mag)), c = -np.array(depth), transform=ccrs.PlateCarree(), edgecolors='grey', zorder=4)

ax.set_title("Start:%s; End:%s" % (st,et))
#color bar
axins = inset_axes(ax,
                   width="2%",  # width = 5% of parent_bbox width
                   height="100%",  # height : 50%
                   loc='lower left',
                   bbox_to_anchor=(1.05, 0., 1, 1),
                   bbox_transform=ax.transAxes,
                   borderpad=0,
                   )

cbar = plt.colorbar(sc, cax=axins)
cbar.set_label('Depth')


#phantom plot
for i in range(3):
    plt.scatter([],  [],  s = np.exp(i+5),  edgecolor = 'k', facecolor = 'none', label = str(i+5))

#legend
h,  l  =  plt.gca().get_legend_handles_labels()
ax.legend(h,  l, title = "Magnitude", labelspacing = 2, borderpad = 3, frameon = True,  numpoints = 1,  ncol = 5,  framealpha = 0.9,  loc = 'lower left')

plt.savefig('../../figures/cm_EQ30.svg', bbox_inches='tight')
plt.show()
