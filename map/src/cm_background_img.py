"""
Use images to create a background in cartopy.
"""

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import os

#define the environment variable that records where the images are stored
os.environ["CARTOPY_USER_BACKGROUNDS"] = "../include/raster/Background/"

fig = plt.figure(figsize=(13,6.2))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

#call the image. All informations, name, resolution are stored in an images.json file.
ax.background_img(name='BM', resolution='low')

ax.gridlines(draw_labels=True, color='w', linestyle='-.')

plt.savefig('../figures/cm_BM_background.pdf',bbox_inches='tight')

plt.show()
