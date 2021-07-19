#################################
# librairies
#################################

import folium
from sqlalchemy import create_engine

#################################
#create the map
#################################
macarte = folium.Map(location=[10,-20], zoom_start=3)

#################################
# connexion
#################################
engine = create_engine("mysql://root:iznogod01@localhost/hurricanes")
conn = engine.connect()

sql = "select distinct code, name from reference where  code regexp '2018'"
res = conn.execute(sql)

for line in res:
    # print code
    print( line[0] )
    sql = "select  latitude, longitude from data where code = %s"
    pos = conn.execute(sql, (line[0]))
    points = []
    for p in pos:
        if p[0][-1] == 'N':
            lat = float( p[0][:-1] )
        else:
            lat = - float( p[0][:-1] )
        if   p[1][-1] == 'E':
            lon = float( p[1][:-1] )
        else:
            lon = - float( p[1][:-1] )

        points.append((lat,lon))

    folium.CircleMarker( points[0] , radius = 3, popup = line[0] + '<br>' + line[1]).add_to(macarte)
    folium.PolyLine(points, color='red').add_to(macarte)

#save to html file
macarte.save('f_7.html')
