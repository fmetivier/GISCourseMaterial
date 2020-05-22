#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:16:23 2020

@author: metivier

folium maps

simple map with IPGP places in the world

"""
import folium

#create the map
macarte = folium.Map(location=[25,2.4], zoom_start=3)

#add markers
folium.Marker([48.845366, 2.358222], popup="<img src='../include/images/cuvier.jpg' width='200px' /> <b>Institut de Physique du globe de Paris</b> <br>Main Cuvier Campus").add_to(macarte)
folium.Marker([48.827624, 2.380330], popup="<img src='../include/images/lamarckA.jpg' width='200px' /> <img src='../include/images/lamarckB.jpg' width='200px' /><b>Institut de Physique du globe de Paris</b><br>UP Campus").add_to(macarte)
folium.Marker([15.979679, -61.702719], popup="<img src='../include/images/ovsg.jpg' width='200px' /> <b>Institut de Physique du globe de Paris</b> <br>Guadeloupe Observatory").add_to(macarte)
folium.Marker([14.734571, -61.159924], popup="<img src='../include/images/ovsm.jpg' width='200px' /> <b>Institut de Physique du globe de Paris</b> <br>Martinique Observatory").add_to(macarte)
folium.Marker([-21.208519, 55.571905], popup="<img src='../include/images/piton.jpg' width='200px' /> <b>Institut de Physique du globe de Paris</b> <br>La Réunion Observatory").add_to(macarte)
folium.Marker([48.025666, 2.260932], popup="<img src='../include/images/chambon.jpg' width='200px' /> <b>Institut de Physique du globe de Paris</b> <br>Chambon le forêt Observatory").add_to(macarte)


#save to html file
macarte.save('f_1.html')
