import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import cm
import matplotlib.patches as pch
import MySQLdb
import matplotlib.contour as con
import matplotlib as mpl

#CONNEXION
#get your connection identifiers
f=open('../../python-mysql/src/identifiers.txt')
mylogin=f.readline().strip('\n')
mypass=f.readline().strip('\n')

# name of the database you whish to connect to
base = 'Parcours'
# establish connection
conn = MySQLdb.connect(host = "localhost", user = mylogin, passwd = mypass, db = base)
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

fig = plt.figure(figsize = (20, 20))
ax = fig.add_subplot(111)
map = Basemap(llcrnrlon = -5, llcrnrlat = 42, urcrnrlon = 9., urcrnrlat = 52., resolution = 'i',  projection = 'tmerc',  lat_0  =  46,  lon_0  =  2.5)

map.readshapefile("../include/shapefiles/DEPARTEMENTS/DEPARTEMENT_LATLON", "dep")

for info,  shape in list(zip(map.dep_info,  map.dep)):
	if info['CODE_DEPT'] in keys:
		x, y = list(zip(*shape))
		p = pch.Polygon(list(zip(x, y)), edgecolor = 'k', facecolor = cmap(OYB[info['CODE_DEPT']]/maxval))
		print(p)
		ax.add_artist(p)


# make some space at the bottom of the the image to place the colorbar
divider = make_axes_locatable(ax)
cax = divider.append_axes("bottom", size="5%", pad=0.05)

#create the customcontinuous  colorbar
norm = mpl.colors.Normalize(1,maxval)
cb1 = mpl.colorbar.ColorbarBase(cax, cmap = cmap, norm = norm, orientation = 'horizontal')
cb1.set_label(u"Nombre d'étudiants")

plt.show()
