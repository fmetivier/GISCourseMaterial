#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cm_17.py

Purpose :
read shapefile
regrid equipotential head lines
calculate streamlines
plot

cartopy version
"""
import geopandas

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.interpolate import griddata  # this one not the scipy one

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader

from owslib.wmts import WebMapTileService

import numpy as np

# open shapefile
deps = geopandas.read_file(
    "../../Data/map/shapefiles/Aquitaine/Isopiezes_mio-plio-quaternaire_latlon.shp"
)

print(deps.head())

X = []
Y = []
Z = []
for i in range(len(deps["geometry"])):

    try:
        # print deps["geometry"][i].geom_type
        if deps["geometry"][i].geom_type == "LineString":
            x, y = deps["geometry"][i].coords.xy
            z = deps["COTE_mNGF"][i] * np.ones(len(x))
            X = np.hstack((X, x))
            Y = np.hstack((Y, y))
            Z = np.hstack((Z, z))

        elif deps["geometry"][i].geom_type == "MultiLineString":
            for line in deps["geometry"][i]:
                x, y = line.coords.xy
                z = deps["COTE_mNGF"][i] * np.ones(len(x))
                X = np.hstack((X, x))
                Y = np.hstack((Y, y))
                Z = np.hstack((Z, z))
    except:
        print(i)
        pass


xs = np.linspace(min(X), max(X), 400)
ys = np.linspace(min(Y), max(Y), 400)
xx, yy = np.meshgrid(xs, ys)
zz = griddata(
    np.column_stack((X, Y)), Z, (xx, yy)
)  # grid data this method does NO EXTRAPOLATION which leads to a masked array

print(np.shape(zz))
v, u = np.gradient(
    zz
)  # calculate gradient BEWARE lines (y-direction) first,  columns (x-direction) second


# Define figure size and basemap
# URL of NASA GIBS
URL = "http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi"
wmts = WebMapTileService(URL)

# Layers for MODIS true color and snow RGB
layer = "Landsat_WELD_CorrectedReflectance_Bands157_Global_Annual"

date_str = "1999-08-16"

# Plot setup
plot_CRS = ccrs.PlateCarree()
geodetic_CRS = ccrs.Geodetic()


x0, y0 = plot_CRS.transform_point(-1.43, 44.15, geodetic_CRS)
x1, y1 = plot_CRS.transform_point(-0.69, 44.68, geodetic_CRS)

fig = plt.figure(figsize=(20, 20))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())


ax.set_xlim(-1.5, -0.5)
ax.set_ylim(44, 45)

ax.gridlines(
    draw_labels=True,
    xlocs=[-1.5, -1, -0.5, 0],
    ylocs=[44, 44.5, 45],
    color="white",
    linestyle="--",
)
ax.coastlines(resolution="10m")

ax.add_wmts(wmts, layer, wmts_kwargs={"time": date_str})

c = ax.contourf(
    xx, yy, zz, [10, 20, 30, 40, 50, 60, 70, 80], alpha=0.4, transform=plot_CRS
)
ax.contour(xx, yy, zz, [10, 20, 30, 40, 50, 60, 70, 80], transform=plot_CRS)
ax.streamplot(
    xx, yy, -u, -v, density=1, color="red", arrowsize=2.5, transform=plot_CRS
)  # streamlines $\mathbf{U}_{Darcy} \propto - \mathbf{grad}(h)$
cb = plt.colorbar(c, shrink=0.8)
cb.set_label("Hauteur piézométrique")

# Print some information
x, y = (-1.1681992, 44.45807)
ax.text(x, y, "Etang de Cazaux", color="w")
x, y = (-1.1749838, 44.345)
ax.text(x, y, "Etang de Parentis", color="w")
x, y = (-1.4, 44.7)
ax.text(x, y, u"Océan atlantique", color="w", rotation=90, fontsize=30)
x, y = (-1.184541, 44.668606)
ax.text(x, y, "Bassin d'Arcachon", color="w")


# Print some information
x, y = (-1.1681992, 44.45807)
ax.text(x, y, "Etang de Cazaux", color="w", transform=plot_CRS)
x, y = (-1.1749838, 44.345)
ax.text(x, y, "Etang de Parentis", color="w", transform=plot_CRS)
x, y = (-1.4, 44.7)
ax.text(
    x, y, u"Océan atlantique", color="w", rotation=90, fontsize=30, transform=plot_CRS
)
x, y = (-1.184541, 44.668606)
ax.text(x, y, "Bassin d'Arcachon", color="w", transform=plot_CRS)

# plt.savefig("../figures/cm_shp2grid.pdf",bbox_inches='tight')
plt.show()
