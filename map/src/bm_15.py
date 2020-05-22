#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
bm_15.py

Map the French départements with the result of a query performed in
the MySQL Parcours database.

basemap version
"""

#libraries
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.patches import Patch
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch
import numpy as np
from matplotlib import cm
import MySQLdb # msyql api

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
ax = fig.add_subplot(111)

#MAP
map = Basemap(llcrnrlon = -5, llcrnrlat = 42, urcrnrlon = 9., urcrnrlat = 52., \
resolution = 'i',  projection = 'tmerc',  lat_0  =  46,  lon_0  =  2.5)

#background maps
map.drawmapboundary(fill_color = 'aqua')
map.fillcontinents(color = 'w', lake_color = 'aqua')
map.drawcoastlines()

#the scale
#the scale
map.drawmeridians(range(-5, 10, 2), color = 'k', dashes = [4,  2], \
 labels = [0, 0, 0, 1], linewidth = 0.5)
map.drawparallels(range(40, 54, 2), color = 'k', dashes = [4,  2], \
labels = [1, 0, 1, 0], linewidth = 0.5)

#background department map
map.readshapefile("../include/shapefiles/DEPARTEMENTS/DEPARTEMENT_LATLON", "deps")

#COLORMAP
#selects and colors the departements
cmap = cm.get_cmap('viridis')
c = (0.9, 0.9, 0.9)
for info,  shape in list(zip(map.deps_info,  map.deps)):
    if info['CODE_DEPT'] in keys:
        if OYB[info['CODE_DEPT']]>50:
            c = cmap(0.99)
        elif OYB[info['CODE_DEPT']] >=  10 and OYB[info['CODE_DEPT']] < 50:
            c = cmap(0.75)
        elif OYB[info['CODE_DEPT']] >=  5 and OYB[info['CODE_DEPT']] < 10:
            c = cmap(0.5)
        elif OYB[info['CODE_DEPT']] >=  1  < 5:
            c = cmap(0.25)
    else:
        c = (0.9, 0.9, 0.9)
    p = Polygon(np.array(shape),  closed = True)
    ax.add_collection(PatchCollection([p], edgecolor = 'k', \
     linewidth = 0.5,  facecolor = c, zorder = 2))

print( shape )

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
