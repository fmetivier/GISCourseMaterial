import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature

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
maxval = 0
for r in rows:
   OYB[r[0]] = float(r[1])
   keys.append(r[0])
   if float(r[1])>maxval:
	   maxval = float(r[1])

print( maxval )
print( keys )

cmap = cm.get_cmap('viridis')
#initialize figure and axis with projection
fig = plt.figure(figsize = (20, 20))
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
for feature in features:
	dep = feature.attributes['CODE_DEPT']
	if  dep in keys:
		ax.add_geometries([feature.geometry], facecolor = cmap(OYB[dep]/maxval), crs = ccrs.PlateCarree(),  edgecolor = 'k')
	else:
		ax.add_geometries([feature.geometry], facecolor = 'w', crs = ccrs.PlateCarree(),  edgecolor = 'k')

# make some space at the bottom of the the image to place the colorbar
axins = inset_axes(ax,
                   width="2%",  # width = 5% of parent_bbox width
                   height="100%",  # height : 50%
                   loc='lower left',
                   bbox_to_anchor=(1.05, 0., 1, 1),
                   bbox_transform=ax.transAxes,
                   borderpad=0,
                   )

#create the customcontinuous  colorbar
norm = mpl.colors.Normalize(1,maxval)
cb1 = mpl.colorbar.ColorbarBase(axins, cmap = cmap, norm = norm, orientation = 'vertical')
cb1.set_label(u"Nombre d'étudiants")

plt.show()
