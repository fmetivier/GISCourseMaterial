#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:21:19 2020

@author: metivier
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:16:23 2020

@author: metivier

folium maps 

using  Cluster Markers to plot the place where students where
the year before registering at IPGP

"""

import folium
from folium.plugins import MarkerCluster

from sqlalchemy import create_engine
import pandas as pd
import numpy as np

#create the map
macarte = folium.Map(location=[46.5,2.5], zoom_start=6)

engine = create_engine("mysql://root:iznogod01@localhost/Parcours")

sql="select cp, prenom from IdentiteTbl i inner join ParcoursTbl p on i.idetudiant=p.idetudiant where annee=anneeufr-1 and pays='France'"

stud = pd.read_sql(sql,engine)

f=open('../include/data/laposte_hexasmal_1.csv')
line=f.readline()
lines=f.readlines()

codep=[]
lat=[]
lon=[]
for l in lines:
    d=l.split(',')
    codep.append(d[2])
    lat.append(d[5])
    lon.append(d[6].strip('\n'))
    
data={'cp':codep, 'lat':lat, 'lon':lon}

cp = pd.DataFrame(data,columns=['cp','lat','lon'])
ccp= cp.drop_duplicates('cp')

merged=stud.set_index('cp').join(ccp.set_index('cp'))
merged=merged.dropna()

mc = MarkerCluster()
for index, row in merged.iterrows():
    mc.add_child(folium.Marker(location=[row['lat'],row['lon']],popup=row['prenom']))

    
macarte.add_child(mc)




macarte.save('f_4.html')