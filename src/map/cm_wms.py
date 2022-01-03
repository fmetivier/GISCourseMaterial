"""
Use wmts servers using cartopy
"""
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
from owslib.wmts import WebMapTileService

import cartopy.crs as ccrs


def main():

	# Plot setup
	plot_CRS  =  ccrs.PlateCarree()

	# URL of NASA GIBS
	URL  =  'http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi'
	wmts  =  WebMapTileService(URL)


	fig  =  plt.figure(figsize = (15, 22)) #must be reasonably big because of the sampling of the image during savefig.
	ax  =  fig.add_subplot(311,  projection = plot_CRS)

	# Blue Marble with bathymetry
	layer  =  'BlueMarble_ShadedRelief_Bathymetry'
	ax.add_wmts(wmts,  layer)
	ax.gridlines(draw_labels = True, xlocs = range(-180, 181, 60), ylocs = range(-90, 91, 30), color = 'w', linestyle = '-.')

	ax2  =  fig.add_subplot(312,  projection = plot_CRS)

	layer  =  'ASTER_GDEM_Color_Shaded_Relief'
	ax2.add_wmts(wmts,  layer)

	ax2.coastlines(resolution = '110m')
	ax2.gridlines(draw_labels = True, xlocs = range(-180, 181, 60), ylocs = range(-90, 91, 30), color = 'w', linestyle = '-.')


	ax3  =  fig.add_subplot(313,  projection = plot_CRS)

	layer = 'GPW_Population_Density_2020'
	ax3.add_wmts(wmts,  layer)

	ax3.coastlines(resolution = '110m')
	ax3.gridlines(draw_labels = True, xlocs = range(-180, 181, 60), ylocs = range(-90, 91, 30), color = 'k', linestyle = '-.')

	plt.savefig('../../figures/cm_wmts_1.svg', bbox_inches = 'tight')

	plt.show()

def other_examples():


	# Plot setup
	plot_CRS  =  ccrs.PlateCarree()

	fig  =  plt.figure(figsize = (10, 10))
	ax  =  fig.add_subplot(111,  projection = plot_CRS)


	# URL of NASA GIBS
	URL  =  'http://gibs.earthdata.nasa.gov/wmts/epsg4326/best/wmts.cgi'
	wmts  =  WebMapTileService(URL)

	# Layers for MODIS true color and snow RGB
	layer  =  'Landsat_WELD_CorrectedReflectance_Bands157_Global_Annual'

	date_str  =  '1999-08-16'


	ax.set_xlim(-5, 7)
	ax.set_ylim(42, 52)

	ax.add_wmts(wmts,  layer,  wmts_kwargs = {'time': date_str})

	ax.coastlines(resolution = '10m', color = 'w')
	ax.gridlines(draw_labels = True, xlocs = range(-5, 8, 2), ylocs = range(42, 53, 2), color = 'w', linestyle = '--')

	plt.savefig('../../figures/cm_France_Landsat.svg', bbox_inches = 'tight')
	plt.show()


if __name__  ==  '__main__':
    main()
    other_examples()
