#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
bm_15.py

Map the French départements with the result of a query performed in
the MySQL Parcours database.

cartopy version
"""

#libraries

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl

from matplotlib.patches import Patch
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature

import numpy as np

import MySQLdb

#CONNEXION
# name of the database you whish to connect to
base = 'Parcours'
# establish connection
conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "iznogod01", db = base)
# create a curso object to send quaries
cursor = conn.cursor()
# write the SQL query
query = """select dep, count(*) as N from
        (select substr(cp,1,2) as dep
            from ParcoursTbl p inner join IdentiteTbl i on p.idetudiant=i.idetudiant
            where annee=anneeufr-1 and pays='France') as Q
        group by dep ;
    """
# execute the query
cursor.execute(query)
# fetch the dataset

#DICTIONNARY AND LIST
# We are going to create a dictionnary with the number of
# students as the value and the departemnt code as the key
# and a list of keys
OYB = {}
keys = []
rows  =  cursor.fetchall()
for r in rows:
   OYB[r[0]] = float(r[1])
   keys.append(r[0])


#FIGURE
fig = plt.figure()
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())

#set map limits
ax.set_xlim(-5,10)
ax.set_ylim(40,52)

# the first time it may take time to load into cache
ocean_50m = cfeature.NaturalEarthFeature('physical', 'ocean', '50m',
                                        edgecolor='face',
                                        facecolor=cfeature.COLORS['water'])

ax.add_feature(ocean_50m)

#you have to go beyhond the limits if you want the grid to extend until the limits.
#remind that up to now only PlateCarree offers the possibility to draw labels.
ax.gridlines(draw_labels=True,xlocs=range(-5,12,2), ylocs=range(40,54,2), zorder=4)

#get the department
reader= shpreader.Reader("../include/shapefiles/DEPARTEMENTS/DEPARTEMENT_LATLON.shp")
features = reader.records()

#loop through departments
#COLORMAP
#selects and colors the departements
cmap = cm.get_cmap('viridis')
c = (0.9, 0.9, 0.9)
for feature in features:
	dep = feature.attributes['CODE_DEPT']
	if dep in keys:
		if OYB[dep]>50:
			c = cmap(0.99)
		elif OYB[dep] >=  10 and OYB[dep] < 50:
			c = cmap(0.75)
		elif OYB[dep] >=  5 and OYB[dep] < 10:
			c = cmap(0.5)
		elif OYB[dep] >=  1  < 5:
			c = cmap(0.25)
		else:
			c = (0.9, 0.9, 0.9)

		ax.add_geometries([feature.geometry], edgecolor = 'k', \
		linewidth = 0.5,  facecolor = c, zorder = 2,crs=ccrs.PlateCarree())
	else:
		ax.add_geometries([feature.geometry], edgecolor = 'k', \
		linewidth = 0.5,  facecolor = 'white', zorder = 2,crs=ccrs.PlateCarree())


#and the legend
colors  =  [cmap(0.99),  cmap(0.75),  cmap(0.5),  cmap(0.25), (0.9, 0.9, 0.9)]
texts  =  ["$N \geq 50$",  "$10 \leq N < 50$", \
 	"$5 \leq N < 10$",  "$1\leq N<5$ ", "$N = 0$"]
patches  =  [ Patch(color = colors[i],  label = "{:s}".format(texts[i]) )\
 	for i in range(len(texts)) ]
plt.legend(handles = patches,  loc = 'lower left', \
 	title = 'Students')

#END
plt.show()
