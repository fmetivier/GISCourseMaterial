"""
Reprojeter les données d'un shapefile avec cartopy
"""
import cartopy.crs as ccrs
import cartopy.io.shapereader as shapereader

import matplotlib.pyplot as plt
import numpy as np

reader = shapereader.Reader("./shapefiles/DEPARTEMENTS/DEPARTEMENT.SHP")

fig = plt.figure()
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
ax.coastlines(resolution='10m')
ax.gridlines(draw_labels=True)
ax.set_xlim(-5,10)
ax.set_ylim(40,55)

# epsg code replaces the complete projection definition. it can be found easily on the web
ax.add_geometries(reader.geometries(), crs=ccrs.epsg(2154))


plt.show()
