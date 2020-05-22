#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
cm_16.py

Draw equipotential (isopieze map) lines of the Plio-quaternary aquifer
on top of a Landast ETM view of the Lakes of Landes south of Arcachon.
The ETM image comes from the earthdata web service

cartopy version
"""

#libraries
import geopandas

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader

from owslib.wmts import WebMapTileService


def convert_shape():
    #read the file
    piezo = geopandas.read_file("../include/shapefiles/Aquitaine/Isopiezes_mio-plio-quaternaire.shp")


    print(piezo.head())
    print(piezo.crs)
    print(" ================ ")

    #test to get rid of null or empty values in the record (else the conversion fails)
    piezo =  piezo[piezo['geometry'].notnull()]
    #all is here the Plate carree definition
    piezo2 = piezo.to_crs({'init': 'epsg:4326'})
    print(piezo2.head())
    print(piezo.crs)
    print(" ================= ")


    #save the file
    piezo2.to_file("./shapefiles/Aquitaine/Isopiezes_mio-plio-quaternaire_latlon.shp",encoding='utf-8')


def map_piezo():

	# URL of NASA GIBS
	URL = 'http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi'
	wmts = WebMapTileService(URL)

	# Layers for MODIS true color and snow RGB
	layer = 'Landsat_WELD_CorrectedReflectance_Bands157_Global_Annual'

	date_str = '1999-08-16'

	# Plot setup
	plot_CRS = ccrs.PlateCarree()
	geodetic_CRS = ccrs.Geodetic()


	x0, y0 = plot_CRS.transform_point(-1.43, 44.15, geodetic_CRS)
	x1, y1 = plot_CRS.transform_point(-0.69, 44.68, geodetic_CRS)

	fig = plt.figure(figsize = (20, 20))
	ax = fig.add_subplot(111, projection=ccrs.PlateCarree())


	ax.set_xlim(-1.5,0)
	ax.set_ylim(44,45)

	ax.gridlines(draw_labels=True, xlocs=[-1.5,-1,-0.5,0], ylocs=[44,44.5,45], color='white', linestyle='--')
	ax.coastlines(resolution='10m')

	ax.add_wmts(wmts, layer, wmts_kwargs={'time': date_str})



	# Open shapefile
	reader = shpreader.Reader("../include/shapefiles/Aquitaine/Isopiezes_mio-plio-quaternaire_latlon.shp")
	features = reader.records()


	# retrieve the polylines and plot them using different colors
	cmap = cm.get_cmap('YlOrRd')
	for f in features:
		c = cmap(float(f.attributes['COTE_mNGF'])/100) #100 is assumed to be the maximum piezometric head in the region
		print(f.geometry)
		#~ ax.plot(x, y, '-', linewidth = 2, color = c, label = info['COTE_mNGF'])
		ax.add_geometries([f.geometry], edgecolor = c, facecolor='none', linewidth=2, label = f.attributes['COTE_mNGF'], crs=plot_CRS)


	# Print some information
	x, y = (-1.1681992, 44.45807)
	ax.text(x, y, "Etang de Cazaux", color = 'w', transform=plot_CRS)
	x, y = (-1.1749838, 44.345)
	ax.text(x, y, 'Etang de Parentis', color = 'w', transform=plot_CRS)
	x, y = (-1.4, 44.7)
	ax.text(x, y, u"Océan atlantique", color = 'w', rotation = 90, fontsize = 30, transform=plot_CRS)
	x, y = (-1.184541, 44.668606)
	ax.text(x, y, "Bassin d'Arcachon", color = 'w', transform=plot_CRS)


	axins = inset_axes(ax,
					   width="2%",  # width = 5% of parent_bbox width
					   height="100%",  # height : 50%
					   loc='lower left',
					   bbox_to_anchor=(1.05, 0., 1, 1),
					   bbox_transform=ax.transAxes,
					   borderpad=0,
					   )

	#create the customcontinuous  colorbar
	norm = mpl.colors.Normalize(1,100)
	cb1 = mpl.colorbar.ColorbarBase(axins, cmap = cmap, norm = norm, orientation = 'vertical')
	cb1.set_label(u"hauteur piézométrique")




	# Show
	plt.show()


map_piezo()
