# -*- coding: utf-8 -*-
"""
pm_6.py

plots the histogram of wind directions at Saint-Maur as a polar plot.
"""
#import libraries
import matplotlib.pylab as py
import openDB as odb


#get the data
#establish the connection
o = odb.OpenDB(base = "Parcelle", user = "root", passwd = "root", host = "localhost")
#write and execute the query
sql = "select round(winddir/20)*20, count(winddir) from imetos group by round(winddir/20)*20 order by winddir" 

res = o.execQuery(sql)
print(res)
#retrieve the results
radii = []
theta = []
for r in res:
	if r[0] == 360: # add the 360 to the 0 class
		radii[0] += r[1]
	else:
		theta.append(float(r[0]))
		radii.append(r[1])
		
#plot the result
theta = py.array(theta)*py.pi/180.
radii = py.array(radii)

print(theta)

# force square figure and square axes as it looks better for polar plots
fig = py.figure(figsize=(8,8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)

width = 20.*py.pi/180.
bars = py.bar(theta, radii, width = width, bottom = 0.0)
for r,bar in zip(radii, bars):
    bar.set_facecolor("r")
    bar.set_edgecolor("k")
    bar.set_alpha(0.5)

py.show()
